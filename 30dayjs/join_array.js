/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
export const join = function (arr1, arr2) {
  const res = {};

  arr1.forEach((obj) => (res[obj.id] = obj));

  arr2.forEach((obj) => {
    if (res[obj.id]) {
      res[obj.id] = { ...res[obj.id], ...obj };
    } else {
      res[obj.id] = obj;
    }
  });

  return Object.values(res);
};

const arr1 = [{ id: 1, b: { b: 94 }, v: [4, 3], y: 48 }];
const arr2 = [{ id: 1, b: { c: 84 }, v: [1, 3] }];

const res = join(arr1, arr2);
console.log(res);
