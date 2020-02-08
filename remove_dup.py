#
def remove_duplicates(text):
    # text: list of string
    text_set = {}
    for t in text:
        if t not in text_set:
            text_set.add(t)

    return text
