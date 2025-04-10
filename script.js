function showMessage() { 
    alert("Hello! Welcome to my website."); 
}
function changeBgColor() { 
    document.body.style.backgroundColor = "lightblue"; 
}
function displayGreeting() {
    let name = document.getElementById("nameInput").value.trim(); // Get input and remove spaces

    if (name === "") {
        document.getElementById("greetingMessage").textContent = "Please enter your name!";
    } else {
        document.getElementById("greetingMessage").textContent = "Hello, " + name + "! Welcome to my webpage!";
    }
}
function changeByColorUser() {
    let name = document.getElementById("colorinput").ariaValueMax;
    document.getElementById("colorUser"),innerHTML = "Hello, " + name + "! Welcome to my website" ;
}
function changeBgColor() {
    const colors = ["lightblue", "lightgreen", "pink", "yellow", "purple", "orange"];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = randomColor;
}
function checkAge() {
    let age = DocumentFragment.getElementById("ageInput").value;
    if(age>= 18){
        alert("You're an adult!");
    }else{
        alert("You're still a kid!")
    }
}
function zoomIn(img) {
    img.style.transform = "scale(1.2";
}
function zoomOut(img){
    img.style.transform = "scale(1)";
}