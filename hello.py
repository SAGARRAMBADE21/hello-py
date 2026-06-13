__version__ = "1.2.0"


def greet(name="World"):
    return f"Hello, {name}!"


def farewell(name="World"):
    return f"Goodbye, {name}!"


def ask(name="World"):
    return f"How are you, {name}?"


if __name__ == "__main__":
    print(greet())
    print(ask())
    print(farewell())
