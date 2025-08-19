from collections import deque

graph = {}
search_queue = deque()
# to prevent cycles in the search
visited = set()

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]

search_queue += graph["you"]

while search_queue:
    person = search_queue.popleft()
    if person not in visited:
        if person == "aa":
            print("Found The Mango Seller.")
            break
        else:
            visited.add(person)
            search_queue += graph.get(person, [])
print("The Mango Seller Not Found.")
