class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = new Array();
        if (s.length <= 1){
            return false;
        }
        for (let i = 0; i < s.length; i++){
            if (s[i] === "("){
                stack.push(s[i]);
            }
            else if (s[i] === "["){
                stack.push(s[i]);
            }
            else if (s[i] === "{"){
                stack.push(s[i]);
            }
            else if (s[i] === ")"){
                let top = stack.pop();
                if (top !== "(" ){
                    return false;
                }
            }
            else if (s[i] === "]"){
                let top = stack.pop();
                if (top !== "[" ){
                    return false;
                }
            }
            else if (s[i] === "}"){
                let top = stack.pop();
                if (top !== "{" ){
                    return false;
                }
            }
            

        }
        return true;
    }
}
