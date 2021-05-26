######
README
######

Aquaponics_System
*****************
.. Brief description of project, what it is used for.

Installing / Getting started
============================
.. Introduction of minimal setup.
   Command, followed by explanation in next paragraph or after every command.

Developing
==========
Built with
----------
.. List of main libraries, frameworks used including versions.

Prerequisites
-------------
.. What is needed to set up dev environment.
   For instances, dependencies or tools include download links.

Setting up dev
--------------
.. Brief intro of what to do to start developing.
   Commands with explanations as well.
1. ``Clone`` repository into local system.
2. ``cd`` to ``./Aquaponics_System``.
3. ``pip install -r requirements.txt``.
4. You're ready!

Running dev version
-------------------
:NOTE: Perform points 2 to 6 **only** if it is **first** time.
:``$``: Terminal commands.
:``$$``: Python shell commands.

1. ``cd`` to ``src/Applications/AquaponicsDjango/``.
2. $ ``python3 manage.py shell``.
3. $$ ``from django.contrib.auth.models import User``.
4. $$ ``user = User.objects.create_user(<username>, password='<password>')``.
5. $$ ``user.save()``.
6. $$ ``exit()``.
7. Remember above username and password.
8. $ ``python3 manage.py makemigrations``.
9. $ ``python3 manage.py migrate``.
10. $ ``python3 manage.py runserver``.
11. Open another terminal and ``cd`` to ``src/AquaponicsSystem/``.
12. $ ``python3 main.py``.
13. System is up and running.
14. Ctrl-C in both terminals to quit.

Building
--------
.. How to build the project after working on it.
   Commands and explanation.

Deploying / Publishing
----------------------
.. How to build and release a new version?
   Commands and explanation.

Versioning
==========
.. SemVer versioning info, link to other versions.
0.0

Configuration
=============
.. Configurations a user can enter when using the project.

Tests
=====
.. Describe and show how to run tests with examples. Also, explain them with
   reasons.

Style guide
===========
.. Coding style and how to check it.

API Reference
=============
.. Links to API documentation, description, explanation.

Database
========
.. Database versions and usages with download links.
   Also include DB Schema, relations, etc.

Credits
=======
*  :File: ``src/AquaponicsSystem/EmulatedHardware/ProjectEssentials/``
   :User: `CXINFINITE <https://github.com/CXINFINITE>`_.
   :Repository: `ProjectEssentials-Python
                <https://github.com/CXINFINITE/ProjectEssentials-Python>`_.

Licensing
=========
.. State license and link to text version.
