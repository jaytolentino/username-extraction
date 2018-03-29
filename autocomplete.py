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
    if (len(found) == 5):
        next_to_find = found[len(found) - 1]
        while (next_to_find):
            if (found[-1] == next_to_find):
                found += find(query, next_to_find)[1:]
            else:
                found += find(query, next_to_find)
            next_to_find = increment_last_letter(next_to_find)
    return found

def extract(query):
    results = []
    for i in range(ord("a"), ord("z")):
        results += find(query, chr(i))
    print "ME: ", results
    return results

def main():
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    print "OK: ", database
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

if __name__ == "__main__":
    main()
