function getNumStr(num: string): string {
  return num === '0' ? '1' : '0';
}

function getDiffNum(num: string): string {
  let res = ""

  for (let i = 0; i < num.length; i++) {
    res += getNumStr(num[i]);
  }

  return res
}

function findDifferentBinaryString(nums: string[]): string {
  const first = getDiffNum(nums[0]);
  console.log(first);
  return ''
};

console.log(findDifferentBinaryString(["01", "10"])) // "11";
