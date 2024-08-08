"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be

only_desktop_version = pytest.mark.parametrize("browser_management",
                                               [(1920, 1080), (2560, 1440)],
                                               indirect=True,
                                               ids=['FHD', 'QHD'])
only_mobile_version = pytest.mark.parametrize("browser_management",
                                              [(375, 667), (430, 932)],
                                              indirect=True,
                                              ids=['iPhone_SE', 'iPhone_14_Pro_Max'])


@only_desktop_version
def test_github_desktop(browser_management):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()

    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)


@only_mobile_version
def test_github_mobile(browser_management):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()

    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)
