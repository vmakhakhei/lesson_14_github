import pytest
from selene.support.shared import browser


@pytest.fixture
def browser_setup():
    browser.config.window_width = 850
    browser.config.window_height = 800
    browser.config.hold_browser_open = True