lookup = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def int_to_roman(integer):
    try:
        return lookup[integer]
    except Exception as error:
        print(error)
