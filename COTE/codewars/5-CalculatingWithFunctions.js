//https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/solutions/javascript
//[ ]

function executeValue(callback, value){
   return typeof callback === 'function' ? callback(value) : value;
 }
 function zero(callback) {
   let value=0
   return executeValue(callback, value)
 }
 function one(callback) {
   let value=1
   return executeValue(callback, value)
 }
 function two(callback) {
   let value=2
   return executeValue(callback, value)
 }
 function three(callback) {
   let value=3
   return executeValue(callback, value)
 }
 function four(callback) {
   let value=4
   return executeValue(callback, value)
 }
 function five(callback) {
   let value=5
   return executeValue(callback, value)
 }
 function six(callback) {
   let value=6
   return executeValue(callback, value)
 }
 function seven(callback) {
   let value=7
   return executeValue(callback, value)
 }
 function eight(callback) {
   let value=8
   return executeValue(callback, value)
 }
 function nine(callback) {
   let value=9
   return executeValue(callback, value)
 }
 
 function plus(a) {
   return function(b){
     return a+b
   }
 }
 function minus(a) {
   return function(b){
     return b-a
   }
 }
 function times(a) {
   return function(b){
     return b*a
   }
 }
 function dividedBy(a) {
   return function(b){
     return Math.floor(b/a)
   }
 }



//1
var n = function(digit) {
   return function(op) {
     return op ? op(digit) : digit;
   }
 };
 var zero = n(0);
 var one = n(1);
 var two = n(2);
 var three = n(3);
 var four = n(4);
 var five = n(5);
 var six = n(6);
 var seven = n(7);
 var eight = n(8);
 var nine = n(9);
 
 function plus(r) { return function(l) { return l + r; }; }
 function minus(r) { return function(l) { return l - r; }; }
 function times(r) { return function(l) { return l * r; }; }
 function dividedBy(r) { return function(l) { return l / r; }; }

//2
function zero(func)   { return func ? func(0) : 0; };
function one(func)    { return func ? func(1) : 1; };
function two(func)    { return func ? func(2) : 2; };
function three(func)  { return func ? func(3) : 3; };
function four(func)   { return func ? func(4) : 4; };
function five(func)   { return func ? func(5) : 5; };
function six(func)    { return func ? func(6) : 6; };
function seven(func)  { return func ? func(7) : 7; };
function eight(func)  { return func ? func(8) : 8; };
function nine(func)   { return func ? func(9) : 9; };

function plus( b )      { return function( a ) { return a + b; }; };
function minus( b )     { return function( a ) { return a - b; }; };
function times( b )     { return function( a ) { return a * b; }; };
function dividedBy( b ) { return function( a ) { return a / b; }; };