from autocomplete import *

def test_increment_last_letter():
    test_case_single_letter = "a"
    expected_single_letter_result = "b"
    assert increment_last_letter(test_case_single_letter) == expected_single_letter_result

    test_case_multiple_letters = "abcdefg"
    expected_multiple_letters_result = "abcdefh"
    assert increment_last_letter(test_case_multiple_letters) == expected_multiple_letters_result

    test_case_ending_with_z = "xyz"
    expected_ending_with_z_result = "xz"
    assert increment_last_letter(test_case_ending_with_z) == expected_ending_with_z_result

    test_case_z_only = "z"
    expected_z_only_result = ""
    assert increment_last_letter(test_case_z_only) == expected_z_only_result

test_increment_last_letter()
