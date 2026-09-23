import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, passed", [
    ("standard_user", "secret_sauce", True),
    ("wrong_user", "secret_sauce", False)
])
def test_login( page, username, password, passed):
    login = LoginPage(page)
    login.open()
    login.action(username, password)
    if passed:
        login.verify()
    else:
        login.login_error()