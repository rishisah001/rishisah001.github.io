#!/usr/bin/env python
import os
import sys
import django
import subprocess

def initialize_project():
    """Initialize the Django project with all necessary setup"""
    
    print("🚀 Initializing NASA Weather Insights Project...")
    
    # Create necessary directories
    directories = [
        'media/downloads',
        'static/css',
        'static/js',
        'static/images',
        'ml_models',
        'templates',
        'weather_dashboard/utils'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings')
    
    try:
        django.setup()
        
        # Run migrations
        print("📦 Setting up database...")
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        
        # Collect static files
        print("🎨 Collecting static files...")
        subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'], check=True)
        
        print("\n🎉 Project initialization completed successfully!")
        print("\n📋 Next steps:")
        print("1. Place your ML model files in the 'ml_models/' directory")
        print("2. Run: python manage.py runserver")
        print("3. Access: http://localhost:8000")
        print("\n🐛 For issues, check:")
        print("   - All required packages are installed")
        print("   - ML model files are in correct format")
        print("   - NASA POWER API is accessible")
        
    except Exception as e:
        print(f"❌ Error during initialization: {e}")
        sys.exit(1)

if __name__ == '__main__':
    initialize_project()