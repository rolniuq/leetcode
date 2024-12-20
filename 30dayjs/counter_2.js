export function createCounter2(n) {
  var value = n;

  return {
    reset() {
      value = n
      return value
    },
    increment() {
      value++;
      return value
    },
    decrement() {
      value--;
      return value
    },
  };
}
