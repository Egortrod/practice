def diff_keys(old, new):
    old_keys = set(old)
    new_keys = set(new)
    return {
        'kept': old_keys & new_keys,
        'added': new_keys - old_keys,
        'removed': old_keys - new_keys,
    }