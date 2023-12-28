from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def login():
    # Login
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="confirm modal"]'))).click()

    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.NAME, 'userEmail'))).send_keys("daniel.li7691@gmail.com")

    email_submit = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="sc-763a3587-1 gOzeoU"]')))

    driver.execute_script("arguments[0].style.zIndex = '9999';", email_submit)
    email_submit.click()

    password = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.NAME, 'password'))).send_keys("Daniel2005!")

    pass_submit = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="sc-763a3587-1 gOzeoU"]')))
    driver.execute_script("arguments[0].style.zIndex = '9999';", pass_submit)
    pass_submit.click()


def getinfo(url):
    body = driver.find_element(By.CLASS_NAME, 'NoticeModalView_detail__t4JWo')
    text = body.text
    print(text.split(0, 15))


driver.get("https://weverse.io/enhypen/notice")

login()

# the events are all class = NoticeListView_notice_item__1-Ud8
WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'NoticeListView_notice_item__1-Ud8')))

notices = driver.find_elements(By.CLASS_NAME, 'NoticeListView_notice_item_link__uBuv-')

for notice in notices:
    randomThing = driver.find_elements(By.CLASS_NAME, 'HeaderView_action__QDUUD')
    driver.execute_script("arguments[0].style.zIndex = '9999';", notice)
    driver.execute_script("arguments[0].style.zIndex = '0';", randomThing)
    driver.execute_script("arguments[0].scrollIntoView(true);", notice)
    notice.click()


while (True):
    pass
