function myStupidSolution(): (s: string) => number {
  function removeCharAtIndex(str: string, index: number) {
    return str.substring(0, index) + str.substring(index + 1);
  }

  // Missing last case
  return function LengthOfLongestSubstring(s: string): number {
    const obj: { [key: string]: number } = {};

    let char = "";
    for (let i = 0; i < s.length; i++) {
      for (let j = i; j < s.length; j++) {
        if (char.includes(s[j])) {
          continue;
        }

        char += s[j];
        obj[char] = 0;
      }
      char = "";
    }

    const sCloned = s;
    for (const key of Object.keys(obj)) {
      while (s.length > 0) {
        const index = s.indexOf(key);
        if (index !== -1) {
          s = removeCharAtIndex(s, index);
          obj[key]++;
        } else {
          break;
        }
      }

      s = sCloned;
    }

    let max = "";
    for (const key of Object.keys(obj)) {
      if (max.length < key.length && obj[key] > 0) {
        max = key;
      }
    }

    return max.length;
  }
}

// Sliding window. Ref: https://algo.monster/problems/sliding_window_maximum
function lengthOfLongestSubstring(s: string): number {
  let left = 0;
  let right = 0;
  const set = new Set<string>();

  let max = 0;
  while (right < s.length) {
    if (!set.has(s[right])) {
      set.add(s[right]);
      right++;
      max = Math.max(max, right - left);
    } else {
      set.delete(s[left]);
      left++;
    }
  }

  return max;
}
