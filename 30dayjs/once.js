/**
 * @param {Function} fn
 * @return {Function}
 */

export const once = (fn) => {
  let wasCalled = false;

  return function (...args) {
    if (wasCalled) {
      return undefined;
    }

    wasCalled = true;
    return fn(...args);
  };
};
