from typing import List
import requests
from bs4 import BeautifulSoup
from exercise import Exercise


def get_exercise_details_urls() -> List[str]:
    # exercise_details_urls = []
    # with open('exercise_details_urls.txt') as exercise_details_urls_file:
    #     for url in exercise_details_urls_file:
    #         cleaned_url = url.strip()
    #         exercise_details_urls.append(cleaned_url)
    #
    # return exercise_details_urls

    # FIXME: Delete and uncomment code above.
    return ["https://www.bodybuilding.com/exercises/palms-down-wrist-curl-over-a-bench"]


# FIXME: Extract wanted data
def parse_exercise(exercise_details_url: str) -> Exercise:
    exercise_details_request = requests.get(exercise_details_url)
    exercise_details_parser = BeautifulSoup(exercise_details_request.content, "html.parser")

    title_element = exercise_details_parser.find(name="h1")
    title = title_element.text.strip()

    # FIXME: Replace href filter because it is too specific. Can a wildcard be used?
    primary_muscle_element = exercise_details_parser.find(name="a", href="/exercises/muscle/forearms")
    primary_muscle = primary_muscle_element.text.strip()

    image_elements = exercise_details_parser.find_all(name="img", class_="ExImg ExDetail-img js-ex-enlarge")
    image_srcs = []
    for image_element in image_elements:
        src = image_element['src'].strip()
        image_srcs.append(src)

    return Exercise(name=title, primary_muscle=primary_muscle, image_urls=image_srcs)


def main():
    exercise_details_urls = get_exercise_details_urls()
    exercises = []
    for exercise_details_url in exercise_details_urls:
        exercise = parse_exercise(exercise_details_url=exercise_details_url)
        exercises.append(exercise)

    # FIXME: Save data in a csv file for importing into Notion


main()
