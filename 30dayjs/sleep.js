/**
 * @param {number} millis
 * @return {Promise}
 */
export async function sleep(millis) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      return resolve(millis);
    }, millis);
  });
}
