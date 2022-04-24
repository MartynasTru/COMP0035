import user

# testing initialization of the class


def test_success():
    check = user.User("Martynas", "Trusilo",
                      "martynastrusilo@gmail.com", "minivn")
    assert check.first_name == "Martynas"
    assert check.last_name == "Trusilo"
    assert check.email_address == "martynastrusilo@gmail.com"
    assert check.username == "minivn"

# Checking if password is correct
# It is supposed to fail as correct password is "mypassword" and we
# have inputted "mypasswo4rd"


def test_fail():
    model = user.User("Martynas", "Trusilo",
                      "martynastrusilo@gmail.com", "minivn")
    assert model._password_hash == "mypasswo4rd"
