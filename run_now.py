#!/usr/bin/env python3
"""
Quick runner - Use this to start
"""
import subprocess
import sys

print("Setting up LLM-BDD Testing System...")

# Install dependencies
print("\nInstalling dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "openai", "selenium", "webdriver-manager"])

print("\n✅ Dependencies installed!")
print("\n📝 IMPORTANT: Edit config.py with your OpenAI API key")
print("   Get free key from: https://platform.openai.com/api-keys")
print("\n🚀 To run: python py313_tester.py")
print("\nPress Enter to continue...")
input()

# Run main program
import py313_tester
py313_tester.main()