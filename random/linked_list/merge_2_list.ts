export type node = {
  val: number;
  next: node | null;
};

function mergeTwoLists(l1: node | null, l2: node | null): node | null {
  if (!l1) return l2;
  if (!l2) return l1;

  let head: node = { val: 0, next: null };
  let current: node = head;

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
