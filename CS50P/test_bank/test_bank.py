from bank import value

def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()

def test_return_zero():
    assert value('hello') == 0
    assert value('hello g') == 0
    assert value('Hello G') == 0


def test_return_twenty():
    assert value('hi') == 20
    assert value('hey') == 20
    assert value('hell') == 20


def test_return_hundred():
    assert value('good morning') == 100
    assert value('love you') == 100


if __name__ == "__main__":
    main()

