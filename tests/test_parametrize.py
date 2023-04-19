"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=["mobile", "desktop"])
def browser_setting(request):
    browser.open("https://github.com/")
    if request.param == "mobile":
        browser.config.window_height = 640
        browser.config.window_width = 480
    if request.param == "desktop":
        browser.driver.maximize_window()
    yield request.param


@pytest.mark.parametrize("browser_setting", ["desktop"], indirect=True)
def test_github_desktop(browser_setting):
    browser.element('[href="/login"]').click()
    assert browser.element('h1').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_setting", ["mobile"], indirect=True)
def test_github_mobile(browser_setting):
    browser.element('[type="button"] .Button-label').click()
    browser.element('[href="/login"]').click()
    assert browser.element('h1').should(have.text('Sign in to GitHub'))
