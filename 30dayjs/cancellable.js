/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
export const cancellable = function(fn, args, t) {
  const timer = setTimeout(() => {
    return fn(...args)
  }, t)

  return function() {
    return clearTimeout(timer)
  }
};

const fn = (x) => x * 5, args = [2], t = 20
// Output: [{"time": 20, "returned": 10}]

const cancelTimeMs = 50;
const cancelFn = cancellable(fn, args, t);
setTimeout(cancelFn, cancelTimeMs);
