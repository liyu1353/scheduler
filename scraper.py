from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


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
        EC.presence_of_element_located((By.CLASS_NAME, 'NoticeListView_notice_item_link__uBuv-')))

notices = driver.find_elements(By.CLASS_NAME, 'NoticeListView_notice_item_link__uBuv-')

for notice in notices:
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'NoticeListView_notice_item_link__uBuv-')))
    link = notice.get_attribute("href")
    current = driver.current_window_handle
    script = "window.open('" + link + "')"
    driver.execute_script(script)
    new_tab = [tab for tab in driver.window_handles if tab != current][0]
    driver.switch_to.window(new_tab)
    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'p')))
    text = driver.find_element(By.CLASS_NAME, 'p').text
    print(text)
    driver.close()
    driver.switch_to.window(current)



def label(title, contents):
    if "Release Announcement" in title:
        #find date of release
        a = contents.split(" ")
        mo = a.get(a.index("2023") - 2)
        if mo == "January":
            month = 1
        elif mo == "February":
            month = 2
        elif mo == "March":
            month = 3
        elif mo == "April":
            month = 4
        elif mo == "May":
            month = 5
        # do the rest of this crap later
        day = int(a.get(a.index("2023") - 2)[0, a.get(a.index("2023")-2) - 1])
        return "Release"


while (True):
    pass
