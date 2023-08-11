import requests

url = "https://www.bodybuilding.com/exercises/finder?equipment=barbell%2Cbody-only%2Cdumbbell%2Cnone%2Cother"

response = requests.get(url)
print(response.status_code)
print(response.text)

# FIXME: Tap "Load more" until the list is fully displayed
# FIXME: From each exercise's details page, collect the following:
#  Details page's url
#  Exercise's name
#  Workout type
#  Main muscle worked
#  Equipment used
#  Difficulty level
#  All images Instructions
