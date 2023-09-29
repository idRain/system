from io import StringIO
import csv

def bfs(graph, result, cur, prev, neighbours):
    parent = 1 if (prev > 0) else 0

    result[cur][1] += parent
    result[cur][3] += prev - parent
    result[cur][0] = len(graph[cur])
    result[cur][4] = neighbours

    for child in graph[cur]:
        result[cur][2] += bfs(graph, result, child, prev + 1, len(graph[cur]) - 1)

    result[cur][2] -= result[cur][0]

    return result[cur][2] + result[cur][0] + 1

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')

    graph = dict()
    nodes = set()
    starts = set()
    not_starts = set()

    for row in reader:
      a = row[0]
      b = row[1]

      if a in graph:
          graph[a].append(b)
      else:
          graph[a] = [b]

      nodes.add(a)
      nodes.add(b)    
      not_starts.add(b)

    for node in nodes:
        if node not in graph:
            graph[node] = []
        if node not in not_starts:
            starts.add(node)

    result = { node: [0, 0, 0, 0, 0] for node in nodes }

    for start in starts:
        bfs(graph, result, start, 0, 0)

    keys = sorted(result.keys())
    values = [result[key] for key in keys]
    
    return '\n'.join([",".join(str(el) for el in value) for value in values])

print(task("1,2\n2,3\n2,4\n3,5\n3,6"))