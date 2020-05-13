# class Stack():
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.stack)


# def earliest_ancestor(ancestors, starting_node):
#     # Create a q/stack and enqueue starting vertex
#     stack = Stack()
#     visited = set()
#     stack.push(starting_node)
#     first = -1
#     # While stack has ancestors and queue is not empty:
#     while stack.size() > 0:
#         # pop the first vertex/ancestor
#         vertex = stack.pop()
#         # if ancestor not visited
#         if vertex not in visited:
#             # mark as visited
#             visited.add(vertex)
#             print(visited)

#             for ancestor in ancestors:

#                 if ancestor[1] == vertex:
#                     stack.push(ancestor[0])

#                     if first == -1:
#                         first = ancestor[0]
#                     parents = []

#                     for anc in ancestors:
#                         if anc[1] == vertex:
#                             parents.append(anc[0])

#                             if len(parents) == 1:
#                                 first = anc[0]
#                             else:
#                                 if first > anc[0]:
#                                     first = anc[0]
#     return first

def earliest_ancestor(ancestors, starting_node):
    parents = []

    for relationship in ancestors:
        if relationship[1] == starting_node:
            parents.append(relationship)

    while len(parents) > 0:
        ancestor = parents.pop()
        earlier_ancestor = earliest_ancestor(ancestors, ancestor[0])
        if earlier_ancestor > -1:
            parents.append((earlier_ancestor, ancestor[0]))
        elif len(parents) == 0:
            return ancestor[0]

    return -1
