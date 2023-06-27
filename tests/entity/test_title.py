from entity.title import Title

def test_title():
    assert Title("Hello", len("Hello")).title == "Hello"
    assert Title("Hello", len("Hello")).title != "hello"
    assert Title("Hello", len("Hello")).number_char == 5
    assert Title("Hello", len("Hello")).number_char != 6