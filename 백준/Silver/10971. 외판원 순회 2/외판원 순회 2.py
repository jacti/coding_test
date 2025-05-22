import sys
sys.path.append("/Users/jactio/develop/coding_test/function_visualizer")
sys.stdin = open("input.txt", "r")

from function_visualizer import FunctionVisualizer

visualizer = FunctionVisualizer()

N = int(sys.stdin.readline())

graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

@visualizer.visualize(param_names=["cur","n"],show_execution_order=True)
def TSP(cur:int,n:int,prefix_sum:int,visited:list[bool]):
    global graph
    if n ==0:
        return prefix_sum + (float('inf') if graph[cur][0]==0 else graph[cur][0])
    else:
        result = []
        for i, visit in enumerate(visited):
            if not visit:
                if graph[cur][i] == 0:
                    result.append(float('inf'))
                else:
                    new_sum = prefix_sum + graph[cur][i]
                    new_visited = visited[:]
                    new_visited[i] = True
                    result.append(TSP(i,n-1,new_sum,new_visited))
        return min(result)

visited = [False]*N
visited[0] = True
print(TSP(0,N-1,0,visited))

visualizer.render("TSP2_4","png")