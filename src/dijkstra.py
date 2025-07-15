import heapq

def dijkstra(graph,start) : #다익스트라 알고리즘

    distances = {node: float("inf") for node in graph} #역간 거리를 무한대로 초기화 // (진짜 무한대가 아니라 무한대라고 가정)
    distances[start] = 0 # 처음역이니까 당연히 거리가 0

    que =[(0,start)] # 처음역 거리,처음역 이름

    visited = set() #방문했던 역들을 모아둘 set자료형

    prev = {node: None for node in graph} #방문했던 역들 거리

    while que : 
        c_distance, c_node = heapq.heappop(que) #처음역에서 현재까지 최단거리, 현재 역명

        if c_node in visited : #방문한적이 있으면 넘기고, 방문한 적 없다면 방문 기록 남기기
            continue
        visited.add(c_node)

        for neighbor, n_dist in graph[c_node].items() : #현재역에서 갈 수 있는 역, 그리고 그 역까지의 최단거리// 갈 수 있는 역이 있을 때까지 반복
            new_dist = c_distance + n_dist #이전역까지 최단거리 + 현재 체크한거리

            if new_dist < distances[neighbor] : #지금 현재역까지의 거리가 그 전에 기록된 현재역까지 거리가 작으면 지금 잰 걸로 저장
                distances[neighbor] = new_dist
                prev[neighbor] = c_node
                heapq.heappush(que,(new_dist,neighbor))


    return  distances, prev #시작역부터 각 역의 최단거리, 현재역이 이전역 어디서 왔는지 체크


def routes(prev, end) : #
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    return list(reversed(path))
