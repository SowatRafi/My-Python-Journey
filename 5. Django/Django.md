**Install**
`pip install Django`
****

**Creating a `Django` project**

* Make sure you are in your project directory.

`django-admin startproject (Project Name) .`
****

* Avoid naming projects after built-in Python or Django components.
Example: `Django` or `test`. Which conflicts with built-in `python` _package_.
  (`.`) tells the script to install `Django` in your current directory. This avoids the creation of an extra outer directory with same name as the _project directory_. This can be _renamed_ if created.
****

**Components created by `stratproject` script**

* The outer `myProject/` root directory is just a container for your project. Its name doesn't matter to `Django`; you can rename it to anything you like.

* `manage.py` - A command-line utility that lets you interact with this Django project in various ways.

* The inner `myProject/` directory is actual `Python` package for your project. Its name is the `Python` package name you will need to use to `import` anything inside it. (_e.g. `mysite.urls`_)

* `mysite/__init__.py` - An empty file that tells `Python` that this directory should be considered a `Python` Package.

* `mysite/asgi.py` - ASGI, or the Asynchronous Server Gateway Interface, is the specification which Channels and Daphne are built upon, designed to untie Channels apps from a specific application server and provide a common way to write application and middleware code.
  It’s a spiritual successor to WSGI, designed not only run in an asynchronous fashion via asyncio, but also supporting multiple protocols.

* `mysite/settings.py` - _Setting/configuration_ for the `Django` _project_.

* `mysite/urls.py` - The **URL** declarations for this `Django` project; a "**table of contents**" of your `Django-powered` site.

* `mysite/wsgi.py` - An entry-point for **WSGI-compatible** _web server_ to serve your _project_.
****
**Starting `Django` development server**

`python manage.py runserver` _By default it uses port: **8000**_

`python manage.py runserver 8080` _For running in **8080**_
****

**Migrations**

* `Django` uses `migration`s to propagate _changes to your model into your database schema_.
  (_Model are source of information about your data you are storing._)
  
* They are designed to be mostly **automatic**.
* **Migration**s are alike _version control system_ for your **database schema**.
****
**Migration Commands**

`python manage.py migrate` - Applies and unapplied _migrations_

`python manage.py makemigrations` - Creates new _migrations_ based on changes you make to your models.

`python manage.py sqlmigrate` - Display the `SQL statements` for a _migration_.

`python manage.py showmigrations` - Lists a _project's_ `migrations` and _their status_.
****

**Create a Django App**

* By convention `app` names are plural.

`django-admin startapp (App name)`

* Avoid **naming** `apps` after _built-in_ `Python` or `Django` components.
Example: `Django` or `test`. Which **conflicts** with _bulit-in_ `Python` package.
****

**Activating your `App`**

* To **activate** your `app` so the **project is aware** of it you need to add it to the list of installed `apps` inside `settings.py` file.
* This allows `Django` to keep tract of the `app` and let you do stuff with the `app` in the **project** like creating tables etc.
****

`Django Admin` **and** `Superuser`

`python manage.py createsuperuser`

* `Django` comes with built-in administrative interface page.

* `Django` `superuser` is used to manage the `Django admin` page.
****

**Templates**

* A template contains static parts of desired HTML output.

* A template also has some special syntax for dynamic content.

* Special template tags `{%tag%}`

* Special template variables: `{{variable}}`

* Special template variable and filters: `{{variable | filter}}`
****

**Adding mockup design template to `Django`**

**APP DIRECTORY** _>_ `templates` **>** `app directory name` **>** `add index.html`

**APP DIRECTORY** _>_ `static` **>** `app directory name` **>** `add bs & css`
****

**Views**

* A _view_ function, or _view_ for short, is simply a Python function that takes a **Web request** and returns a **Web response**.

* This response can be the `HTML` contents of a **Web page**, or a redirect, or a `404 error`, or an `XML document`, or an **image** etc.

* The _view_ itself contains whatever arbitrary **logic necessary** to **return that response**.

* This _code_ can live **anywhere you want**, as long as it's on your **Python Path**. or the sake of putting the code _somewhere_, the convention is to put views in a file called `views.py`, placed in your project or _application directory_.
****

**URL and URL Patterns**

* URL stands for Uniform Resource Locator. It is a website's address.

* URL patterns includes the path of url request and where to send it.
****

**`Django` `Models`**

* `Django` models are `Python` _classes_ that allows us to save data inside a database.

* All objects is a row in a table.

* A **model** is single source of information about your data.

* A **model** contains the essential fields and behaviours of the data you are storing.

* Each **model** maps to a single database table.

* Each **model** is `Python` `class` that subclasses `djanog.db.models.Model`

* Each attribute of the **model** represents a **database** field.


**Example:**

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
Equivalent to:

    CREATE TABLE myapp_person(
        "id" serial NOT NULL PRIMARY KEY,
        "first_name" varchar(30) NOT NULL,
        "last_name" varchar(30) NOT NULL,
****

**Migrating `Models`**

1. `python manage.py makemigartions`

2. `python manage.py migrate`
****


**Database Setup**

* `SQLite` is the **default database configuration** for `Django`.
* `Django` supports _other_ database systems like:
  1. `PostgreSQL`,
  2. `Oracle`,
  3. `MySQL`
    

     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          # 'NAME': BASE_DIR / 'db.sqlite3',
          'NAME': 'portfoliodb',
          'USER': 'postgres',
          'PASSWORD': 'password',
          'HOST': 'Test Server',
          'PORT': 5432,
        }
      }

You also need to `pip3 install psycopg2`
****
