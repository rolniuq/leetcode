/*
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */

Array.prototype.bubbleSort = function (fn) {
  for (let i = 0; i < this.length; i++) {
    for (let j = 0; j < this.length - 1; j++) {
      if (fn(this[j], this[j + 1])) {
        [this[j], this[j + 1]] = [this[j + 1], this[j]];
      }
    }
  }
};

export const sortBy = function (arr, fn) {
  const myFunc = (a, b) => a - b;
  return arr.bubbleSort(myFunc);
};

const res = sortBy([1, 3, 2, 4, 5, 6]);
for (let index = 0; index < res.length; index++) {
  console.log(res[index]);
}
