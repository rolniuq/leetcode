import { CreateLinkedList, PrintLinkedList } from './helper';
import { node } from './merge_2_list';

function getNodeString(l: node | null): string {
  if (l === null) {
    return '';
  }

  let str = ""
  while (l !== null) {
    str += l.val.toString();
    l = l.next;
  }

  return str;
}

function addTwoNumbers(l1 : node | null, l2 : node | null): node | null {
  const str1 = getNodeString(l1);
  const str2 = getNodeString(l2);

  const num1 = BigInt(str1.split('').reverse().join('') || '0');
  const num2 = BigInt(str2.split('').reverse().join('') || '0');

  const sum = num1 + num2;
  let sumStr = sum.toString().split('').reverse().join('');

  const head: node = { val: parseInt(sumStr[0]), next: null };
  let current: node = head;

  sumStr = sumStr.slice(1);

  while(sumStr.length > 0) {
    current.next = { val: parseInt(sumStr[0]), next: null };
    current = current.next;

    sumStr = sumStr.slice(1);
  }

  return head;
}

const head = addTwoNumbers(CreateLinkedList([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]), CreateLinkedList([5,6,4])); // 807
PrintLinkedList(head)
