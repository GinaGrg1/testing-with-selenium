from behave import *

use_step_matcher('re')


@When('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    # Using regex to grab the word in double-quotes and assign it to variable link_id
    link = context.browser.find_element_by_id(link_id)
    link.click()
