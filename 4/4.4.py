class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f"Sending message '{message}' to user '{user.name}'")

    def post(self, message):
        print(f"Posting message '{message}' on my wall")

    def info(self):
        return ""

    def describe(self):
        print(f"User: {self.name}")
        print(self.info())


class Person(User):
    def __init__(self, name, birthdate):
        super().__init__(name)
        self.birthdate = birthdate

    def info(self):
        return f"Birthdate: {self.birthdate}"

    def subscribe(self, user):
        print(f"Subscribing to user '{user.name}'")


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Description: {self.description}"