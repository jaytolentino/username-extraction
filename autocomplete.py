def increment(str, add_letter):
    if not str or not add_letter and len(str) == 1:
        return ''
    chars = list(str)
    if add_letter and len(str) == 1:
        chars.append('a')
        return ''.join(chars)
    if (chars[-1] == 'z'):
        while len(chars) > 0 and chars[-1] == 'z':
            del chars[-1]
        if len(chars) <= 1:
            return ''
    chars[-1] = chr(ord(chars[-1]) + 1)
    return  ''.join(chars)

def get_next_term_from_terms(first, second):
    if not first or not second:
        return ''
    length = len(first) if len(first) < len(second) else len(second)
    for i in range(length):
        if (first[i] != second[i]):
            return second[:i + 1]
    return second

def get_next_term(current_term, terms):
    if (len(terms) > 1):
        return get_next_term_from_terms(terms[-2], terms[-1])
    add_letter = len(terms) == 1 and len(current_term) < 26
    if (len(terms) == 0):
        return increment(current_term, add_letter)
    else:
        return increment(terms[-1], add_letter)

def find(query, term):
    found = query(term)
    next_term = get_next_term(term, found)
    if not next_term:
        return []
    if len(found) > 0 and found[-1].startswith(next_term):
        del found[-1]
    return found + find(query, next_term)

def extract(query):
    usernames = []
    for i in range(ord('a'), ord('z') + 1):
        usernames += find(query, chr(i))
    return usernames

def main():
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

if __name__ == "__main__":
    main()
