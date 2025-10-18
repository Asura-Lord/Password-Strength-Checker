#!/usr/bin/env python3
import argparse, secrets, string, math

try:
    import pyperclip
    HAS_CLIP = True
except ImportError:
    HAS_CLIP = False


def score_password(pw):
    length = len(pw)
    lower = any(c.islower() for c in pw)
    upper = any(c.isupper() for c in pw)
    digit = any(c.isdigit() for c in pw)
    symbol = any(not c.isalnum() for c in pw)

    charset = 0
    if lower: charset += 26
    if upper: charset += 26
    if digit: charset += 10
    if symbol: charset += 32
    entropy = round(length * math.log2(charset), 2) if charset else 0
    score = min(entropy / 60 * 100, 100)

    if score < 40: level = "Weak"
    elif score < 70: level = "Medium"
    else: level = "Strong"

    return {"password": pw, "score": round(score, 1), "classification": level, "entropy": entropy}


def generate_password(length=16, symbols=True):
    alphabet = string.ascii_letters + string.digits
    if symbols:
        alphabet += "!@#$%^&*()-_=+[]{}"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def main():
    p = argparse.ArgumentParser(description="PassGuard — Password Strength Checker & Generator")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check"); c.add_argument("password")
    g = sub.add_parser("gen"); g.add_argument("--length", type=int, default=16)
    g.add_argument("--no-symbols", action="store_true"); g.add_argument("--copy", action="store_true")

    a = p.parse_args()

    if a.cmd == "check":
        res = score_password(a.password)
        print(f"[{res['classification']}] Score: {res['score']}/100  Entropy: {res['entropy']} bits")

    elif a.cmd == "gen":
        pw = generate_password(a.length, not a.no_symbols)
        print(pw)
        if a.copy and HAS_CLIP:
            pyperclip.copy(pw); print("(Copied to clipboard)")

if __name__ == "__main__":
    main()
