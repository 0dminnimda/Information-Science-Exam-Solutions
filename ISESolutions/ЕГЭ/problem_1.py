#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from __future__ import annotations
from collections import defaultdict

__all__ = (
    "Node",)


# the problem gives us a drawing of a graph
# and a table describing the lengths of the edges of the graph

# the problem breaks down into two parts:
# 1) comparison of names from the figure and the table
# 2) finding a certain length with some conditions

# 1 - problem of determining the bijective mapping
# between the vertices of two undirected isomorphic graphs

class Node2:
    def __init__(self, name: str) -> None:
        self.name = name
        self.incoming_edges: list[Edge] = list()
        self.outgoing_edges: list[Edge] = list()

    def attach(self, other: Node, length: int = 1) -> Node:
        edge: Edge = Edge(self, other, length)
        other.incoming_edges.append(edge)
        self.outgoing_edges.append(edge)
        return self


class EdgeProperties:
    def __init__(self, length: int = None):
        self.length: int = length

    def same_relation(self):
        pass


class Edge:
    def __init__(self,
                 node1: Node, node2: Node,
                 length: int = 1) -> None:
        self.node1: Node = node1
        self.node2: Node = node2
        self.length: int = length

    def are_nodes_equal(self, other: Edge):
        return (
            (self.node1 == other.node1)
            and (self.node2 == other.node2))

    def __eq__(self, other: Edge):
        return (
            self.are_nodes_equal(other)
            and (self.length == other.length))


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.edges: dict[Node, EdgeProperties] = dict()

    def attach(self, other: Node,
               edge_props: EdgeProperties = EdgeProperties()) -> Node:
        if self.validate_edge(other):
            other.edges[self] = edge_props
            self.edges[other] = edge_props
        return self

    def validate_edge(self, other: Edge) -> bool:
        if self.edges.get(other, None) is None:
            return True
        return False


named_nodes = [Node(chr(i)) for i in range(ord("а"), ord("ж")+1)]
nodes = [Node(str(i)) for i in range(len(named_nodes))]

edge_indices = [
    [0, 1, 19], [0, 2, 18], [0, 3, 21],
    [1, 2, 23], [1, 5, 15], [1, 6, 16],
    [2, 3, 22], [2, 6, 11],
    [4, 5, 10], [4, 6, 12],
    [5, 6, 14]]

for i, j, *k in edge_indices:
    nodes[i].attach(nodes[j], *k)

named_edge_indices = [
    [0, 1], [0, 4],
    [1, 2], [1, 4],
    [2, 3], [2, 4], [2, 5],
    [3, 5], [3, 6],
    [4, 5],
    [5, 6]]

for i, j in named_edge_indices:
    named_nodes[i].attach(named_nodes[j])

defdict = defaultdict(list)
named_defdict = defaultdict(list)

for n in named_nodes:
    named_defdict[len(n.edges)].append(n)
    # print(n.name, len(n.edges))

# print()

for n in nodes:
    named_defdict[len(n.edges)].append(n)
    # print(n.name, len(n.edges))

