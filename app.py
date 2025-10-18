import streamlit as st
from passguard import score_password, generate_password

st.title("🔐 PassGuard — Password Strength Checker & Generator")

st.header("Check Password Strength")
pw = st.text_input("Enter a password to check:", type="password")
if st.button("Check"):
    if pw:
        r = score_password(pw)
        st.metric("Strength", r["classification"], f"{r['score']}/100")
        st.write(f"Entropy: {r['entropy']} bits")
    else:
        st.warning("Please enter a password first!")

st.header("Generate Strong Password")
length = st.slider("Length", 8, 64, 16)
symbols = st.checkbox("Include symbols", True)
if st.button("Generate"):
    pw = generate_password(length, symbols)
    st.code(pw)
    st.info("Copy this password manually or use the CLI --copy option.")
