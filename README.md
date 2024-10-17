# Django Inventory Management Application

This is a Django-based application for managing inventory items. It includes features for creating, reading, updating, and deleting items, with Redis caching implemented for performance optimization.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Usage Examples](#usage-examples)
- [License](#license)

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Redis (running locally or accessible via network)
- PostgreSQL (database management system)

## Installation

### Install PostgreSQL

1. **Download PostgreSQL**:
   - Visit the [PostgreSQL download page](https://www.postgresql.org/download/) and choose the installer for your operating system (Windows).

2. **Install PostgreSQL**:
   - Follow the instructions in the installer to complete the installation.
   - During the installation, you can set a password for the default `postgres` user.

3. **Set Up PostgreSQL Database**:
   - Open the PostgreSQL command line or use a tool like pgAdmin to create a new database for your Django application.
   - Example commands to create a database via command line:
     ```bash
     psql -U postgres
     CREATE DATABASE inventery;
     CREATE USER yourusername WITH PASSWORD 'yourpassword';
     ALTER ROLE yourusername SET client_encoding TO 'utf8';
     ALTER ROLE yourusername SET default_transaction_isolation TO 'read committed';
     ALTER ROLE yourusername SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE inventory_management TO yourusername;
     ```

### Install Required Python Packages

To install the required packages, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/inventory_management.git
   cd inventory_management


2. **Install required packages:**
   pip install -r requirements.txt

3. **Create a New Django Project**
   django-admin startproject inventory_management
  django-admin startproject inventory_management
  cd inventory_management
  python manage.py startapp inventory

 4. **Configure the Django Project**
Update **settings.py:** Open inventory_management/settings.py and configure the database and caching settings as follows:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventery',  # Your database name
        'USER': 'postgres',    # PostgreSQL username
        'PASSWORD': '****',    # PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',        # Default PostgreSQL port
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

INSTALLED_APPS = [
    ...
    'rest_framework',
    'inventory',  # Your app name
]

5. **Run Database Migrations:**
    Execute the following command to set up the database:
   - python manage.py migrate
     
6. **Create a Superuser:**
Create a superuser to access the Django admin interface:
- python manage.py createsuperuser

7. **Run the Development Server**
   - python manage.py runserver

8. **Run the API**
   -Refer the documention to the CRUD operations
   
9.  **Unit Testing**
    - cd inventory_management/inventory
    - mkdir tests
     ** Run command**
    - python manage.py test inventory.tests.test
      
