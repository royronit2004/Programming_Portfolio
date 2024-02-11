from project import correct_arg, select_universe, select_grade
import pytest



def test_correct_arg():
   with pytest.raises(SystemExit):
       correct_arg


def test_select_universe():
    assert select_universe("Iron-Man") == "Marvel Universe"
    assert select_universe("Spider-Man") == "Marvel Universe"
    assert select_universe("Doctor Doom") == "Marvel Universe"
    assert select_universe("Batman") == "DC Universe"
    assert select_universe("Superman") == "DC Universe"
    assert select_universe("Lex Luthor") == "DC Universe"


def test_select_grade():
    assert select_grade(2006) == "Grade 12"
    assert select_grade(2007) == "Grade 11"
    assert select_grade(2008) == "Grade 10"

