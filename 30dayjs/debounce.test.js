import { debounce } from "./debounce";

describe("Debounce", () => {
  it("Run", () => {
    const fn = debounce(() => console.log("Hello"), 1000);
    fn();
    fn();
    fn();
    fn();
  });
});
