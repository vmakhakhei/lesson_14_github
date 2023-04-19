"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import time
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


def test_github_desktop(browser_setting):
    if browser_setting == "desktop":
        browser.element('[href="/login"]').click()
        assert browser.element('h1').should(have.text('Sign in to GitHub'))
    if browser_setting == "mobile":
        pytest.skip("Test only for desktop screen size")


def test_github_mobile(browser_setting):
    if browser_setting == "desktop":
        pytest.skip("Test only for mobile screen size")
    if browser_setting == "mobile":
        browser.element('[type="button"] .Button-label').click()
        browser.element('[href="/login"]').click()
        assert browser.element('h1').should(have.text('Sign in to GitHub'))
