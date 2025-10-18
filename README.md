🛡️ Password Strength Checker & Generator

“Weak passwords are an open invitation to hackers. Strengthen your shield.”

🔥 Overview

This project is a Password Strength Checker & Generator designed to:

Assess how strong your passwords are.

Generate strong, secure passwords.

Teach you what hackers look for when breaking weak passwords.

It’s simple, effective, and built with real-world cybersecurity in mind.

🛠️ Features

Check Password Strength

Weak / Medium / Strong evaluation.

Score based on:

Length

Uppercase & lowercase letters

Numbers

Special characters

Password Generator

Generates random strong passwords.

Copy generated password to clipboard.

Educational Value

Learn what makes a password hackable.

Understand hacker techniques like brute-force, dictionary attacks, and rainbow tables.

⚡ Requirements

Python 3.10+

Streamlit

pyperclip

Other dependencies in requirements.txt

Lightweight setup recommended to avoid heavy packages like TensorFlow if you just need basic functionality.

💻 Installation & Setup (Windows / PowerShell)
# Clone the repo
git clone https://github.com/Asura-Lord/Password-Strength-Checker.git
cd Password-Strength-Checker

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Run the app
streamlit run app.py

🐧 Installation & Setup (Linux / Bash)
# Clone the repo
git clone https://github.com/Asura-Lord/Password-Strength-Checker.git
cd Password-Strength-Checker

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies
python3 -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Run the app
streamlit run app.py

🚀 How to Use

Open the app using Streamlit (streamlit run app.py).

Enter a password to check strength.

Use Generate Password button to create strong passwords.

Copy password to clipboard and use safely.

📂 Project Structure
Password-Strength-Checker/
├── app.py               # Main Streamlit app
├── passguard.py         # Password strength logic
├── requirements.txt     # Dependencies
├── .venv/               # Virtual environment (local)
└── README.md            # This file

⚠️ Warning (Hacker Style 😎)

Weak passwords are dangerous. Don’t give hackers a free ticket.
Your safety online is only as strong as your weakest password.

💀 Use this tool responsibly. Secure your accounts, learn, and stay one step ahead of the hackers.
