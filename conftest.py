# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="function")
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         context.tracing.start(screenshots=True, snapshots=True)
#         page = context.new_page()
#         yield page
#         context.tracing.stop(path="tracing.zip")
#         browser.close()

import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false").lower() == "true"
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()    