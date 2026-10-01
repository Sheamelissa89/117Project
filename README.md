# Django Portfolio — FSDI 117

**Student:** Shea Mullin  
**Cohort:** 68  
**Assignment 1:** Models for the Projects Section of My Portfolio

## Overview

This project is a Django portfolio application that stores project information and skills in a database and displays them dynamically on the Projects page.

Assignment 1 focuses on creating the Project and Skill models, registering them in Django admin, populating project data, and rendering that data through a Django view and template.

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Pillow

## Features

- Project and Skill models registered in Django admin
- Project records with titles and descriptions
- Optional project images and URLs
- Many-to-many relationship between projects and skills
- Custom string representations for model records
- Dynamic project content displayed at `/projects/`

## Database Models

### Skill

The Skill model stores a skill name. Skills can be associated with multiple projects.

### Project

The Project model stores:

- Title
- Description
- Optional image
- Optional URL
- Associated skills through a `ManyToManyField`

Both models include `__str__` methods to make their records readable in Django admin.

## Implementation

- Created the Project and Skill model definitions.
- Installed Pillow to support Django image fields.
- Created and applied database migrations.
- Registered both models in Django admin.
- Added the project “Project 117 FullStack” with a description and the skills Python, Django, HTML, CSS, and SQLite.
- Connected the Projects page to database records through a Django view, URL route, and template.
- Confirmed that `/projects/` rendered successfully and returned HTTP 200.

## Running Locally

Run the following commands from the directory containing `manage.py`, with your Python environment activated and the project dependencies installed:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver