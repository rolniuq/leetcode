import { createHelloWorld } from "./hello_world";

describe("createHelloWorld", () => {
  it("should return 'Hello World' regardless of input", () => {
    const helloWorldFunction = createHelloWorld();

    // Test with no arguments
    expect(helloWorldFunction()).toBe("Hello World");

    // Test with one argument
    expect(helloWorldFunction("arg1")).toBe("Hello World");

    // Test with multiple arguments
    expect(helloWorldFunction("arg1", "arg2", "arg3")).toBe("Hello World");
  });
});
