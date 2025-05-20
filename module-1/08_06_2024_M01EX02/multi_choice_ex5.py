def check_the_number(n):
    lst_numbers = []

    for i in range(1, 5):
        lst_numbers.append(i)
    if n in lst_numbers:
        return "True"
    return "False"


if __name__ == "__main__":
    n = 7
    print(check_the_number(n))
