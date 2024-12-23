import { memoize } from "./memoized";

describe("memoize", () => {
  it("Run", () => {
    const fn = () => 1;
    const memo = memoize(fn);
    expect(memo()).toEqual(1);
    expect(memo()).toEqual(1);
  });
});
