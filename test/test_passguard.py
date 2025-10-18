from passguard import score_password, generate_password

def test_gen_length():
    pw = generate_password(20)
    assert len(pw) == 20

def test_scoring():
    res = score_password("Aa1$")
    assert "classification" in res
