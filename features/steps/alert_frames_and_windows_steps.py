from behave import given, when, then
from selenium import webdriver


@given('launch chrome')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('open website')
def step_impl(context):
    context.driver.get("https://demoqa.com/")


@when('verify logo present')
def step_impl(context):
    status = context.driver.find_element_by_xpath("//*[@id=\"app\"]/header/a/img").is_displayed()
    assert status is True


@then('close browser')
def step_impl(context):
    context.driver.close()
