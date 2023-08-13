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
# FIXME: Open a tab for each exercise, or check if you can enter each exercise details page