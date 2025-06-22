# diaoyu

This repository contains a Django project skeleton with a backend management interface using Tabler UI.

## Setup
1. Install Django (`pip install django`).
2. Run migrations:
   ```
   python manage.py migrate
   ```
3. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```

## Templates and UI
Templates under `core/templates/` extend `base.html`, which loads Tabler CSS and JS from CDN. Replace with local assets as needed.
