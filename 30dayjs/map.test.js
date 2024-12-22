import { map } from "./map";

describe("Test map", () => {
  it("Plus", () => {
    const arr = [1, 2, 3];
    const fn = (i) => {
      return i + 1;
    };

    const res = map(arr, fn);
    expect(res[0]).toEqual(2);
    expect(res[1]).toEqual(3);
    expect(res[2]).toEqual(4);
  });
});
