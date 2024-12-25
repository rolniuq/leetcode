/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
export const chunk = function (arr, size) {
  return arr.reduce((res, _, index) => {
    if (index % size === 0) {
      res.push(arr.slice(index, index + size));
    }

    return res;
  }, []);
};
