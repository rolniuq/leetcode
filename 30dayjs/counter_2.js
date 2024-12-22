/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
export function createCounter2(n) {
  var value = n;

  return {
    reset() {
      value = n;
      return value;
    },
    increment() {
      value++;
      return value;
    },
    decrement() {
      value--;
      return value;
    },
  };
}
