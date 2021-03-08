#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from ISESolutions.ЕГЭ.problem_1 import Node
import pytest


def test_node_init():
    name: str = "root"
    node: Node = Node(name)
    assert node.name == name
    assert len(node.parents) == 0
    assert len(node.children) == 0

