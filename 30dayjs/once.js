/**
 * @param {Function} fn
 * @return {Function}
 */

export const once = (fn) => {
  let wasCalled = false;

  return function(...args){
    if (wasCalled) {
      return undefined;
    }

    wasCalled = true;
    return fn(...args);
  }
};

const fn = (a,b,c) => (a + b + c)
const onceFn = once(fn)

console.log(onceFn(1,2,3));
console.log(onceFn(2,3,6));
