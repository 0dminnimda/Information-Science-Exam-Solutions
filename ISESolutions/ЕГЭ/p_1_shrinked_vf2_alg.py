import networkx as nx
class GraphMatcher:
    def __init__(self, G1, G2):
        self.G1 = G1
        self.G2 = G2
        self.G2_nodes = set(G2.nodes())
        self.G2_node_order = {n: i for i, n in enumerate(G2)}
        self.core_1 = {}
        self.core_2 = {}
        self.inout_1 = {}
        self.inout_2 = {}
        self.state = GMState(self)
    def candidate_pairs_iter(self):
        G2_nodes = self.G2_nodes
        min_key = self.G2_node_order.__getitem__
        T1_inout = [node for node in self.inout_1 if node not in self.core_1]
        T2_inout = [node for node in self.inout_2 if node not in self.core_2]
        if T1_inout and T2_inout:
            node_2 = min(T2_inout, key=min_key)
            for node_1 in T1_inout:
                yield node_1, node_2
        else:  # XXX
            other_node = min(G2_nodes - set(self.core_2), key=min_key)
            for node in self.G1:
                if node not in self.core_1:
                    yield node, other_node
    def match(self):
        if len(self.core_1) == len(self.G2):
            yield self.core_1.copy()
        else:
            for G1_node, G2_node in self.candidate_pairs_iter():
                if self.syntactic_feasibility(G1_node, G2_node):
                    newstate = self.state.__class__(self, G1_node, G2_node)
                    yield from self.match()
                    newstate.restore()
    def syntactic_feasibility(self, G1_node, G2_node):
        if self.G1.number_of_edges(
                G1_node, G1_node) != self.G2.number_of_edges(
                G2_node, G2_node):
            return False
        for neighbor in self.G1[G1_node]:
            if neighbor in self.core_1:
                if not (self.core_1[neighbor] in self.G2[G2_node]):
                    return False
                elif self.G1.number_of_edges(
                    neighbor, G1_node
                ) != self.G2.number_of_edges(self.core_1[neighbor], G2_node):
                    return False
        for neighbor in self.G2[G2_node]:
            if neighbor in self.core_2:
                if not (self.core_2[neighbor] in self.G1[G1_node]):
                    return False
                else:
                    if self.G1.number_of_edges(
                        self.core_2[neighbor], G1_node
                    ) != self.G2.number_of_edges(neighbor, G2_node):
                        return False
        num1 = 0
        for neighbor in self.G1[G1_node]:
            if (neighbor in self.inout_1) and (neighbor not in self.core_1):
                num1 += 1
        num2 = 0
        for neighbor in self.G2[G2_node]:
            if (neighbor in self.inout_2) and (neighbor not in self.core_2):
                num2 += 1
        if not (num1 == num2):
            return False
        num1 = 0
        for neighbor in self.G1[G1_node]:
            if neighbor not in self.inout_1:
                num1 += 1
        num2 = 0
        for neighbor in self.G2[G2_node]:
            if neighbor not in self.inout_2:
                num2 += 1
        if not (num1 == num2):
            return False
        return True
class GMState:
    def __init__(self, GM, G1_node=None, G2_node=None):
        self.GM = GM
        self.G1_node = None
        self.G2_node = None
        self.depth = len(GM.core_1)
        if G1_node is None or G2_node is None:
            GM.core_1 = {}
            GM.core_2 = {}
            GM.inout_1 = {}
            GM.inout_2 = {}
        if G1_node is not None and G2_node is not None:
            GM.core_1[G1_node] = G2_node
            GM.core_2[G2_node] = G1_node
            self.G1_node = G1_node
            self.G2_node = G2_node
            self.depth = len(GM.core_1)
            if G1_node not in GM.inout_1:
                GM.inout_1[G1_node] = self.depth
            if G2_node not in GM.inout_2:
                GM.inout_2[G2_node] = self.depth
            new_nodes = set()
            for node in GM.core_1:
                new_nodes.update(
                    [neighbor for neighbor in GM.G1[node]
                     if neighbor not in GM.core_1])
            for node in new_nodes:
                if node not in GM.inout_1:
                    GM.inout_1[node] = self.depth
            new_nodes = set()
            for node in GM.core_2:
                new_nodes.update(
                    [neighbor for neighbor in GM.G2[node]
                     if neighbor not in GM.core_2])
            for node in new_nodes:
                if node not in GM.inout_2:
                    GM.inout_2[node] = self.depth
    def restore(self):
        if self.G1_node is not None and self.G2_node is not None:
            del self.GM.core_1[self.G1_node]
            del self.GM.core_2[self.G2_node]
        for vector in (self.GM.inout_1, self.GM.inout_2):
            for node in list(vector.keys()):
                if vector[node] == self.depth:
                    del vector[node]

G1 = nx.path_graph(4)
G2 = nx.path_graph("3210")
GM = GraphMatcher(G1, G2)
print(next(GM.match()))
