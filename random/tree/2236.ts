import { TreeNode } from "../helper/helper";

function checkTree(root: TreeNode | null): boolean {
  const headVal = root.val;

  const sum = root.left.val + root.right.val;

  return headVal === sum;
}
