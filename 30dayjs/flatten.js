/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
const flat = function (arr, n) {
  if (n <= 0) return arr;

  const res = [];

  arr.forEach((item) => {
    if (Array.isArray(item)) {
      for (let i = 0; i < item.length; i++) {
        res.push(item[i]);
      }
    } else {
      res.push(item);
    }
  });

  return flat(res, n - 1);
};
