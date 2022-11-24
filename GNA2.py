def flatten(l):
    return [item for sublist in l for item in sublist]

def reduce_string(s):
    reduced = [[s[0]]]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            reduced = [*reduced, [s[i]]]
        else:
            reduced[len(reduced) - 1] = [*reduced[len(reduced) - 1], s[i]]
    return [[list[0], len(list)] for list in reduced]

print(''.join((str(x) for x in flatten(reduce_string('aaaabbbbbcccddaa')))))