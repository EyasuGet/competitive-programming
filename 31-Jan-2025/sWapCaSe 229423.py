# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

modified = ""
    for i in s:
        if i.upper() == i:
            modified += i.lower()
        else:
            modified +=  i.upper()
    return modified