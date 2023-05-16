

def calc(n, k, houses, result):
    if k <= 0:
        print(houses, result)
        return (result, houses)

    distance = [[(abs(houses[i][0] - houses[j][0]) +
                  abs(houses[i][1] - houses[j][1]), j) for j in range(n)] for i in range(n)]
    dis = []
    for i in distance: dis.append(sorted(i, key=lambda x: x[0]))
    bang = [[i] for i in range(n)]
    for i in dis: bang[i[1][1]].append(i[0][1])
    bang.sort(key=lambda x: len(x), reverse=True)
    for i in bang[0]:
        result = max(result, distance[bang[0][0]][i][0])

    new_houses = []
    for i in range(n):
        if i not in bang[0]: new_houses.append(houses[i])

    (result, houses) = calc(len(new_houses), k - 1, new_houses, result)

    if not houses: return result
    for i in houses:
        print(result, distance[bang[0][0]][i[2]][0], distance[bang[0][0]], i[2])

        result = max(result, distance[bang[0][0]][i[2]][0])

    return result, []


def solution():
    n, k = map(int, input().split())
    houses = []
    for i in range(n):
        a, b = map(int, input().split())
        houses.append((a, b, i))

    return calc(n, k, houses, 0)[0]


print(solution())
# [[0, 4, 4, 10, 14], [4, 0, 0, 6, 10], [4, 0, 0, 6, 10], [10, 6, 6, 0, 4], [14, 10, 10, 4, 0]]
# [0, 4, 4, 10, 14]
# [4, 0, 0, 6, 10]
# [4, 0, 0, 6, 10]
# [10, 6, 6, 0, 4]
# [14, 10, 10, 4, 0]
# 4