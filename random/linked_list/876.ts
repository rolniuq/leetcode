import { LinkedNode } from "../helper/helper";

function middleOfNode(head: LinkedNode | null): LinkedNode | null {
  let fast = head;
  let slow = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  return slow;
}
