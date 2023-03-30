import pytest
from selene import browser


@pytest.fixture()
def setup_browser():
    browser.config.hold_browser_open = True
    browser.config.browser_name = 'chrome'

