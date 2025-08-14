#!/usr/bin/env python3
"""
Test script for the Energy Assistant Chatbot
"""

import sys
import os

# Add the current directory to the path
sys.path.append(os.path.dirname(__file__))

def test_chatbot_import():
    """Test if the chatbot module can be imported successfully"""
    try:
        from pages.chatbot import show_chatbot, load_data, get_energy_insights
        print("✅ Chatbot module imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Error importing chatbot module: {e}")
        return False

def test_data_loading():
    """Test if the data loading function works"""
    try:
        from pages.chatbot import load_data
        df = load_data()
        if df is not None:
            print(f"✅ Data loaded successfully! Shape: {df.shape}")
            print(f"   Columns: {list(df.columns)}")
            return True
        else:
            print("⚠️ Data loading returned None")
            return False
    except Exception as e:
        print(f"❌ Error in data loading: {e}")
        return False

def test_insights_generation():
    """Test if insights generation works"""
    try:
        from pages.chatbot import load_data, get_energy_insights
        df = load_data()
        if df is not None:
            insights = get_energy_insights(df)
            print(f"✅ Insights generated successfully!")
            print(f"   Total records: {insights.get('total_records', 'N/A')}")
            print(f"   Energy columns: {len(insights.get('energy_columns', []))}")
            print(f"   CO2 columns: {len(insights.get('co2_columns', []))}")
            print(f"   Building columns: {len(insights.get('building_columns', []))}")
            return True
        else:
            print("⚠️ Cannot test insights without data")
            return False
    except Exception as e:
        print(f"❌ Error in insights generation: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Energy Assistant Chatbot...\n")
    
    tests = [
        ("Module Import", test_chatbot_import),
        ("Data Loading", test_data_loading),
        ("Insights Generation", test_insights_generation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Running: {test_name}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append((test_name, False))
        print()
    
    # Summary
    print("📊 Test Results Summary:")
    print("=" * 40)
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The chatbot is ready to use.")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main() 