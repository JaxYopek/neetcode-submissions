class MinStack {
    constructor() {
        this.stack = new Array();
        this.minStack = new Array();
        this.minStack.push(Infinity);
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (val < this.minStack.at(-1)){
            this.minStack.push(val);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        const val = this.stack.pop();
        if (val === this.minStack.at(-1)){
            this.minStack.pop();
        }
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack.at(-1);
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack.at(-1);
    }
}
