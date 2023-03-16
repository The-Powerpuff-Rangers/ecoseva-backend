# EcoSeva
![Mockup4x](https://user-images.githubusercontent.com/69671407/225647892-b5c3453d-ab31-4169-8500-d531f0c1c60f.png)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)


This is a Django project that contains backend code for the `EcoSeva` wriiten in Django. This handles the registration of users, the creation of groups, `geo-location` of users, `reverse geocoding`, etc.

## Local Setup

To run this project locally, follow these steps:

- Clone the repository to your local machine.
- Create a virtual environment using Python 3.
- Activate the virtual environment.
- Install the required packages by running `pip install -r requirements/requirements.txt`.
- Create a `.env` file in the project root and set the required environment variables (e.g. `SECRET_KEY`, `DEBUG`, `DATABASE_URL`).
- Run the migrations by running `python manage.py migrate`.
- Start the development server by running `python manage.py runserver`.
- Visit http://localhost:8000/ in your web browser to view the project.

## Devcontainer Setup

This project includes a devcontainer configuration for use with Visual Studio Code's remote development feature. To use the devcontainer, follow these steps:

- Clone the repository to your local machine.
- Open the project in Visual Studio Code.
- Install the Remote Development extension pack.
- Open the Command Palette (Ctrl/Cmd + Shift + P) and select "Remote-Containers: Reopen in Container".
- Wait for the `devcontainer` to build and start. This may take several minutes the first time.
- Create a `.env` file in the project root and set the required environment variables (e.g. `SECRET_KEY`, `DEBUG`, `DATABASE_URL`).
- Run the migrations by running `python manage.py migrate`.
- Start the development server by running `python manage.py runserver`.
- Visit http://localhost:8000/ in your web browser to view the project.

## Swagger UI Support

This project includes support for Swagger UI, which provides a user-friendly interface for exploring and testing the project's API endpoints. To use Swagger UI, follow these steps:

- Start the development server by running `python manage.py runserver`.
- Visit http://localhost:8000/api/schema/docs in your web browser to view the Swagger UI page.
- Use the interface to explore the API endpoints and test them by sending requests.

## Project Structure

```
.
├── CONTRIBUTING.md
├── LICENCE
├── README.md
├── backend
├── base
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── managers.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   └── config.ini
├── db.sqlite3
├── kerver
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements
│   └── requirements.txt
├── schema.yml
├── static
│   └── json
│       └── overview.json
└── tools
    ├── commit-msg
    └── setup.sh
```
