def print_dist(dist, v):
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()


def min_dist(mdist, vset, v):
    min_val = float("inf")
    min_ind = -1
    for i in range(v):
        if (not vset[i]) and mdist[i] < min_val:
            min_ind = i
            min_val = mdist[i]
    return min_ind


def dijkstra(graph, v, src):
    mdist = [float("inf") for _ in range(v)]
    vset = [False for _ in range(v)]
    mdist[src] = 0.0

    for _ in range(v - 1):
        u = min_dist(mdist, vset, v)
        vset[u] = True

        for i in range(v):
            if (
                (not vset[i])
                and graph[u][i] != float("inf")
                and mdist[u] + graph[u][i] < mdist[i]
            ):
                mdist[i] = mdist[u] + graph[u][i]

    print_dist(mdist, i)