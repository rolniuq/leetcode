/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
export const compactObject = function (obj) {
  if (!obj) return null;
  if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
  if ("object" !== typeof obj) return obj;

  const newObj = {};

  for (const key in obj) {
    const value = compactObject(obj[key]);
    if (value) newObj[key] = value;
  }

  return newObj;
};

console.log(compactObject([null, 0, false, 1]));
