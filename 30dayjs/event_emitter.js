export class EventEmitter {
  constructor() {
    this.emitter = {};
  }

  /**
   * @param {string} eventName
   * @param {Function} callback
   * @return {Object}
   */
  subscribe(eventName, callback) {
    this.emitter[eventName] = this.emitter[eventName] || [];
    this.emitter[eventName].push(callback);

    return {
      unsubscribe: () => {
        if (!this.emitter[eventName]) {
          return;
        }

        this.emitter[eventName].pop();
      },
    };
  }

  /**
   * @param {string} eventName
   * @param {Array} args
   * @return {Array}
   */
  emit(eventName, args = []) {
    const fns = this.emitter[eventName];
    if (!fns) {
      return [];
    }

    return fns.map((fn) => fn(args));
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
