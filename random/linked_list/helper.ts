import { node } from './merge_2_list';

export function CreateLinkedList(arr: number[]): node | null {
  let head: node = { val: arr[0], next: null };
  let current: node = head;

  for (let i = 1; i < arr.length; i++) {
    current.next = { val: arr[i], next: null };
    current = current.next;
  }

  return head;
}

export function PrintLinkedList(head: node | null): void {
  let current: node | null = head;

  while (current !== null) {
    console.log(current.val);
    current = current.next;
  }
}
