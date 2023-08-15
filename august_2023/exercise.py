from typing import List


class Exercise:
    def __init__(self, name: str, primary_muscle: str, start_positioning_image_url: str, end_positioning_image_url: str,
                 instructions: str):
        self.name = name
        self.primary_muscle = primary_muscle
        self.start_positioning_image_url = start_positioning_image_url
        self.end_positioning_image_url = end_positioning_image_url
        self.instructions = instructions

    def __iter__(self):
        return iter([self.name, self.primary_muscle, self.start_positioning_image_url, self.end_positioning_image_url,
                     self.instructions])
