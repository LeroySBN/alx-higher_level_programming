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
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictinaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON sting representation of list_objs to a file"""
        filename = str(cls.__name__) + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            list_dicts = [item.to_dictionary() for item in list_objs]
            file.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance withh all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(4, 2)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns the list of a jJSON string representation"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**kwargs) for kwargs in  list_dicts]
        except IOError:
            return []
