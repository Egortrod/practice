def get_first_name(fullname):
    return fullname.split('_')[0]


def sort_by(key, coll):
    return sorted(coll, key=key) #sorted by key-func