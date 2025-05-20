def sliding_windows(num_list, k):
    res = []
    n = len(num_list)
    for i in range(k - 1, n - k // 2 + 1):
        res.append(max(num_list[i - k // 2 - 1 : i + k // 2]))
    return res


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(sliding_windows(num_list, k))
