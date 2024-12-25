import { chunk } from "./chunk_array";

describe("ChunkArray", () => {
  it("Run", () => {
    const nums = [1, 2, 3, 4, 5, 6, 7];
    const chunks = chunk(nums, 3);
    expect(chunks.length).toEqual(3);
  });
});
