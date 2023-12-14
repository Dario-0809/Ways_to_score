# count the number of ways for the score to get to
import math

count = []

def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def ways_to_score(TT_goals, TTL_goals):
    total_goals = TT_goals + TTL_goals
    ways = combinations(total_goals, TT_goals)
    return ways


def counting():  
    matches = int(input())
    if matches > 0 and matches <= 100:

        for i in range(matches):
            score = str(input())
            TT_goals, TTL_goals = map(int, score.split())

            if (TT_goals and TTL_goals > 0) and (TT_goals and TTL_goals <= 10):
                result = ways_to_score(TT_goals, TTL_goals)
                count.append(result)

if __name__ == "__main__":
    counting()
    for i in range(len(count)):
        print(count[i])


# Input: 2
# 2 0
# 1 3
# Output:
# 1
# 4

        