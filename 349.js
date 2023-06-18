const nums = [3,2,1,4];

if (nums.length < 3) {
    console.log(-1);
}
let iMax = nums.indexOf(Math.max(...nums))
let iMin = nums.indexOf(Math.min(...nums))
//splice() edits the orig array
nums.splice(iMax, 1);
nums.splice(iMin, 1);
//random item from an array
answer = nums[Math.floor(Math.random()*nums.length)]
console.log(answer)