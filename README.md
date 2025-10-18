# 🛡️ Password Strength Checker & Generator

[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-ready-orange)](https://streamlit.io/)
[![Live demo](https://img.shields.io/badge/Live-Demo-blue?logo=streamlit)](https://password-strength-checker-asura-lord.streamlit.app/)
[![Repo size](https://img.shields.io/github/repo-size/Asura-Lord/Password-Strength-Checker)](https://github.com/Asura-Lord/Password-Strength-Checker)
[![CI](https://github.com/Asura-Lord/Password-Strength-Checker/actions/workflows/ci.yml/badge.svg)](https://github.com/Asura-Lord/Password-Strength-Checker/actions)


    <img src="<img width="1723" height="865" alt="Screenshot 2025-10-18 112241" src="https://github.com/user-attachments/assets/97d6c039-00ad-48d7-99b2-a175552681e1" />


<p align="center"><em>Live demo: <a href="https://password-strength-checker-asura-lord.streamlit.app/">https://password-strength-checker-asura-lord.streamlit.app/</a></em></p>

## Table of Contents
- Overview
- Why this matters
- Features
- Quick start
- Usage
- Generator tips
- Scoring overview
- Project structure
- Contributing
- Security & privacy
- License
- Contact

---

## Overview
A compact Streamlit app that inspects password strength, suggests improvements, and generates battle‑ready passwords. Built for developers and security enthusiasts who want a hands‑on look at password hygiene.

Transparent scoring logic + an interactive UI let you learn what makes passwords fail under attack — and how to fix them.

---

## Why this matters
Attackers rely on low entropy: short length, predictable words, common substitutions, and reused patterns. This tool highlights those weaknesses so you can fix them before someone else exploits them.

---

## Features
- Live password strength evaluation: Weak / Medium / Strong  
- Scoring factors:
  - Length (high weight)
  - Upper / lower case mix
  - Digit variety
  - Special characters / symbols
  - Basic dictionary & predictable pattern checks
- Random password generator with adjustable length & character classes
- Copy-to-clipboard utility (pyperclip)
- Streamlit UI for fast, interactive testing
- Educational notes: brute-force, dictionary attacks, rainbow tables & mitigations

---

## Quick start (run locally in ~60s)

Clone the project and run it in an isolated virtual environment.

Windows (PowerShell)
```powershell
git clone https://github.com/Asura-Lord/Password-Strength-Checker.git
cd Password-Strength-Checker

python -m venv .venv
# Activate the virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies and run
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

macOS / Linux (bash)
```bash
git clone https://github.com/Asura-Lord/Password-Strength-Checker.git
cd Password-Strength-Checker

python3 -m venv .venv
# Activate the virtual environment
source .venv/bin/activate

# Install dependencies and run
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

Open the URL printed by Streamlit (usually http://localhost:8501).

Notes:
- Using `python -m streamlit run` ensures Streamlit runs under the venv interpreter.
- Add `.venv/` to `.gitignore` — do not commit your environment.

---

## Usage
- Enter a password to see a score and targeted suggestions.
- Click "Generate Password" to create a secure password; tune length and character sets as needed.
- Copy generated passwords to your password manager (avoid storing them in plaintext).

Example:
- Passphrase: "correct horse battery staple!" → far stronger than "P@ssw0rd123"

Practical tips:
- Target 12+ characters for general use; 16+ (or a long passphrase) for sensitive accounts.
- Never reuse passwords across services.
- Use a password manager + enable 2FA.

---

## Generator tips
- Entropy grows with length: +1 char ≈ +log2(charset_size) bits.
- Mix character classes for much higher brute-force cost.
- Prefer long passphrases if you must remember the password; otherwise use a password manager.

Default generator settings in this project:
- Length: 16
- All character classes included
- Avoids simple dictionary outputs

---

## How it scores passwords (overview)
Scoring factors:
- Length (largest influence)
- Character variety (upper/lower/digits/symbols)
- Patterns: repeated sequences, sequential chars, common words
- Penalties for obvious weak patterns (e.g., "1234", "password", keyboard walks)

Labels:
- Weak ≤ X
- Medium > X and ≤ Y
- Strong > Y

(Exact thresholds and algorithm live in passguard.py — review and tweak to match your threat model.)

---

## Project structure
Password-Strength-Checker/
- app.py           — Streamlit front-end
- passguard.py     — Scoring & generator logic
- requirements.txt — dependencies (pin versions for reproducible demos)
- README.md        — this file
- .venv/           — local virtual environment (ignored)

---

## Contributing
Ideas welcome: improve scoring, integrate stronger dictionary checks, add CLI mode, add tests.

Recommended workflow:
1. Fork the repo
2. Create a branch: `git checkout -b feature/my-change`
3. Implement & test
4. Open a PR with a clear description and rationale

Keep dependencies minimal and document any security trade-offs.

---

## Security & privacy
- This is an educational tool. Misuse for unauthorized access is illegal and unethical.
- All checks in this repo are local to your machine / Streamlit server; no password data is transmitted externally by default.
- Do not paste production passwords into public/demo instances. Prefer local, isolated environments for sensitive testing.

Suggested privacy statement to display in demos:
"All password checks and generation occur locally. No password data is sent to external services."

---

## License
MIT License — (c) 2025 Asura-Lord  
See LICENSE file for full text.

---

## Contact
Report bugs or request features: https://github.com/Asura-Lord/Password-Strength-Checker/issues  
Author: Asura-Lord — https://github.com/Asura-Lord

Stay safe. Harden the gates. 🖤<img width="1723" height="865" alt="Screenshot 2025-10-18 112241" src="https://github.com/user-attachments/assets/f6643c79-c349-4b33-ae40-e204bfa80c64" />
