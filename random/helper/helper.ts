export type LinkedNode = {
  val: number;
  next: LinkedNode | null;
};

export type TreeNode = {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

export function CreateLinkedList(arr: number[]): LinkedNode | null {
  let head: LinkedNode = { val: arr[0], next: null };
  let current: LinkedNode = head;

  for (let i = 1; i < arr.length; i++) {
    current.next = { val: arr[i], next: null };
    current = current.next;
  }

  return head;
}

export function PrintLinkedList(head: LinkedNode | null): void {
  let current: LinkedNode | null = head;

  while (current !== null) {
    console.log(current.val);
    current = current.next;
  }
}
