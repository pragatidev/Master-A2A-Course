
# Complete Installation Guide

Detailed setup instructions for the Master A2A course development environment.

## System Requirements

- **Operating System:** Windows 10/11, macOS 10.15+, or Linux
- **Python:** Version 3.8 or higher
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 2GB free space for course materials

## Step-by-Step Installation

### 1. Install Python 3.8+

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH" during installation

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python@3.11

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

### 2. Install VS Code

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install with default settings
3. Install required extensions (automatic when opening workspace)

### 3. Clone and Setup Course Repository

```bash
# Clone the repository
git clone https://github.com/[username]/Master-A2A-Course.git
cd Master-A2A-Course

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Copy environment template
cp .env.sample .env
```

### 4. Configure Environment Variables

Edit the `.env` file:

```env
# Required: Add your OpenAI API key
OPENAI_API_KEY=sk-your-actual-key-here

# Optional: Customize other settings
OPENAI_MODEL=gpt-4o-mini
LOG_LEVEL=INFO
DEBUG_MODE=True
```

**Getting OpenAI API Key:**
1. Visit [platform.openai.com](https://platform.openai.com/)
2. Create account or sign in
3. Go to API Keys section
4. Create new secret key
5. Copy to your `.env` file

**Cost Estimate:** $3–5 for complete course (using gpt-4o-mini)

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Verify Installation

```bash
python 05-setup/environment_check.py
```

You should see all green checkmarks ✅

### 7. Open Course in VS Code

```bash
code Master-A2A-Course.code-workspace
```

VS Code will automatically:
- Configure Python interpreter
- Install recommended extensions
- Set up Jupyter notebook environment

## Troubleshooting

### Common Issues

**ImportError: No module named 'xyz'**
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

**VS Code doesn't recognize Python**
- Open Command Palette (Ctrl+Shift+P)
- Type "Python: Select Interpreter"
- Choose the Python from your virtual environment

**Jupyter notebooks won't run**
- Install Jupyter extension in VS Code
- Restart VS Code
- Select correct Python kernel in notebook

**OpenAI API errors**
- Verify API key in `.env` file
- Check account has available credits
- Ensure no extra spaces in API key

### Getting Help

1. **Environment Check:** Run `python 05-setup/environment_check.py`
2. **Course Discussion:** Use Udemy course Q&A section
3. **GitHub Issues:** Open issue in course repository
4. **LinkedIn:** Message [@pragatikunwer](https://linkedin.com/in/pragatikunwer)

## Next Steps

Once setup is complete:

1. ✅ Verify green checkmarks from environment check
2. 📝 Open `01-notebooks/01_VS_Code_Environment_Setup.ipynb`
3. 🚀 Start building your first A2A agent network!

## Optional Tools

**Git GUI (for beginners):**
- [GitHub Desktop](https://desktop.github.com/)
- [SourceTree](https://www.sourcetreeapp.com/)

**Database Browser (for advanced projects):**
- [DB Browser for SQLite](https://sqlitebrowser.org/)

---

**Setup taking too long?** The environment check script will identify exactly what needs attention. Most issues are resolved in under 5 minutes!
