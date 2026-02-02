import node, a_star, os
os.system("cls" if os.name == "nt" else "clear")

# Declaration of h(n) = x, estimated cost from node n to goal
S = node.node("S", 7)
A = node.node("A", 6)
B = node.node("B", 5)
C = node.node("C", 1)
D = node.node("D", 4)
G = node.node("G", 0)

# Declaration of edges and costs
S.set_edges({A: 2, B: 4})
A.set_edges({C: 5, D: 10})
B.set_edges({D: 4})
C.set_edges({G: 3})
D.set_edges({G: 2})

# Create instance of A*
star = a_star.a_star()
star.search(S, G)

