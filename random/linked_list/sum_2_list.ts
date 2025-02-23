import { CreateLinkedList, PrintLinkedList } from '../helper/helper';
import { TreeNode } from '../helper/helper';

function getNodeString(l: TreeNode | null): string {
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

function addTwoNumbers(l1 : TreeNode | null, l2 : TreeNode | null): TreeNode | null {
  const str1 = getNodeString(l1);
  const str2 = getNodeString(l2);

  const num1 = BigInt(str1.split('').reverse().join('') || '0');
  const num2 = BigInt(str2.split('').reverse().join('') || '0');

  const sum = num1 + num2;
  let sumStr = sum.toString().split('').reverse().join('');

  const head: TreeNode = { val: parseInt(sumStr[0]), next: null };
  let current: TreeNode = head;

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
