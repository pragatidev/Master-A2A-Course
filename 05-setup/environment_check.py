
#!/usr/bin/env python3
"""
Environment Setup Verification Script
Run this to ensure your A2A development environment is ready!
"""

import os
import sys
from pathlib import Path

def check_python_version():
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print("✅ Python version:", f"{version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print("❌ Python 3.8+ required. Current:", f"{version.major}.{version.minor}.{version.micro}")
        return False

def check_environment_file():
    env_file = Path('.env')
    if not env_file.exists():
        print("❌ .env file not found. Copy .env.sample to .env first!")
        return False
    try:
        from dotenv import load_dotenv
        load_dotenv()
        openai_key = os.getenv('OPENAI_API_KEY')
        if openai_key and openai_key != 'your_openai_api_key_here':
            print("✅ OpenAI API key configured")
            return True
        else:
            print("❌ OpenAI API key not set in .env file")
            return False
    except ImportError:
        print("❌ python-dotenv not installed. Run: pip install -r requirements.txt")
        return False

def check_required_packages():
    required_packages = [
        'requests', 'pydantic', 'fastapi', 'jupyter',
        'loguru', 'openai', 'python-dotenv'
    ]
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    return True

def test_basic_functionality():
    try:
        from dotenv import load_dotenv
        import asyncio
        import requests
        print("✅ Basic imports working")
        openai_key = os.getenv('OPENAI_API_KEY')
        if openai_key and openai_key != 'your_openai_api_key_here':
            try:
                import openai
                client = openai.OpenAI(api_key=openai_key)
                print("✅ OpenAI client initialized successfully")
            except Exception as e:
                print(f"⚠️  OpenAI client warning: {e}")
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def main():
    print("🚀 Master A2A Course - Environment Check\n")
    checks = [
        check_python_version(),
        check_environment_file(),
        check_required_packages(),
        test_basic_functionality()
    ]
    if all(checks):
        print("\n🎉 Environment setup complete! You're ready to start learning A2A!")
        print("Next step: Open 01-notebooks/01_VS_Code_Environment_Setup.ipynb")
    else:
        print("\n❌ Setup incomplete. Please fix the issues above.")
        print("Check 05-setup/install_guide.md for detailed instructions.")

if __name__ == "__main__":
    main()
