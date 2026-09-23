from pages.login_page import LoginPage
from pages.home_page import homePage
from pages.Cart_page import Cart
from pages.Checkout_page import Checkout

def checkout(page):
    login_page = LoginPage(page)
    Home_page = homePage(page)
    Cart_page = Cart(page)
    checkout_page = Checkout(page)
    login_page.open()
    login_page.action("standard_user", "secret_sauce")
    Home_page.addItemtocart()
    Home_page.openCart()
    Cart_page.checkOut()
    checkout_page.fillCheckoutForm("John", "Doe", "12345")
