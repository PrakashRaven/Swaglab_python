from playwright.sync_api import expect

class Cart:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_count = page.locator(".shopping_cart_badge")
        self.backpack = page.get_by_text("Sauce Labs Backpack")
        self.bike_light = page.get_by_text("Sauce Labs Bike Light")
        #self.continue_shopping_button = page.locator("#continue-shopping")
        self.check_out_button = page.locator("#checkout")

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def verify(self):
        expect(self.title).to_have_text("Your Cart")
        expect(self.cart_count).to_have_text("2")
        expect(self.backpack).to_be_visible()
        expect(self.bike_light).to_be_visible()

    def checkOut(self):
        self.check_out_button.click()

    


    