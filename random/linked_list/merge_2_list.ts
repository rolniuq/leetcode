import { TreeNode } from "../helper/helper";

function mergeTwoLists(l1: TreeNode | null, l2: TreeNode | null): TreeNode | null {
  if (!l1) return l2;
  if (!l2) return l1;

  let head: TreeNode = { val: 0, next: null };
  let current: TreeNode = head;

  while (l1 && l2) {
    if (l1.val < l2.val) {
      current.next = l1;
      l1 = l1.next;
    } else {
      current.next = l2;
      l2 = l2.next;
    }

    current = current.next;
  }

  current.next = l1 || l2;

  return head;
}
