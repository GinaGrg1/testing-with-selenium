from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    # title_tag = context.browser.find_element(*HomePageLocators.TITLE)
    # assert title_tag.is_displayed()
    page = BasePage(context.driver)
    assert page.title.is_displayed()

# We can use step instead of then, as there is an And statement.
@step('The title tag has content "(.*)"')
def step_impl(context, content):
    # title_tag = context.browser.find_element(*HomePageLocators.TITLE)
    # assert title_tag.text == content
    page = BasePage(context.driver)
    assert page.title.text == content


@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()
