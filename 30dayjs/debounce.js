/*
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
export const debounce = (fn, t) => {
  let timerId = null;
  return function (...args) {
    clearTimeout(timerId);
    timerId = setTimeout(() => fn(...args), t);
  };
};
