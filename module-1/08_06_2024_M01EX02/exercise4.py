def solution(source, target):
    n_source = len(source)
    n_target = len(target)

    dp = [[0] * (n_target + 1) for _ in range(n_source + 1)]

    for i in range(n_target + 1):
        dp[0][i] = i

    for i in range(n_source + 1):
        dp[i][0] = i

    for i in range(1, n_source + 1):
        for j in range(1, n_target + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[n_source][n_target]


if __name__ == "__main__":
    source = "yu"
    target = "you"
    print(solution(source, target))

    source = "hi"
    target = "hello"
    print(solution(source, target))

    source = "holla"
    target = "hello"
    print(solution(source, target))
