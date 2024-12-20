export const expect = function(val) {
  return {
    toBe(expect) {
      if (expect === val) {
        return true
      }

      throw new Error("Not Equal")
    },
    notToBe(expect) {
      if (expect !== val) {
        return true
      }

      throw new Error("Equal")
    }
  }
}
