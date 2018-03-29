def increment_last_letter(str):
    if not str:
        return ""

    chars = list(str)
    index = len(chars) - 1

    last_letter = chars[index]
    if (last_letter == "z"):
        return increment_last_letter("".join(chars[:-1]))

    chars[index] = chr(ord(last_letter) + 1)
    return  "".join(chars)

def find(query, to_find, length):
    found = query(to_find)

    if (len(found) == 5):
        last = found[4]
        length = length + 1
        chars = list(last[:length])
        next_to_find =
    else:
        next_to_find = increment_last_letter(to_find)

    while(next_to_find):
        # print next_to_find
        found += find(query, next_to_find, length)
        next_to_find = increment_last_letter(next_to_find)

    return found

def extract(query):
    results = []
    for i in range(ord("a"), ord("z")):
        results += find(query, chr(i), 1)
    print "ME: ", results
    return results

def main():
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    print "OK: ", database
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

    # database = ["abracadara", "bob", "mallory"]
    # print "OK: ", database
    # query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    # assert extract(query) == database
    #
    # database = ["a"]
    # print "OK: ", database
    # query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    # assert extract(query) == database
    #
    # database = []
    # print "OK: ", database
    # query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    # assert extract(query) == database
    #
    # database = []
    # with open("/Users/jay/Programming/OpenAI-Scholar-Application-2018/test_usernames.txt") as f:
    #     database = f.readlines()
    #     database = [x.strip() for x in database]
    # print "OK: ", database
    # query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    # assert extract(query) == database


if __name__ == "__main__":
    main()
