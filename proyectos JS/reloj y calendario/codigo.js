const añadirCero = (num)=>{
    if (num.toString().length < 2) {
        return "0".concat(num);
    }
    else{
        return num;
    }
};


const actualizarHorario = ()=>{
    let horario = new Date();
    
    let hora = añadirCero(horario.getHours());
    let minutos = añadirCero(horario.getMinutes());
    let segundos = añadirCero(horario.getSeconds());

    document.querySelector(".hora").textContent = `${hora}:`;
    document.querySelector(".minutos").textContent = `${minutos}:`;
    document.querySelector(".segundos").textContent = `${segundos}`;
};

const obtenerAño = ()=>{
    let año = new Date();

    document.getElementById("año").textContent = año.getFullYear();
};

const mesArray = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

const obtenerMes = ()=>{
    let mes = new Date();

    if (mes.getMonth() + 1 == 0) {
        document.getElementById("mes").textContent = mesArray[0];
    }
    else if (mes.getMonth() + 1 == 2) {
        document.getElementById("mes").textContent = mesArray[1];
    }
    else if (mes.getMonth() + 1 == 3) {
        document.getElementById("mes").textContent = mesArray[2];
    }
    else if (mes.getMonth() + 1 == 4) {
        document.getElementById("mes").textContent = mesArray[3];
    }
    else if (mes.getMonth() + 1 == 5) {
        document.getElementById("mes").textContent = mesArray[4];
    }
    else if (mes.getMonth() + 1 == 6) {
        document.getElementById("mes").textContent = mesArray[5];
    }
    else if (mes.getMonth() + 1 == 7) {
        document.getElementById("mes").textContent = mesArray[6];
    }
    else if (mes.getMonth() + 1 == 8) {
        document.getElementById("mes").textContent = mesArray[7];
    }
    else if (mes.getMonth() + 1 == 9) {
        document.getElementById("mes").textContent = mesArray[8];
    }
    else if (mes.getMonth() + 1 == 10) {
        document.getElementById("mes").textContent = mesArray[9];
    }
    else if (mes.getMonth() + 1 == 11) {
        document.getElementById("mes").textContent = mesArray[10];
    }
    else{
        document.getElementById("mes").textContent = mesArray[11];
    }
};

const obtenerDia = ()=>{
    let dia = new Date();

    if (dia.getDay() == 0) {
        let domingo = document.getElementById("domingo"); 

        domingo.style.border = "solid #000 2px";
        domingo.style.backgroundColor = "#00f";
    }
    else if (dia.getDay() == 1) {
        let lunes = document.getElementById("lunes");

        lunes.style.border = "solid #000 2px";
        lunes.style.backgroundColor = "#00f";
    }
    else if (dia.getDay() == 2) {
        let martes = document.getElementById("martes");

        martes.style.border = "solid #000 2px";
        martes.style.backgroundColor = "#00f";
    }
    else if (dia.getDay() == 3) {
        let miercoles = document.getElementById("miercoles"); 

        miercoles.style.border = "solid #000 2px";
        miercoles.style.backgroundColor = "#00f";
    }
    else if (dia.getDay() == 4) {
        let jueves = document.getElementById("jueves"); 

        jueves.style.border = "solid #000 2px";
        jueves.style.backgroundColor = "#00f";
    }
    else if (dia.getDay() == 5) {
        let viernes = document.getElementById("viernes");

        viernes.style.border = "solid #000 2px";
        viernes.style.backgroundColor = "#00f";
    }
    else{
        let sabado = document.getElementById("sabado"); 
        
        sabado.style.border = "solid #000 2px";
        sabado.style.backgroundColor = "#00f";
    }
};

const cantidadDias = ()=>{
    let mesLength = new Date();

    if ((mesLength.getDate()) == 31) { //casos para meses con 31 dias
        crearDias(31);
    }
    else if ((mesLength.getDate()) == 28) { //casos para meses con 28 dias
        crearDias(28);
    }
    else{ //resto de los meses q tienen 30 dias
        crearDias(30);
    }
};

const crearDias = numDias=>{
    let diaAPintar = new Date().getDate();

    const fechaContainer = document.getElementById("fecha-container");

    for (let i = 1; i <= numDias + 1; i++) {
        const dia = document.createElement("div");
        dia.classList.add("fecha");

        dia.innerHTML = i;

        if (i == diaAPintar) {
            dia.style.backgroundColor = "#0f0";
            fechaContainer.appendChild(dia);    
        }
        else{
            fechaContainer.appendChild(dia);
        }
    }
};

actualizarHorario();
setInterval(actualizarHorario,1000);

obtenerAño();
obtenerMes();
obtenerDia();
cantidadDias();