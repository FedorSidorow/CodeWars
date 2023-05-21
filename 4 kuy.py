def strip_comments(strng, markers):
    """
    strips all text that follows any of a set of comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.
    """
    text = strng.split('\n')
    for key in markers:
        text = [v.split(key)[0].rstrip() for v in text]
    return "\n".join(text)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ['#', '!']))