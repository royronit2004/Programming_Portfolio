from um import count

def main():
    test_ul_case()
    test_wordum()
    test_space()


def test_ul_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_wordum():
    assert count("yumm1") == 0

def test_space():
    assert count("Hello um world") == 1
    assert count("um?") == 1


if __name__ == "__main__":
    main()