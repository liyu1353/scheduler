from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import pygsheets
import pandas as pd

def sheet():
    gc = pygsheets.authorize(service_file='/Users/daniel/PycharmProjects/scheduler/scheduler-409417-e731d6b458a7.json')
    df = pd.DataFrame()
    sh = gc.open('Scheduler Database')
    current = sh[0]


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


def label(title, contents):
    if "Release Announcement" in title:
        return "Release"

#for finding dates when it's most likely to appear first
def finddate(text):
    words = text.split(" ")
    year = "2023"
    try:
        a = words.index("2023")
    except:
        year = "2024"
        try:
            a = words.index("2024")
        except:
            return None
    while not words[words.index(year) - 1][0].isnumeric():
        words = words[words.index(year) + 1]
        try:
            a = words.index(year)
        except:
            return None
    a = words.index(year)
    return words[a - 2] + " " + words[a - 1] + " " + words[a]

def finddateaddconcert(text):
    #for later to do, additional concert will usually list the original dates first so
    #we have to start from the additional concert index

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
    #print(text)
    if not finddate(text) == None:
        print(finddate(text))
    driver.close()
    driver.switch_to.window(current)

while (True):
    pass
