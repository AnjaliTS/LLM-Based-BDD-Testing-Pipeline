@echo off
echo Setting up LLM-BDD Testing for Python 3.13...
echo.

REM Create virtual environment
echo 1. Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

REM Install dependencies
echo.
echo 2. Installing dependencies...
pip install openai==1.3.0 selenium==4.16.0 webdriver-manager==4.0.1

echo.
echo 3. Setup complete!
echo.
echo IMPORTANT: Edit config.py with your OpenAI API key:
echo   - Go to: https://platform.openai.com/api-keys
echo   - Get free key (FREE $5 credit)
echo   - Replace "your-actual-key-here" in config.py
echo.
echo 4. To run the system:
echo    python py313_tester.py
echo.
pause