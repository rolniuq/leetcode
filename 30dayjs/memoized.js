/**
 * @param {Function} fn
 * @return {Function}
 */
export const memoize = (fn) => {
  const m = {};

  return function(...args) {
    const key = JSON.stringify(args);

    if (m[key] === undefined) {
      m[key] = fn(...args);
    }

    return m[key];
  }
}
