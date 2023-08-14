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

# FIXME: Iterate through urls

# FIXME: Extract wanted data

# FIXME: Save data in a csv file for importing into Notion