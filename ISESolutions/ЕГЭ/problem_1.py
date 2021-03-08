#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from __future__ import annotations

__all__ = (
    "Node",)


# the problem gives us a drawing of a graph
# and a table describing the lengths of the edges of the graph

# the problem breaks down into two parts:
# 1) comparison of names from the figure and the table
# 2) finding a certain length with some conditions


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.parents: list[Node] = list()
        self.children: list[Node] = list()

    def attach(self, other: Node) -> Node:
        other.parents.append(self)
        self.children.append(other)
        return self


class Edge:
    def __init__(self, start_node: Node, end_node: Node) -> None:
        pass
