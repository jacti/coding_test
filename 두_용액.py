import sys

# sys.stdin = open("input.txt","r")
N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()


def binary_search(target, solutions):
    solutions
    global N
    left = 0
    right = N - 2

    while left <= right:
        half = (left + right) // 2
        if solutions[half] == target:
            return solutions[half]
        elif solutions[half] < target:
            left = half + 1
        else:
            right = half - 1
    if right == -1:
        return solutions[0]
    elif left == N - 1:
        return solutions[N - 2]
    else:
        i = max(left, right)
        if abs(target - solutions[i - 1]) < abs(solutions[i] - target):
            return solutions[i - 1]
        else:
            return solutions[i]


min_sum = float("inf")
min_comb = None

for index, solution in enumerate(solutions):
    rest = 0 - solution
    new_solutions = solutions[:index]
    if index < N - 1:
        new_solutions += solutions[index + 1 :]
    b = binary_search(rest, new_solutions)
    solution_sum = abs((solution + b))
    if min_sum > solution_sum:
        min_sum = solution_sum
        min_comb = [solution, b]
        if min_sum == 0:
            break

min_comb.sort()
print(f"{min_comb[0]} {min_comb[1]}")
