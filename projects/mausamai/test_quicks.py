import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings')
django.setup()

from weather_dashboard.ml_model import WeatherPredictor

def quick_test():
    print("🧪 Quick ML Model Test")
    print("=" * 40)
    
    predictor = WeatherPredictor()
    
    # Check model availability
    print("📋 Model Availability:")
    available = predictor.check_models_available()
    for model, status in available.items():
        print(f"   {model}: {'✅' if status else '❌'}")
    
    # Test prediction (will use fallback if models not trained yet)
    print("\n🌤️  Test Prediction:")
    result = predictor.predict_weather(27.7172, 85.3240, "2024-12-25")
    
    print(f"Success: {result['success']}")
    print(f"Data Source: {result['data_source']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Predictions: {len(result['predictions'])}")
    
    for pred in result['predictions'][:3]:
        print(f"  {pred['condition']}: {pred['probability']}% ({pred['risk_level']})")

if __name__ == "__main__":
    quick_test()