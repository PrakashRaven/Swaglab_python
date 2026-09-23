from pages.login_page import LoginPage
from pages.home_page import homePage
from pages.Cart_page import Cart

def test_cartPage(page):
    login = LoginPage(page)
    home = homePage(page)
    cart = Cart(page)
    login.open()
    login.action("standard_user", "secret_sauce")
    home.addItemtocart()
    home.openCart()
    cart.verify()
    cart.checkOut()
