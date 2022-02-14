import time

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://profil.wp.pl/login/login.html')
time.sleep(2)

# 1. znalezc miejsce gdzie wprowadza sie nazwe email
login_field = browser.find_element_by_id('login')
# 2. wpisac w miejsce email
login_field.send_keys('XXX')

password_field = browser.find_element_by_id('password')
password_field.send_keys('XXX')

loguj_button = browser.find_element_by_xpath("//button[@type='submit']")
loguj_button.click()
time.sleep(2)

napisz_button = browser.find_element_by_xpath(
    "//button[contains(text(),'napisz')]")
napisz_button.click()
time.sleep(2)
recepient_input = browser.find_element_by_xpath(
    "//input[@value='']"
)
recepient_input.send_keys('**tu idzie email ***')

subject_input = browser.find_element_by_xpath(
    "//input[@name='subject']")
subject_input.send_keys('XXX')

action = webdriver.ActionChains(browser)

email_content = browser.find_element_by_xpath(
    "//div[@class='DraftEditor-editorContainer']/div"
)
email_content.click()
action.move_to_element(email_content).send_keys('''
XXX
 ''').perform()

send_button = browser.find_element_by_xpath(
    "//button[@type='submit']")
send_button.click()

time.sleep(2)
browser.close()
