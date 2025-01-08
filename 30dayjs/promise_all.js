/*
 * @param {Array<Function>} fns
 * @return {Promise<any>}
 */
export const promiseAll = (fns) => {
  return new Promise((resolve, reject) => {
    let count = 0;
    const results = [];

    fns.forEach((fn, index) => {
      fn()
        .then((res) => {
          results[index] = res;
          count++;

          if (count === fns.length) resolve(results);
        })
        .catch((err) => reject(err));
    });

    return resolve(results);
  });
};
