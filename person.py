import json
from datetime import datetime
import pandas as pd

class Person:
    
    @staticmethod
    def load_person_data():
        """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names
    
    @staticmethod
    def find_person_data_by_name(suchstring):
        """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        #print(suchstring)
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            print(eintrag)
            if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
                print()

                return eintrag
        else:
            return {}
        
    @staticmethod
    def find_person_data_by_id(person_id):
        """A Function that takes an ID and returns the person as a dictionary"""
        person_data = Person.load_person_data()
        for eintrag in person_data:
            if eintrag["id"] == person_id:
                return eintrag
        return {}
        
    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]
        

    def calc_age(self):
        today = datetime.now()
        age = today.year - self.date_of_birth
        self.age = age
        return age
    

    def calc_max_heart_rate(self):
        max_hr_bpm =  223 - 0.9 * self.calc_age()
        return int(max_hr_bpm)

    @classmethod
    def load_by_id(cls, person_id):
        person_dict = cls.find_person_data_by_id(person_id)
        if person_dict:
            return cls(person_dict)
        else:
            return None
        
        

if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    print(Person.find_person_data_by_name("Heyer, Yannic"))
    selected_person = Person(Person.find_person_data_by_name("Heyer, Yannic"))
    print(selected_person.calc_max_heart_rate())
    

    try:
        person_id_input = int(input("Bitte geben Sie die ID der Person ein: "))
        person_by_id = Person.load_by_id(person_id_input)
        if person_by_id:
            print(f"Person loaded by ID: {person_by_id.firstname} {person_by_id.lastname}")
            print(f"Das Alter beträgt:",person_by_id.calc_age())
            print(f"Max Herzfrequenz: {person_by_id.calc_max_heart_rate()} bpm")
        else:
            print("Keine Person mit der gegebenen ID gefunden.")
    except ValueError:
        print("Bitte geben Sie eine gültige numerische ID ein.")