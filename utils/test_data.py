from faker import Faker


fake = Faker()


def generate_user():

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "postal_code": fake.postcode()
    }


def generate_product_quantity():

    return fake.random_int(
        min=1,
        max=10
    )