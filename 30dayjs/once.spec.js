import { once } from "./once";

describe("once", () => {
  it("Run", () => {
    const fn = (a, b) => a + b;
    const res = once(fn)(1, 2);
    expect(res).toEqual(3);
  });
});
