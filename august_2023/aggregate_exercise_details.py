from typing import List
import requests
from bs4 import BeautifulSoup
from exercise import Exercise


def get_exercise_details_urls() -> List[str]:
    exercise_details_urls = []
    with open('exercise_details_urls.txt') as exercise_details_urls_file:
        for url in exercise_details_urls_file:
            cleaned_url = url.strip()
            exercise_details_urls.append(cleaned_url)

    return exercise_details_urls


def extract_exercise_name(exercise_details_parser: BeautifulSoup) -> str:
    title_element = exercise_details_parser.find(name="h1")
    return title_element.text.strip()


def extract_primary_muscle(exercise_details_parser: BeautifulSoup) -> str:
    exercise_characteristics_list_element = exercise_details_parser.find(name="ul", class_="bb-list--plain")
    exercise_characteristics_list_item_elements = exercise_characteristics_list_element.find_all(name="li")

    for characteristic_list_item in exercise_characteristics_list_item_elements:
        characteristic_list_item_text = characteristic_list_item.text.strip()
        if "Main Muscle Worked:" in characteristic_list_item_text:
            return characteristic_list_item.contents[1].text.strip()

    return "Unknown"


def extract_image_urls(exercise_details_parser: BeautifulSoup) -> List[str]:
    image_elements = exercise_details_parser.find_all(name="img", class_="ExImg ExDetail-img js-ex-enlarge")
    image_srcs = []

    for image_element in image_elements:
        src = image_element['src'].strip()
        image_srcs.append(src)

    return image_srcs


def extract_instructions(exercise_details_parser: BeautifulSoup) -> List[str]:
    instructions_section_element = exercise_details_parser.find(name="section",
                                                                class_="ExDetail-section ExDetail-guide")
    instructions_list_element = instructions_section_element.find(name="ol")
    instructions_elements = instructions_list_element.find_all("li")

    instructions = []
    for instruction_element in instructions_elements:
        cleaned_instruction = instruction_element.text.strip()
        instructions.append(cleaned_instruction)

    return instructions


def parse_exercise(exercise_details_url: str) -> Exercise:
    exercise_details_request = requests.get(exercise_details_url)
    exercise_details_parser = BeautifulSoup(exercise_details_request.content, "html.parser")

    name = extract_exercise_name(exercise_details_parser=exercise_details_parser)
    primary_muscle = extract_primary_muscle(exercise_details_parser=exercise_details_parser)
    image_urls = extract_image_urls(exercise_details_parser=exercise_details_parser)
    instructions = extract_instructions(exercise_details_parser=exercise_details_parser)

    return Exercise(name=name, primary_muscle=primary_muscle, image_urls=image_urls, instructions=instructions)


def main():
    exercise_details_urls = get_exercise_details_urls()
    exercises = []
    for exercise_details_url in exercise_details_urls:
        exercise = parse_exercise(exercise_details_url=exercise_details_url)
        exercises.append(exercise)

    # FIXME: Save data in a csv file for importing into Notion


main()
