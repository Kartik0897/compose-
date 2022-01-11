from behave import *
from selenium import webdriver


@given('Launch chrome browser')
  def launchBrowser(context):
   context.driver = webdriver.Chrome(executable_path="Path of c drive")

@when('Open gmail')
  def openGmail(context):
   context.driver.get("https:\\www.gmail.com")

@when('Login gmail')
 def loginGmail(context):
  context.driver.find_element_by_css_selector("input[type='email']").send_keys("xyz@gmail.com")
  context.driver.find_element_by_css_selector("input[type='password']").send_keys("xxxxxx")

@then('Verify compose button ')
  def verifyCompose(context):
    compose = context.driver.find_element_by_xpath("//*[@id=':3i']/div/div").click()
    assert compose is True
    context.driver.find_element_by_css_selector("*[id=':b4']").send_keys("Incubyte@gmail.com")
    context.driver.find_element_by_css_selector("*[id=':86']").send_keys("Incubyte")
    context.driver.find_element_by_css_selector("*[role='textbox']").send_keys("Automation QA test for Incubyte")
    context.driver.find_element_by_xpath("//*[@id=':7w'']").click()

@then('close  chrome browser')
  def closeBrowser(context):
    context.driver.close()