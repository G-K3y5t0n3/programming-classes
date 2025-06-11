from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Michael-Jacob", "Quizon") == "Quizon; Michael-Jacob"
    assert make_full_name("Michael", "Quizon") == "Quizon; Michael"
    assert make_full_name("M", "Q") == "Q; M"

def test_extract_family_name():
    assert extract_family_name("Quizon; Michel-Jacob") == "Quizon"
    assert extract_family_name("Doe; Jane") == "Doe"
    assert extract_family_name("Alipoyo; Sherclemn") == "Alipoyo"

def test_extract_given_name():
    assert extract_given_name("Quizon; Michael-Jacob") == "Michael-Jacob"
    assert extract_given_name("Quizon; Michael") == "Michael"
    assert extract_given_name("Doe; Jane") == "Jane"

pytest.main(["-v", "--tb=line", "-rN", __file__])