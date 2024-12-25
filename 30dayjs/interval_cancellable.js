/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
export const intervalCancellable = function (fn, args, t) {
  fn(...args);
  const timer = setInterval(() => {
    fn(...args);
  }, t);

  return function () {
    return clearInterval(timer);
  };
};
