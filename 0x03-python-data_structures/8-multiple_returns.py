#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        s_len = None
        first_char = None

    else:
        s_len = len(sentence)
        first_char = sentence[0]
    n_tuple = (s_len, first_char)
    return n_tuple
