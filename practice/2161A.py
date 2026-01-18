test_cases = int(input())

for i in range(test_cases):
    elo, min_elo, delta, _ = map(lambda x: int(x), input().split(" "))
    contests = input()
    # print(elo, min_elo, delta)
    result = 0
    for contest in contests:
        can_participate = False
        # print(contest)
        if contest == "2":
            if elo < min_elo:
                can_participate = True
        else:
            can_participate = True
        
        if can_participate:
            elo = max(0, elo - delta)
            result += 1
    print(result)