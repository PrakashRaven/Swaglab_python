from pages.home_page import homePage
from pages.login_page import LoginPage

def test_homepage(page):
    login = LoginPage(page)
    homepage = homePage(page)
    login.open()
    login.action("standard_user", "secret_sauce")
    homepage.verify_home_page()
    homepage.addItemtocart()
    homepage.checkCartbadge()
    homepage.openCart()
