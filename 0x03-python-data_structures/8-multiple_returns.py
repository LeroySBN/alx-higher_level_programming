def multiple_returns(sentence):
    if sentence == "":
        return (len(sentence), None)
    else:
        length = len(sentence)
        first = sentence[0]
        return (length, first)
