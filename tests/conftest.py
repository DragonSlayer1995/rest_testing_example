import random
import string
import pytest

from core.users_client import UsersClient
from core.users_data import UsersData


@pytest.fixture(scope="session")
def user_data():
    _id = random.randint(100, 1000)
    user_name = ''.join(map(str, random.sample(string.ascii_lowercase, 5)))
    password = ''.join(map(str, random.sample(range(0, 9), 5)))
    return UsersData(_id, user_name, password)

@pytest.fixture(scope="session")
def users_client():
    return UsersClient('https://fakerestapi.azurewebsites.net/')