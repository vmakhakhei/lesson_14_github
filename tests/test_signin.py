from selene import browser


def open_github():
    browser.open("https://github.com/")

def sign_in():
    browser.element('[href="/login"]').click

def menu():
    browser.element('[type="button"] .Button-label').click()


def test_mobile_git(browser_setup):
    open_github()
    menu()
    sign_in()


