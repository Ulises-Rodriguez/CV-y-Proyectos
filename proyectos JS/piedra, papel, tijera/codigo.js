//idea a futuro hacer algo para q no se pueda dar devuleta a los otros botones hasta q se alla apretado el boton de nuevo juego
//idea hacer algo como añadir clases a los botonos cosa de q solo se le pueda dar al boton q tenga cierta clase el cual le permita o evita q los otros botones se apreten

const counterUser = document.getElementById("user-counter");
const counterPC = document.getElementById("pc-counter");

const piedraUser = document.getElementById("piedraUser");
const papelUser = document.getElementById("papelUser");
const tijeraUser = document.getElementById("tijeraUser");

const newGame = document.getElementById("againButton");

let elementNum = 0;

piedraUser.addEventListener("click",()=>{
    elementNum = piedraUser.value;
    compare();
});

papelUser.addEventListener("click",()=>{
    elementNum = papelUser.value;
    compare();
});

tijeraUser.addEventListener("click",()=>{
    elementNum = tijeraUser.value;
    compare();
});

const choiceUser = (element)=>{
    if (element == 1) {
        return parseInt(piedraUser.value);
    }
    else if (element == 2) {
        return parseInt(papelUser.value);
    }
    else{
        return parseInt(tijeraUser.value);
    }
};

const userCounter = (numUser)=>{
    counterUser.textContent = parseInt(numUser) + 1;
};

const pcCounter = (numPC)=>{
    counterPC.textContent = parseInt(numPC) + 1;
};

const compare = ()=>{
    let pcChoice = parseInt(Math.random() * 3 + 1);
    let userChoice = choiceUser(elementNum);

    if (pcChoice == 1) {
        const piedraPC = document.getElementById("piedraPC");
        
        if (userChoice === 1) {
            alert("el juego termino en empate, inicie un juego nuevo");
            piedraPC.style.border = "solid 4px #fb0";
            piedraUser.style.border = "solid 4px #fb0";
        }
        else if (userChoice === 2) {
            alert("tu contrincante elijio piedra, por lo cual has gando");
            piedraPC.style.border = "solid 4px #f00";
            papelUser.style.border = "solid 4px #0f0";
            userCounter(counterUser.textContent);
        }
        else if (userChoice === 3) {
            alert("tu contrincante elijio piedra, por lo cual has perdido");
            piedraPC.style.border = "solid 4px #0f0";
            tijeraUser.style.border = "solid 4px #f00";
            pcCounter(counterPC.textContent);
        }
    }
    else if (pcChoice == 2) {
        const papelPC = document.getElementById("papelPC");
        
        if (userChoice == 1) {
            alert("tu contrincante elijio papel, por lo cual has perdido");
            papelPC.style.border = "solid 4px #0f0";
            piedraUser.style.border = "solid 4px #f00";
            pcCounter(counterUser.textContent);
        }
        else if (userChoice == 2) {
            alert("el juego termino en empate, inicie un juego nuevo");
            papelPC.style.border = "solid 4px #fb0";
            papelUser.style.border = "solid 4px #fb0";
        }
        else if (userChoice === 3) {
            alert("tu contrincante elijio papel, por lo cual has ganado");
            papelPC.style.border = "solid 4px #f00";
            tijeraUser.style.border = "solid 4px #0f0";
            userCounter(counterPC.textContent);
        }
    }
    else{
        const tijeraPC = document.getElementById("tijeraPC");
        
        if (userChoice === 1) {
            alert("tu contrincante elijio tijera, por lo cual has ganado");
            tijeraPC.style.border = "solid 4px #f00";
            piedraUser.style.border = "solid 4px #0f0";
            userCounter(counterUser.textContent);
        }
        else if (userChoice === 2) {
            alert("tu contrincante elijio tijera, por lo cual has perdido");
            tijeraPC.style.border = "solid 4px #0f0";
            papelUser.style.border = "solid 4px #f00";
            pcCounter(counterPC.textContent);

        }
        else if (userChoice === 3) {
            alert("el juego termino en empate, inicie un juego nuevo");
            tijeraPC.style.border = "solid 4px #fb0";
            tijeraUser.style.border = "solid 4px #fb0";
        }
    }
};

newGame.addEventListener("click",()=>{
    reset();
});

const reset = ()=>{
    piedraPC.style.border = "solid 4px #000";
    piedraUser.style.border = "solid 4px #000";
    papelPC.style.border = "solid 4px #000";
    papelUser.style.border = "solid 4px #000";
    tijeraPC.style.border = "solid 4px #000";
    tijeraUser.style.border = "solid 4px #000";
};