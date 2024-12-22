/*
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

export const map = (arr, fn) => {
  const returnArr = [];
  for (let i = 0; i < arr.length; i++) {
    returnArr[i] = fn(arr[i], i);
  }

  return returnArr;
};
