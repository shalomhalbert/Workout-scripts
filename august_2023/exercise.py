from typing import List


class Exercise:
    def __init__(self, name: str, primary_muscle: str, image_urls: List[str], instructions: List[str]):
        self.name = name
        self.primary_muscle = primary_muscle
        self.image_urls = image_urls
        self.instructions = instructions
