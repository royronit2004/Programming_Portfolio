from plates import is_valid


def main():
    test_minmax()
    two_letter_start()
    test_num_mid()
    num_zero()
    test_punc()


def test_minmax():
    assert is_valid('AA') == True
    assert is_valid('AABBCC') == True
    assert is_valid('A') == False
    assert is_valid('AABBCCD') == False

def two_letter_start():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False

def test_num_mid():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False

def num_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_punc():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI3 14') == False

if __name__ == "__main__":
    main()
