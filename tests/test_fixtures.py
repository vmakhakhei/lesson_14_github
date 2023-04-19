import time

import pytest
from selene import browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture
def browser_mobile():
    browser.config.window_height = 640
    browser.config.window_width = 480


@pytest.fixture
def browser_desktop():
    browser.config.window_height = 1920
    browser.config.window_width = 1080


@pytest.mark.desktop
def test_github_desktop(browser_desktop):
    browser.open("https://github.com/")
    browser.element('[href="/login"]').click()
    time.sleep(5)
    pass


@pytest.mark.mobile
def test_github_mobile(browser_mobile):
    browser.open("https://github.com/")
    browser.element('[type="button"] .Button-label').click()
    browser.element('[href="/login"]').click()
    time.sleep(5)
    pass
