import { reduce } from './reduce';

describe('reduce', () => {
  const nums = [1, 2, 3, 4];
  const fn = (a, b) => a + b;
  const init = 0;
  it('Should be return 10', () => {
    expect(reduce(nums, fn, init)).toEqual(10);
  });
});
