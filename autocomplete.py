def increment_last_letter(str):
    if not str or len(str) == 1:
        return ""

    chars = list(str)
    index = len(chars) - 1

    last_letter = chars[index]
    if (last_letter == 'z'):
        return increment_last_letter("".join(chars[:-1]))

    chars[index] = chr(ord(last_letter) + 1)
    return  "".join(chars)

def find(query, to_find):
    found = query(to_find)
    if (len(found) > 1):
        next_to_find = found[-1]
        while (next_to_find):
            if (found[-1] == next_to_find):
                found += find(query, next_to_find)[1:]
            else:
                found += find(query, next_to_find)
            next_to_find = increment_last_letter(next_to_find)
    return found

def extract(query):
    all_usernames = []
    for i in range(ord("a"), ord("z")):
        all_usernames += find(query, chr(i))
    print "ME: ", all_usernames
    return all_usernames

def main():
    # database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    # print "OK: ", database
    # query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    # assert extract(query) == database

    database = []
    with open("/Users/jay/Programming/OpenAI-Scholar-Application-2018/test_usernames.txt") as f:
        database = f.readlines()
        database = [x.strip() for x in database]
    print "OK: ", database
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:8]
    assert extract(query) == database

if __name__ == "__main__":
    main()
