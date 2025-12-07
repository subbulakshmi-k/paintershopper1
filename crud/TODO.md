# TODO: Building and Running the Django Project Locally

## Steps to Complete:

1. **Edit settings.py**: Update `painter/painter/settings.py` to set `DEBUG = True` for local development.
   - Status: Completed

2. **Activate Virtual Environment**: Run the activation script to enable the project's dependencies.
   - Status: Completed (venv already active or python from venv used)

3. **Navigate to Project Directory**: Change to the `painter` directory where `manage.py` is located.
   - Status: Completed

4. **Run Database Migrations**: Execute `python manage.py migrate` to apply any database changes.
   - Status: Completed (No migrations to apply)

5. **Collect Static Files**: Run `python manage.py collectstatic --noinput` to gather static assets.
   - Status: Completed (0 copied, 134 unmodified)

6. **Start Development Server**: Execute `python manage.py runserver` to launch the application locally.
   - Status: Completed (Server started)

7. **Verify and Test**: Confirm the server is running and accessible at http://localhost:8000. Test basic functionality.
   - Status: Pending (User can test now)

After completing each step, this file will be updated to reflect progress.
