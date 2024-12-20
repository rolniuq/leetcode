import { createCounter } from "./counter";

describe("createCounter", () => {
  const n = 10;
  it("Should be return 10 11 12", () => {
    f = createCounter(n);
    expect(f()).toEqual(10);
    expect(f()).toEqual(11);
    expect(f()).toEqual(12);
  });
});
