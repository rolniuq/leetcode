function maxiumumWealth(accounts: number[][]): number {
  let max = 0;
  for (let i = 0; i < accounts.length; i++) {
    const total = accounts[i].reduce((a, b) => a + b, 0);
    if (total > max) {
      max = total;
    }
  }

  return max;
}
