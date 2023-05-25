from behave import *


@when('career: I click career link')
def step_impl(context):
    context.career_page.click_career_lnk()


@when('career: I search after "{city}"')
def step_impl(context, city):
    context.career_page.search_city(city)


@then('career: I search after "{store}"')
def step_impl(context, store):
    context.career_page.search_store(store)


@then('career: I click search job button')
def step_impl(context):
    context.career_page.click_search_job_button()





