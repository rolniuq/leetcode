class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(node: Node) -> int:
    if not node:
        return 0

    left = height(node.left)
    right = height(node.right)

    return 1 + max(left, right)


def is_balanced(tree: Node) -> bool:
    if not tree:
        return True

    left = height(tree.left)
    right = height(tree.right)

    return abs(left - right) <= 1 and is_balanced(tree.left) and is_balanced(tree.right)


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == "__main__":
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print("true" if res else "false")
