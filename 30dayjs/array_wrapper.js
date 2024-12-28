/**
 * @param {number[]} nums
 * @return {void}
 */
export const ArrayWrapper = function (nums) {
  this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function () {
  return this.nums.flat().reduce((prev, curr) => prev + curr, 0);
};

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function () {
  return `[${this.nums.toString()}]`;
};

const obj1 = new ArrayWrapper([1, 2]);
const obj2 = new ArrayWrapper([3, 4]);
console.log(String(obj1));
console.log(obj1 + obj2); // 10
