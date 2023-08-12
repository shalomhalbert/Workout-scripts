import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.bodybuilding.com/exercises/finder?equipment=barbell%2Cbody-only%2Cdumbbell%2Cnone%2Cother"

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get(url=url)
print("First url: " + chrome_browser.current_url)

chrome_browser.close()

# FIXME: Tap "Load more" until the list is fully displayed
# FIXME: From each exercise's details page, collect the following:
#  Details page's url
#  Exercise's name
#  Workout type
#  Main muscle worked
#  Equipment used
#  Difficulty level
#  All images Instructions

# Option #1
# exercise_finder_list_response = requests.get(url=url)
# exercise_finder_list_beautiful_soup = BeautifulSoup(markup=exercise_finder_list_response.text, features="html.parser")
# exercise_finder_list_beautiful_soup.find(name="XXX")

# exercise_web_element = chrome_browser.find_element(by=By.LINK_TEXT, value="Rickshaw Carry")
# exercise_web_element.click()
# time.sleep(2)
