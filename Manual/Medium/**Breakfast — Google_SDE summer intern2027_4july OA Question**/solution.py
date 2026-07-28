import sys
import heapq

def Solution(N, M, edges):
    adjList = [[] for i in range(N+1)]
    # no assembling possible return -1 else return lexio smallest one
    min_heap = []
    ind = [0]*(N+1)
    for u,v in edges:
        adjList[u].append(v)
        ind[v]+= 1
    # here I am able to complete my graph with indegeree and now i will go with the Khan's algo for finding the topo sort
    for i in range(1,N+1):
        if ind[i] == 0:
            heapq.heappush(min_heap,i)
    heapq.heapify(min_heap)
    result = []
    while min_heap:
        temp = heapq.heappop(min_heap)
        result.append(temp)
        for neighbour in adjList[temp]:
            ind[neighbour]-=1
            if ind[neighbour] == 0:
                heapq.heappush(min_heap,neighbour)
    if len(result) != N:
        return [-1]
    return result





def main():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx+=1
    for _ in range(T):
        N = int(data[idx]); idx+=1
        M = int(data[idx]); idx+=1
        edges = []
        for _ in range(M):
            a = int(data[idx]); idx+=1
            b = int(data[idx]); idx+=1
            edges.append((a,b))
        result = Solution(N, M, edges)
        if result:
            print(' '.join(map(str,result)))
        else:
            print(result)

if __name__ == "__main__":
    main()
