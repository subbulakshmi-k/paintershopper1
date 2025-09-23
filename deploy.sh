#!/bin/bash

echo "🚀 Deploying Django Project to Heroku..."

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI is not installed. Please install it first:"
    echo "   curl https://cli-assets.heroku.com/install.sh | sh"
    exit 1
fi

# Login to Heroku
echo "🔐 Logging into Heroku..."
heroku login

# Create Heroku app (if not exists)
echo "📦 Creating Heroku app..."
heroku create painter-shopper-app

# Set Python runtime
echo "🐍 Setting Python runtime..."
heroku stack:set heroku-22

# Deploy to Heroku
echo "🚀 Deploying to Heroku..."
git add .
git commit -m "Deploy Django project to Heroku"
git push heroku main

# Run Django migrations
echo "🗄️ Running database migrations..."
heroku run python manage.py migrate

# Create superuser (optional)
echo "👤 Creating admin user..."
echo "Run this command manually if needed:"
echo "heroku run python manage.py createsuperuser"

echo "✅ Deployment complete!"
echo "🌐 Your app is live at: https://painter-shopper-app.herokuapp.com"
echo "🔗 Admin panel: https://painter-shopper-app.herokuapp.com/admin"
