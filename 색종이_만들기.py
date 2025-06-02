import sys
import time

start = time.time()

# sys.path.append("/Users/jactio/develop/coding_test/function_visualizer")
sys.stdin = open("input.txt", "r")

# from function_visualizer import FunctionVisualizer

# visualizer = FunctionVisualizer()

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

blue_count = 0
white_count =0

# @visualizer.visualize(param_names=["n","x","y"],show_execution_order=True)
def split_and_merge(n, x, y):
    global paper
    global blue_count
    global white_count
    if n == 1:
        return paper[x][y]
    else:
        n //= 2
        result = [
            split_and_merge(n, x, y),
            split_and_merge(n, x, y + n),
            split_and_merge(n, x + n, y),
            split_and_merge(n, x + n, y + n),
        ]
        count = 4
        sum = 0
        for i in result:
            if i == "finish":
                count -=1
            else:
                sum += i
        if 0 < sum < 4:
            blue_count +=sum
            white_count += count - sum
            return "finish"
        elif count != 4:
            white_count += count - sum
            return "finish"
        else:
            return 1 if sum == 4 else 0

result = split_and_merge(N,0,0)
if result != "finish":
    blue_count += result
    white_count += 1-result
print(white_count)
print(blue_count)

end = time.time()
print(f"\n⏱ 실행 시간: {end - start:.6f}초")
# visualizer.render("paper","svg")