import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win" # Copilot fixed assert statement to match return type

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High" # Copilot fixed assert statement to match return type


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low" # Copilot fixed assert statement to match return type


def test_get_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_get_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42
    assert err is None

def test_parse_guess_float():
    ok, value, err = parse_guess("42.0")
    assert ok == True
    assert value == 42
    assert err is None

def test_parse_guess_invalid():
    ok, value, err = parse_guess("abc")
    assert ok == False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok == False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok == False
    assert value is None
    assert err == "Enter a guess."

def test_update_score_win():
    new_score = update_score(100, "Win", 1)
    assert new_score == 100 + (100 - 10 * (1 + 1))  # 100 + 80 = 180

def test_update_score_too_high():
    new_score = update_score(100, "Too High", 1)
    assert new_score == 100 - 5

def test_update_score_too_low():
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 100 - 5


if __name__ == "__main__":
    # Run all test functions
    test_functions = [
        test_winning_guess,
        test_guess_too_high,
        test_guess_too_low,
        test_get_range_easy,
        test_get_range_normal,
        test_get_range_hard,
        test_parse_guess_valid,
        test_parse_guess_float,
        test_parse_guess_invalid,
        test_parse_guess_none,
        test_parse_guess_empty,
        test_update_score_win,
        test_update_score_too_high,
        test_update_score_too_low,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")

