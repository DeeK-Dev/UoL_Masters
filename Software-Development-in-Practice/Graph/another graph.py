# London Underground Journey Planner - www.101computing.net/london-underground-journey-planner/

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def find_shortest_path(graph, start, end, shortest_length=-1, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            if shortest_length == -1 or len(path) < (shortest_length - 1):
                new_path = find_shortest_path(graph, node, end, shortest_length, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
                        shortest_length = len(new_path)
    return shortest


graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

stationFrom = "a"
stationTo = "e"
print("From: " + stationFrom)
print("To: " + stationTo)
print("\nSearching for a path...")
a_path = find_path(graph_elements, stationFrom, stationTo)
print(a_path)
print("\nSearching for all paths...")
all_path = find_all_paths(graph_elements, stationFrom, stationTo)
print(all_path)
print("\nSearching shortest route... This may take a while...")
shortest_path = find_shortest_path(graph_elements, stationFrom, stationTo)
print("Suggested Route: ")
print(shortest_path)
