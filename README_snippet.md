# 🔐 PassGuard — Password Strength Checker & Generator

## Quick Usage

```bash
# create and activate venv
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# check strength
python3 passguard.py check "P@ssw0rd123"

# generate password
python3 passguard.py gen --length 20

# launch web demo
streamlit run app.py
yaml


---

## 🚀 3️⃣ Run it in VS Code Terminal

```bash
# (Linux/Kali)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python3 passguard.py check "Test@123"
python3 passguard.py gen --length 20
streamlit run app.py
or on Windows PowerShell:

powershell

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
python passguard.py check "Test@123"
python passguard.py gen --length 20
streamlit run app.py