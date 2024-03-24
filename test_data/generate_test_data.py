import random

from faker import Faker

fake = Faker()


def email():
    return fake.email(domain="autotests.com")


def random_string(max_nb_chars=10) -> str:
    return fake.text(max_nb_chars)


def random_integer(min_value=99, max_value=999999):
    return fake.random_int(min_value, max_value)


def special_symbols(ln: int = 32):
    return "".join(random.choice('@!@#$%^&*()_+-={}[]|`~:";,.?/') for _ in range(ln))
