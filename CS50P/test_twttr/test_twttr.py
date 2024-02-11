from twttr import shorten

def main():
    test_letter()
    test_num()
    test_punc()

def test_letter():
    assert shorten('twitter') == 'twttr'
    assert shorten('Twitter') == 'Twttr'
    assert shorten('TWITTER') == 'TWTTR'

def test_num():
    assert shorten('1234') == '1234'

def test_punc():
    assert('!') == '!'
    assert('?') == '?'
    assert(',') == ','
    assert('.') == '.'


if __name__ == "__main__":
    main()