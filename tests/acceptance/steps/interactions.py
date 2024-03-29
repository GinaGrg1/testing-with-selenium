from behave import *

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@When('I click on the "(.*)" link')
def step_impl(context, link_text):
    # Using regex to grab the word in double-quotes and assign it to variable link_id
    page = BasePage(context.driver)
    links = page.navigation  # returns a list
    
    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()
