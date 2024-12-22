import { filter } from "./filter";

describe("Test filter", () => {
  it("Run", () => {
    const arr = [1, 2, 3];
    const greaterThanOne = (i) => {
      if (i > 1) {
        return i;
      }
    };

    const res = filter(arr, greaterThanOne);
    expect(res[0]).toEqual(2);
    expect(res[1]).toEqual(3);
  });
});
