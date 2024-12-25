import { isEmpty } from "./is_tempty";

describe("IsEmpty", () => {
  it("Run", () => {
    const objEmpty = {};
    expect(isEmpty(objEmpty)).toBe(true);

    const objValid = { a: 1 };
    expect(isEmpty(objValid)).toBe(false);
  });
});
