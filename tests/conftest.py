import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', params=[(1280, 720), (1920, 1080), (2560, 1440), (3840, 2160)],
                ids=['HD', 'FHD', 'QHD', 'UHD'])
def browser_management_desktop_version(request):
    width, height = request.param

    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(375, 667), (414, 896), (390, 844), (430, 932)],
                ids=['iPhone_SE', 'iPhone_XR', 'iPhone_12_Pro', 'iPhone_14_Pro_Max'])
def browser_management_mobile_version(request):
    width, height = request.param

    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1920, 1080), (2560, 1440), (390, 844), (430, 932)],
                ids=['FHD', 'QHD', 'iPhone_12_Pro', 'iPhone_14_Pro_Max'])
def browser_management(request):
    width, height = request.param

    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    if width > 600:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
