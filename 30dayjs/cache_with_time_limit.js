export const TimeLimitedCache = function () {
  this.storage = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  const found = this.storage.has(key);
  if (found) clearTimeout(this.storage.get(key).ref);

  this.storage.set(key, {
    value: value,
    ref: setTimeout(() => this.storage.delete(key), duration),
  });

  return found;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  return this.storage.has(key) ? this.storage.get(key).value : -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return this.storage.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
