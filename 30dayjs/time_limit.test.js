import { timeLimit } from "./time_limit";

describe("timeLimit", () => {
  it("Run", async () => {
    const fn = timeLimit(() => new Promise((res) => setTimeout(res, 100)), 50);
    await expect(fn()).rejects.toThrow("Time Limit Exceeded");
  });

  it("Run", async () => {
    const fn = timeLimit(() => new Promise((res) => setTimeout(res, 50)), 100);
    await expect(fn()).resolves.toBeUndefined();
  });
});
