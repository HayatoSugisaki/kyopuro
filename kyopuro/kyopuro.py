from collections import deque

def help():
    print("This is a personal library for programming contest by Hayato Sugisaki.")

def hello():
    print('hello')

#幅優先探索で各頂点への最短距離を出す
def shortpath(N_vertex, edge, start):
    
    checklist = deque([])
    visited = [0 for i in range(N_vertex)]
    distance = [0 for i in range(N_vertex)]
    
    checklist.append(start)
    visited[start] = 1
    
    while len(checklist) > 0:
        current = checklist.popleft()
        for v in edge[current]:
            if not visited[v]:
                checklist.append(v)
                visited[v] = 1
                distance[v] = distance[current] + 1

    return(distance)

def hi():
    print(hi)

#幅優先探索で二部グラフか確かめる
def checkbpt(N_vertex, edge):
    checklist = deque([])
    visited = [0 for i in range(N_vertex)]
    distance = [0 for i in range(N_vertex)]
    
    checklist.append(0)
    visited[0] = 1
    
    while len(checklist) > 0:
        current = checklist.popleft()
        for v in edge[current]:
            
            if visited[v]:
                if distance[v] == distance[current]:
                    return(False)
                
            if not visited[v]:
                checklist.append(v)
                visited[v] = 1
                distance[v] = distance[current] + 1
    return(True)
