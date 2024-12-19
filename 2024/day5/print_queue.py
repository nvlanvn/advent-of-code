from collections import defaultdict, deque


def topological_sort(graph):
    in_degree = {u: 0 for u in graph}  # Initialize in-degree of all vertices to 0
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1  # Calculate in-degree of each vertex

    queue = deque(
        [u for u in graph if in_degree[u] == 0]
    )  # Collect all vertices with in-degree 0
    sorted_list = []

    while queue:
        u = queue.popleft()
        sorted_list.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(sorted_list) == len(graph):
        return sorted_list
    else:
        raise ValueError("Graph has a cycle, topological sort not possible")


def reorder_pages(rules, updates):
    graph = defaultdict(list)
    for rule in rules:
        u, v = rule.split("|")
        graph[u].append(v)

    reordered_updates = []
    for update in updates:
        try:
            sorted_update = topological_sort({u: graph[u] for u in update})
            reordered_updates.append(sorted_update)
        except ValueError:
            reordered_updates.append(update)  # If cycle detected, keep original order

    return reordered_updates


# Example rules and updates
rules = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
]

updates = [
    ["75", "97", "47", "61", "53"],
    ["61", "13", "29"],
    ["97", "13", "75", "29", "47"],
]

reordered_updates = reorder_pages(rules, updates)
for update in reordered_updates:
    print(update)
