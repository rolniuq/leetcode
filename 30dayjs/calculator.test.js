import { Calculator } from "./calculator";

describe("Calculator", () => {
  it("Run", () => {
    const c = new Calculator(2);
    const res = c.multiply(5).subtract(8).getResult();
    expect(res).toEqual(2);
  });
});
