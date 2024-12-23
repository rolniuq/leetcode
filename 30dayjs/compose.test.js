import { compose } from "./compose";

describe("compose", () => {
  it("Run", () => {
    const fns = [x => x + 1, x => 2 * x];
    const fn = compose(fns);
    const res = fn(4);
    expect(res).toEqual(9);
  });
})
