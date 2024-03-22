// Prediction 1
// This will print "I was born in1980"
function myBirthYearFun(){
    console.log("I was born in " + 1980);
}
myBirthYearFun();

// Prediction 2
// This will print "I was born in1980"
// the parameter "birhtYearInput" was assigned "1980" by the call to the function on line 14
function myBirthYearFunc(birthYearInput){
    console.log("I was born in" + birthYearInput);
}
myBirthYearFunc(1980);

/*Prediction 3
This will print 30
console log 1 will print "Summing Numbers!"
console log 2 will print "num1 is 10"
console log 3 will print "num2 is 20"
console log 4 willprint the sum of 10 and 20 to give the answer 30
*/
function add(num1, num2){
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    console.log(sum);
}
add(10, 20);
