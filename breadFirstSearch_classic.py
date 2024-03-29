''' bread first search'''

graph = {'S':['A','G'],
         'A':['B','C'],
         'B':['D'],
         'C':['D','G'],
         'D':['G'],
         'G':['G']
        }


start = 'S'
goal = 'C'
queue = [[start]]
visited =[]
print('Bread First Search Algorithm for graph1')
print('Starts from: ', start)
print('The goal is: ', goal)
while queue:
    path = queue.pop(0)   # get the  first list from queue
    print('poped path ',path)
    node = path[-1]      # get the first state of the poped list
    if node == goal:
        print('the path is: ',path)
        break
    if node not in visited:
        visited.append(node)
    children = graph[node]   
    for child in children:
        if child not in visited:
            newPath = path + list(child)
            queue.append(newPath)
            visited.append(child)
        else:
            print(child +' already visited')

    print('queue : ',queue)
print('visted: ',visited)
