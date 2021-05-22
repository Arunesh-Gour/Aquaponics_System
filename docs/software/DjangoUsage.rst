###########
DjangoUsage
###########

:Django version: 3.2

Development
===========
Test run
--------
1. ``cd`` to respective directory.
2. ``python manage.py makemigrations``.
3. ``python manage.py migrate``.
4. ``python manage.py runserver``.

Making urls
-----------
1. ``cd`` to respective directory.
2. ``cd`` to the **app** in which you want to make a new url.
3. Open ``urls.py``.
4. As per requirement add your **url** using ``path`` inside ``urlpatterns``.
5. Save and exit.

Developing instructions
-----------------------
*  Apps are sub-sections of main project, designed to be portable and easy.
*  We generally work on apps only and hook apps to main project.
*  ``urls.py`` contain url links to various **views** or **forms**.
*  ``models.py`` contain models structures in the way they are stored or
   represented inside database.
*  ``forms.py`` contain forms structure in form of classes or functions.
*  ``views.py`` links forms and models, and contain various **views**, which
   are directly linked to **urls**.
*  Views are main focus points to the project.
*  Additional files may be created directly inside an *app* directory, given
   that there is a need and separates the code based on purpose not
   functionality.
*  If creating a directory, include an ``__init__.py`` inside one, even if it is
   empty. This makes the directory look like a *module* to python making it
   easily accessible.
*  Django follows **M-V-C** (Model-View-Controller) architecture.

Helpful Links
-------------
*  `Templates
   <https://docs.djangoproject.com/en/3.2/topics/templates/>`_.
*  `Models
   <https://docs.djangoproject.com/en/3.2/topics/db/models/>`_.
*  `Django shortcut functions
   <https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/>`_.
*  `Many-to-many relationships
   <https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/>`_.
*  `Built-in template tags and filters
   <https://docs.djangoproject.com/en/3.1/ref/templates/builtins/>`_.
*  `Models' on_delete parameter
   <https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models#38389488>`_.
*  `Custom authentication
   <https://docs.djangoproject.com/en/3.2/topics/auth/customizing/>`_ - **not
   recommended**. Given only for support purposes or wherever it is *highly*
   **needed / required**.
