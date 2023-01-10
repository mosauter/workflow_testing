"""Basic module to facilitate something to test with workflows."""


def hello_world() -> str:
    """
    Returns literally only 'Hello World!' until someone forgot to update
    the comment.
    """
    return "Hello World!"


if __name__ == "__main__":
    print(hello_world())
