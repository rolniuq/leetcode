import { argsLength } from "./args_length";

describe("argsLength", () => {
  it("Run", () => {
    expect(argsLength(1, 2, 3)).toEqual(3);
  });
});
