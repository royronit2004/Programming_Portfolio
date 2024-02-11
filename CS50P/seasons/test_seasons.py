from seasons import check_bd

def main():
    test_check_bd()

def test_check_bd():
    assert check_bd("1995-07-08") == ("1995", "07", "08")
    assert check_bd("1995-7-8") == None
    assert check_bd("July 8, 1995") == None

if __name__ == "__main__":
    main()