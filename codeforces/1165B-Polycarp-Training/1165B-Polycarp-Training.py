n = int(input())
contests = list(map(int, input().split()))
contests.sort()
day = 1
for problems in contests:
    if problems >= day:
        day += 1
print(day - 1)