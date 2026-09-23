# import pytest
# from playwright.sync_api import expect

# @pytest.mark.parametrize("username, password, passed",[
#     ("standard_user", "secret_sauce", True),
#     ("wrong_user", "secret_sauce", False)
# ])

# def test_login2(page, username, password, passed):
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill(username)
#     page.locator("#password").fill(password)
#     page.locator("#login-button").click()
#     if passed:
#         expect(page.locator(".title")).to_have_text("Products")
#     else:
#         expect(page.locator("h3")).to_contain_text("Epic sadface: ")    

# def test_addTocart(page):
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill("standard_user")
#     page.locator("#password").fill("secret_sauce")
#     page.locator("#login-button").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
#     expect(page.locator(".shopping_cart_badge")).to_have_text("2")

# def test_checkout(page):
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill("standard_user")
#     page.locator("#password").fill("secret_sauce")
#     page.locator("#login-button").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
#     expect(page.locator(".shopping_cart_badge")).to_have_text("2")
#     page.locator(".shopping_cart_link").click()
#     page.locator("#checkout").click()
#     expect(page.locator(".title")).to_have_text("Checkout: Your Information")
#     page.locator("#first-name").fill("John")
#     page.locator("#last-name").fill("Doe")
#     page.locator("#postal-code").fill("12345")
#     page.locator("#continue").click()
#     expect(page.locator(".title")).to_have_text("Checkout: Overview")
#     page.locator("#finish").click()


