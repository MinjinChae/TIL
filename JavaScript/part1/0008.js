var x = 5; //숫자형
var y = 'five' // 문자형
var isTrue = true; // 불린형
var empty = null; // null 빈 값
var nothing // undefined 존재하지 않는 값
var sym = Symbol('me'); // Symbol 심볼..? 

var item = {
    price: 5000,
    count: 10
}; // 객체(object) 이게뭐여
 
var fruits = ['apple', 'orange', 'kiwi']; // 배열(Array)
var addFruit = function (fruit) {
  fruits.push(fruit);
} // 함수(function)
addFruit('watermelon');
console.log(fruits);
