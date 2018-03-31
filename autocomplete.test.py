from autocomplete import *

def test_increment():
    test_case_single_letter_no_add = "a"
    expected_single_letter_no_add_result = ""
    assert increment(test_case_single_letter_no_add, False) == expected_single_letter_no_add_result
    print "Test increment(): single letter with no letter add - PASSED"

    test_case_single_letter_with_add = "a"
    expected_single_letter_with_add_result = "aa"
    assert increment(test_case_single_letter_with_add, True) == expected_single_letter_with_add_result
    print "Test increment(): single letter with letter add - PASSED"

    test_case_multiple_letters = "abcdefg"
    expected_multiple_letters_result = "abcdefh"
    assert increment(test_case_multiple_letters, False) == expected_multiple_letters_result
    print "Test increment(): multiple letters - PASSED"

    test_case_ending_with_z = "xyz"
    expected_ending_with_z_result = "xz"
    assert increment(test_case_ending_with_z, False) == expected_ending_with_z_result
    print "Test increment(): word ending in z - PASSED"

    test_case_z_only = "z"
    expected_z_only_result = ""
    assert increment(test_case_z_only, False) == expected_z_only_result
    print "Test increment(): z only - PASSED"

    test_case_multiple_z = "azzz"
    expected_multiple_z_result = "b"
    assert increment(test_case_z_only, False) == expected_z_only_result
    print "Test increment(): multiple z's - PASSED"

def test_extract():
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
    print "Test extract(): provided database - PASSED"

    database = ["a"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
    print "Test extract(): single word database - PASSED"

    database = []
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
    print "Test extract(): empty database - PASSED"

    print "Began processing large database..."
    database = []
    with open("/Users/jay/Programming/OpenAI-Scholar-Application-2018/test_usernames.txt") as f:
        database = f.readlines()
        database = [x.strip() for x in database]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
    print "Test extract(): large database - PASSED"

test_increment()
test_extract()
