import { ArrayWrapper } from "./array_wrapper";

describe("Array wrapper", () => {
  it("Run", () => {
    const arr1 = new ArrayWrapper([1, 2, 3]);
    const arr2 = new ArrayWrapper([4, 5, 6]);

    expect(arr1 + arr2).toEqual(21);
  });
});
