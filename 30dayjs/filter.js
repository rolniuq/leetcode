/*
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

export const filter = function (arr, fn) {
  const res = [];
  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      res.push(arr[i]);
    }
  }

  return res;
};
