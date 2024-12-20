import {createCounter2 } from './counter_2'

describe('Counter 2', () => {
  const n = 10;

  it('Should be return 10 11 12', () => {
    const f = createCounter2(n);
    expect(f.reset()).toEqual(10);
    expect(f.increment()).toEqual(11);
    expect(f.decrement()).toEqual(10);
  });
});
