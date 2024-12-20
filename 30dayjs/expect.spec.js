import { expect as myExpect } from "./expect";

describe("expect", () => {
  it("toBe returns true when values are equal", () => {
    myExpect(1).toBe(1);
  });

  it("toBe throws an error when values are not equal", () => {
    expect(() => myExpect(1).toBe(2)).toThrow("Not Equal");
  });

  it("notToBe returns true when values are not equal", () => {
    myExpect(1).notToBe(2);
  });

  it("notToBe throws an error when values are equal", () => {
    expect(() => myExpect(1).notToBe(1)).toThrow("Equal");
  });

  it("toBe works with numbers", () => {
    myExpect(1).toBe(1);
  });

  it("toBe works with strings", () => {
    myExpect("hello").toBe("hello");
  });

  it("toBe works with booleans", () => {
    myExpect(true).toBe(true);
  });

  it("notToBe works with numbers", () => {
    myExpect(1).notToBe(2);
  });

  it("notToBe works with strings", () => {
    myExpect("hello").notToBe("world");
  });

  it("notToBe works with booleans", () => {
    myExpect(true).notToBe(false);
  });
});
