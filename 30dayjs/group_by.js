/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  const res = {};

  this.forEach((item) => {
    const value = fn(item);

    if (!res[value]) {
      res[value] = [item];
    } else {
      res[value].push(item);
    }
  });

  return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
