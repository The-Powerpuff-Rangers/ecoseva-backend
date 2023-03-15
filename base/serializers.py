from rest_framework import serializers

from .models import UserAccount, DustbinGroup, Dustbin


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["email", "name", "password", "dob"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = UserAccount
        fields = ["email", "password"]

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        if email is None:
            raise serializers.ValidationError("An email address is required to log in.")
        user = UserAccount.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError("A user with this email is not found.")
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password.")
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["id", "phone", "email", "name", "dob", "date_joined"]


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["phone", "email", "name"]


class DustbinGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DustbinGroup
        fields = "__all__"


class DustbinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dustbin
        fields = "__all__"


class DustbinEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dustbin
        fields = ["status", "capacity"]
