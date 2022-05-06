import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage

from main import User

@pytest.fixture
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)

@pytest.fixture
def user(setup_db):
    user = User(first_name="John",
                last_name="Doe",
                address="1 rue du chemin, 75000 Paris",
                phone_number="0123456789")
    user.save()
    return user
 
def test_first_name(user):
    assert user.first_name == "John"

def test_last_name(user):
    assert user.last_name == "Doe"

def test_address(user):
    assert user.address == "1 rue du chemin, 75000 Paris"

def test_phone_number(user):
    assert user.phone_number == "0123456789"

def test_full_name(user):
    assert user.full_name == "John Doe"

def test_exists(user):
    assert user.exists() is True

def test_not_exists(setup_db):
    user = User(first_name="John",
                last_name="Doe",
                address="1 rue du chemin, 75000 Paris",
                phone_number="0123456789")
    assert user.exists() is False

def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "John"
    assert user.db_instance["last_name"] == "Doe"
    assert user.db_instance["address"] == "1 rue du chemin, 75000 Paris"
    assert user.db_instance["phone_number"] == "0123456789"

def test_not_db_instance(setup_db):
    user = User(first_name="John",
                last_name="Doe",
                address="1 rue du chemin, 75000 Paris",
                phone_number="0123456789")
    assert user.db_instance is None

def test__check_phone_number(setup_db): 
    user_good = User(first_name="John",
                last_name="Doe",
                address="1 rue du chemin, 75000 Paris",
                phone_number="0123456789")
    user_bad = User(first_name="John",
                last_name="Doe",
                address="1 rue du chemin, 75000 Paris",
                phone_number="abcd")
    
    with pytest.raises(ValueError)as err:
        user_bad._check_phone_number()

    assert "invalide" in str(err.value)
    
    user_good.save(validate_data=True)
    assert user_good.exists() is True

def test__check_name_names_empty(setup_db):
    user_bad = User(first_name="",
                last_name="",
                address="1 rue du chemin, 75000 Paris",
                phone_number="0123456789 ")

    with pytest.raises(ValueError)as err:
        user_bad._check_names()

    assert "The first name and the last name can not be empty" in str(err.value)
       
def test__check_name_names_invalid_characters(setup_db):
    user_bad = User(first_name="John%&*",
                last_name="Doe%&*", 
                address="1 rue du chemin, 75000 Paris",
                phone_number="0123456789 ")

    with pytest.raises(ValueError)as err:
        user_bad._check_names()

    assert "Name is invalide" in str(err.value)

def test_save(setup_db):
    user_test = User(first_name="John%&*",
            last_name="Doe%&*", 
            address="1 rue du chemin, 75000 Paris",
            phone_number="0123456789 ")
    user_test_dub = User(first_name="John%&*",
        last_name="Doe%&*", 
        address="1 rue du chemin, 75000 Paris",
        phone_number="0123456789 ")
    first = user_test.save()
    second = user_test_dub.save()

    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1
     
def test_delete(setup_db):
    user_test = User(first_name="John%&*",
        last_name="Doe%&*", 
        address="1 rue du chemin, 75000 Paris",
        phone_number="0123456789 ")
    user_test.save()
    first = user_test.delete()
    second = user_test.delete()

    assert len(first) > 0
    assert isinstance(first, list)
    assert len(second) == 0
    assert isinstance(second, list)