#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    vscore = 0
    kscore = None
    for k, v in a_dictionary.items():
        if vscore < v:
            vscore = v
            kscore = k
    return kscore
