from playwright.sync_api import expect

class homePage:

    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        # self.menubutton = page.locator("#react-burger-menu-btn")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_count = page.locator(".shopping_cart_badge")
        self.backpack_item = page.locator("#add-to-cart-sauce-labs-backpack")
        self.backlight_item = page.locator("#add-to-cart-sauce-labs-bike-light")

    def open(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def verify_home_page(self):
        expect(self.title).to_be_visible()

    def addItemtocart(self):
        self.backpack_item.click()
        self.backlight_item.click()

    def checkCartbadge(self):
        expect(self.cart_count).to_have_text("2")

    def openCart(self):
        self.cart_link.click()