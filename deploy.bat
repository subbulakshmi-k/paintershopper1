@echo off
echo 🚀 Deploying Django Project to Heroku (Windows)...

echo.
echo 📋 Checking if Heroku CLI is installed...
heroku --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Heroku CLI is not installed.
    echo.
    echo 🔗 Download Heroku CLI for Windows:
    echo    https://cli-assets.heroku.com/heroku-x64.exe
    echo.
    echo 📝 Installation steps:
    echo    1. Download the installer
    echo    2. Run the installer
    echo    3. Restart your command prompt
    echo    4. Run this script again
    pause
    exit /b 1
)

echo ✅ Heroku CLI is installed.

echo.
echo 🔐 Logging into Heroku...
heroku login

echo.
echo 📦 Creating Heroku app...
heroku create painter-shopper-app

if %errorlevel% neq 0 (
    echo.
    echo ⚠️  App creation might have failed. Let's continue anyway...
)

echo.
echo 🐍 Setting Python runtime...
heroku stack:set heroku-22

echo.
echo 📤 Adding files to git...
git add .

echo.
echo 💾 Committing changes...
git commit -m "Deploy Django project to Heroku"

echo.
echo 🚀 Deploying to Heroku...
git push heroku main

echo.
echo 🗄️ Running database migrations...
heroku run python manage.py migrate

echo.
echo ✅ Deployment complete!
echo.
echo 🌐 Your app should be live at: https://painter-shopper-app.herokuapp.com
echo 🔗 Admin panel: https://painter-shopper-app.herokuapp.com/admin
echo.
echo 📝 Optional: Create admin user by running:
echo    heroku run python manage.py createsuperuser
echo.
pause
