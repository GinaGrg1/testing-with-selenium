from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')
options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
    page = HomePage(context.driver)
    context.driver.get(page.url)
    # context.driver.get('http://127.0.0.1:5000')


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
