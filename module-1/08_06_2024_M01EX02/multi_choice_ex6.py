def my_func(data, ma, mi):
    res = []

    for i in data:
        if i < mi:
            res.append(mi)
        elif i > ma:
            res.append(ma)
        else:
            res.append(i)
    return res


if __name__ == "__main__":
    print(my_func([10, 2, 5, 0, 1], 2, 1))
