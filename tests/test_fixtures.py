"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser, be


def test_github_desktop(browser_management_desktop_version):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()

    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)


def test_github_mobile(browser_management_mobile_version):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()

    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)
