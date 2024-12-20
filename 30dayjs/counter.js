export const createCounter = function (n) {
  return function () {
    return n++;
  };
};
