from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import os

options = Options()
options.headless = True

with webdriver.Firefox(options=options) as browser:
    browser.get(f'file://{os.getcwd()}/dist/index.html')
    assert('Calculator' in browser.page_source)

    expression = browser.find_element_by_name('expression')
    expression.clear()
    expression.send_keys('273 + 571')
    assert('844' in browser.page_source)

    expression = browser.find_element_by_name('expression')
    expression.clear()
    expression.send_keys('2 * standard_state_pressure')
    assert('200000.0' in browser.page_source)