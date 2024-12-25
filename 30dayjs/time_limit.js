/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
export const timeLimit = function (fn, t) {
  return async function (...args) {
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => {
        reject(new Error("Time Limit Exceeded"));
      }, t);

      fn(...args)
        .then((res) => {
          clearTimeout(timeout);
          resolve(res);
        })
        .catch((err) => {
          clearTimeout(timeout);
          reject(err);
        });
    });
  };
};
