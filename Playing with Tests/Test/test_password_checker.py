from lib.password_checker import *

#Checks password is valid
def test_valid_password():
    checker = PasswordChecker()
    result = checker.check("Password123")
    assert result is True

#Checks password isn't valid
def test_invalid_password_too_short():
    checker = PasswordChecker()
    try:
        checker.check("Hello")
    except Exception as err:
        assert str(err) == "Invalid password, must be 8+ characters."

#Checks password is exactly 8 characters long
def test_invalid_password_exactly_8_chars():
    checker = PasswordChecker()
    result = checker.check('Eight123')
    assert result is True