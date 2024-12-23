export const compose = (fns) => {
  fns = fns.reverse()
  return function(x) {
    for (const fn of fns) {
      x = fn(x)
    }

    return x
  }
}
