import { sleep } from "./sleep";

describe("Sleep", () => {
  it("run", () => {
    const t = Date.now();
    sleep(100).then(() => expect(Date.now() - t).toBeGreaterThanOrEqual(100));
  });
});
