var likes = 3;
var likesElement = document.querySelector("#likes");

console.log(likesElement)

function add1() {
    likes++;
    likesElement.innerText = likes + "like(s)"
    console.log(likes)
}