from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def open(self):
        self.page.goto("https://www.saucedemo.com/")
        
    def action(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify(self):
        expect(self.page.locator(".title")).to_have_text("Products")

    def login_error(self):
        expect(self.page.locator("h3")).to_contain_text("Epic sadface: ")
