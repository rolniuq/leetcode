from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def dfs(root: Node, path: str, res: List[str]):
    if not root:
        return

    if not root.children:
        res.append(path + str(root.val))
        return

    for child in root.children:
        dfs(child, path + str(root.val), res)


def ternary_tree_paths(root: Node) -> List[str]:
    res = []
    dfs(root, "", res)
    return res
