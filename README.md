# Template-For-OOP-Layered-Architecture
Jinja2 Template For Creating The Layered Architecture In OOP Using Python

- Creates the files necessary to start an OOP project using two entities, including comments, validators and tests.

- Jinja2 templates that are used can be found under the folder *templates*.

- Directories that should exist in the same folder as the *Jinja2TemplateOOP.py* file: 
  - Domain, Repository, Tests, UserInterface -> each with an *__init__.py* empty file in it
  - Additionally, folder *filesDeleted* will be used to send the files from a previous run of the program.
 
- Layered Architecture:

  - **Domain**: creates the base classes for the entitites making use of the pre-existing *entitate.py* file. Includes validators depending on the type of the fields for every class.
  - **Repository**: makes use of a pre-existing *file_repository.py* file
  - **Tests**: creates tests for adding an entity (modification and deletion to be implemented). Domain and Repo tests are to be implemented. File *utils.py* includes a function that clears a file.
  - **User Interface**: creates the console menu for the given entitites including some space for additional functionalities.
  -  **Main.py**: file that controls the resulting project.
