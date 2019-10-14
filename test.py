from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import os

options = Options()
options.headless = True

with webdriver.Firefox(options=options) as browser:
    print(os.getcwd())
    browser.get(f'file://{os.getcwd()}/index.html')
    assert('Calculator' in browser.page_source)