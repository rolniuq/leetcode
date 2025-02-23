export type TreeNode = {
  val: number;
  next: TreeNode | null;
};

export function CreateLinkedList(arr: number[]): TreeNode | null {
  let head: TreeNode = { val: arr[0], next: null };
  let current: TreeNode = head;

  for (let i = 1; i < arr.length; i++) {
    current.next = { val: arr[i], next: null };
    current = current.next;
  }

  return head;
}

export function PrintLinkedList(head: TreeNode | null): void {
  let current: TreeNode | null = head;

  while (current !== null) {
    console.log(current.val);
    current = current.next;
  }
}
