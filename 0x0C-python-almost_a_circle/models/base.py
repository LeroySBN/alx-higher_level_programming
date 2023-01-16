"""Module base"""
import json


class Base:
    """creates a base instance"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes instance

        Args:
            id (int): unidue identifier
        """
        if id is not None:
            self.id = id
        __nb_objects += 1
        self.id = __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictinaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
