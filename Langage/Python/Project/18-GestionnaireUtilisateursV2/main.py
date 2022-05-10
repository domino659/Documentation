import re, string
from tinydb import TinyDB, where, table
from pathlib import Path

class User:

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
    
    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"

    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name)) 

    def _checks(self):
        self._check_names()
        self._check_phone_number()

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("The first name and the last name can not be empty.")

        special_chatacters = string.punctuation + string.digits
        special_chatacters = special_chatacters.replace("-", "")
        for character in self.first_name + self.last_name:
            if character in special_chatacters:
                raise ValueError(f"Name is invalide {self.full_name}.")
    
    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Phone numbes {self.phone_number} is invalide.")

    def exists(self) -> bool:
        return bool(self.db_instance)

    def save(self, validate_data=False) -> int:
        if validate_data:
            self._checks()
        
        if self.exists():
            return -1
        else:
            return User.DB.insert(self.__dict__)
    
    def delete(self) -> list[int]:
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

def get_all_users():
    return [User(**user) for user in User.DB.all()]

# if __name__ == "__main__":
    # create_user = User("Tristan", "Bègue", "+33 4 98 81 62 24", "rue Isabelle Bonneau\n42223 Sainte Martine-les-Bains")
    # create_user.save(validate_data=True)
    # specific_user = User("Tristan", "Bègue")
    # print(specific_user.db_instance)
    # print(specific_user.exists())
    # print(specific_user.delete())

    # from faker import Faker
    # fake = Faker(locale="fr_FR")
    # for _ in range(10):
    #     user = User(first_name=fake.first_name(),
    #         last_name=fake.last_name(),
    #         phone_number=fake.phone_number(),
    #         address=fake.address())
    #     print(user.save(validate_data=True)) 
    #     # print(user)
    #     # print(repr(user))
    #     # print(user.__dict__)
    #     print("-" * 10)