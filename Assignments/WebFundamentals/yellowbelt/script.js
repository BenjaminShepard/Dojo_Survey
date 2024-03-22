// remove the donate button
function hide(element){
    element.remove();
}

// pepper pets
var pets = 0
var petsElement = document.querySelector("#pets")

console.log(petsElement)

function pepperadd1() {
    pets++;
    petsElement.innerText = pets + "Petting(s)"
    console.log(pets)
}

// bruce pets
var pets2 = 0
var pets2Element = document.querySelector("#pets2")

console.log(pets2Element)

function bruceadd1() {
    pets2++;
    pets2Element.innerText = pets2 + "Petting(s)"
    console.log(pets2)
}

// oscar pets
var pets3 = 0
var pets3Element = document.querySelector("#pets3")

console.log(pets3Element)

function oscaradd1() {
    pets3++;
    pets3Element.innerText = pets3 + "Petting(s)"
    console.log(pets3)
}

function selectDog(element) {
    alert("Your are looking for a " + element.value);
}