from behave import *
from selenium import webdriver


use_step_matcher('re')

options = webdriver.ChromeOptions()

options.add_argument("--headless")
options.add_argument("--no-sandbox")
#options.add_argument("--disable-extensions")
#options.add_argument("--disable-gpu")


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
    context.browser.get('http://127.0.0.1:5000')


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
    context.browser.get('http://127.0.0.1:5000/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url
