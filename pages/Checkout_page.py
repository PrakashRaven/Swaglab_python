from playwright.sync_api import expect

class Checkout:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

    def navigate_to_checkout_page(self):
        self.page.goto("https://www.saucedemo.com/checkout-step-one.html")

    def verify_checkout_page(self):
        expect(self.title).to_have_text("Checkout: Your Information")

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    
