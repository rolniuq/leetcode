import { cancellable } from "./cancellable";

describe("cancellable", () => {
  it("Run", async () => {
    let v = 0
    const fn = (x) => {
      v = x * 5
      return v
    }, args = [2], t = 20
    const cancelTimeMs = 50;
    const cancelFn = cancellable(fn, args, t);
    await setTimeout(() => {
      cancelFn()
      expect(v).toEqual(10)
    }, cancelTimeMs);
  })
})
