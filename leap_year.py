# うるう年判定

def leap_year(y):
    flag = False

    if y % 400 == 0:
        flag = True
    elif y % 100 == 0:
        pass
    elif y % 4 == 0:
        flag = True

    return flag
