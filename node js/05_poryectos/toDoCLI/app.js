//1_ npm init -y para crear el package.json
//2_ si usas la importacion de modulos de ES6 tenes q agregar al package.json --> "type" : "module"

//el modulo readline de node nos provee una interface para la lectura de datos
import { createInterface } from "readline";
//chalk le pone colores a la terminal para q se vea mas lindo
import chalk from "chalk";

const tasks = [];

//rl es para q te  
//Este módulo resume los objetos de salida (output) estándar del proceso y de entrada (input) estándar del proceso. El módulo Readline facilita la entrada y lectura de la salida proporcionada por el usuario. 

//el método createInterface() toma dos argumentos. El primer argumento será para la entrada estándar y el segundo será para leer la salida estándar. 
const rl = createInterface({
    //process es un objeto q nos da info y control sobre el actual proceso de node.js
    input: process.stdin,
    output: process.stdout
})

//1 como su nombre indica muestra un menu en consola
const displayMenu = () => {
    console.log(chalk.yellow.bold("📝 listaDeTareas 📝"));
    console.log("1. Agregar tarea");
    console.log("2. Listar tareas");
    console.log("3. Completar tarea");
    console.log("4. Salir");
}

//3 funcion crear tarea
const addTask = () => {
    //3.1 usamos el metodo question para preguntar la tarea 
    rl.question(chalk.bgBlueBright("Escribe la tarea: "), (task) => {
        //3.2 en la funcion callback de question agregamos la tarea al array global 
        //esta la agregamos en formato de objeto para asi no solo agregar la tarea sino la opcion de tarea completada q vamos a usar en la funcion completeTask
        tasks.push({
            task, //recorda q es un short hand q podes usar si la clave y valor tiene el mismo nombre
            complete: false
        });

        //3.3 tiramos un mensaje para indicar q la tarea se agrego
        console.log(chalk.greenBright("La tarea se agrego con exito!"));

        console.log(tasks);

        //3.4 volvemos a mostrar el menu y choiceOption para q puede elegir otra opcion
        displayMenu();
        choseOption();

        //DATO: cada ves q se reinicia o gurdas los cambios corriendo el programa con nodemon la aplicacion hace q la variable global tareas se reinicie y pierda lo q tenia guardado
        //esto lo ideal q lo mandes a un .json o .js o una base de datos para q se guarde
    })

}

//4 listar tareas
const listTasks = () => {
    //4.1 imprimimos en consola el mensaje de tareas por hacer
    console.log(chalk.bgCyanBright("\nTareas por hacer\n"));

    //4.2 analizamos los casos para lista vacia o con tareas 
    //usando el array tasks y foreach vamos a listar todas las tareas
    !tasks.length ? console.log(chalk.bgRedBright.bold("No hay tareas pendientes")) : tasks.forEach((task, index) => {
        //4.3 en la variable status para mostrar los emogis (en ves de mostrar true o false para q se vea mas lindo)
        let status = task.complete ? "✔️" : "❌";
        //4.4 con este consol mostramos
        //con index --> el numero de la tarea (le sumamos 1 para q no muestre tarea 0)
        //con status --> mostramos si el emogi de tarea completada o no
        //con task.task --> el nombre de la tarea
        if (task.complete) {
            //4.5 este if else para mostrar en diferente color si la tarea esta terminada o no
            console.log(chalk.bgGreenBright.bold(`${index + 1}. ${status} - ${task.task}`));
        } else {
            console.log(chalk.bgRedBright.bold(`${index + 1}. ${status} - ${task.task}`));
        }
    });
    //4.6 mostramos el menu y opciones para q el usuario pueda seguir interactuando
    displayMenu();
    choseOption();
}

//5 fun para completar las tareas
const completeTask = ()=>{
    //5.1 hacemos una pregunta  para q el usuario indique q tarea a terminado
    //en la callback hacemos la logica
    rl.question(chalk.bgBlueBright.bold("Ingresa el numero de la tarea completada: "),(taskNum)=>{
        //5.2 en la variable index guardamos el numero q ingrese el usuario convertido a numero (ya q nos llega como string)
        //y le restamos 1 ya q cuando mostramos las tareas estas arrancan desde 1 no desde 0
        const index = parseInt(taskNum) - 1;

        //5.3 este condicional para capturar los casos en el q el usuario ingrese el numero de alguna tarea q no existe o ingrese numeros negativos
        if (index >= 0 && index < tasks.length) {
            //si el numero ingresado es correcto modificamos su valor complete a true
            tasks[index].complete = true;
            console.log(chalk.green.bold("Tarea completada con exito ✔️"));
        } else {
            console.log(chalk.red.bold("Numero de Tarea invalido"));
        }

        //5.4 mostramos el menu y las opciones
        displayMenu();
        choseOption();
    })

}

//2 funcion para q el usuario interactue con la consola
const choseOption = () => {
    rl.question("Elige una opcion, escribe el numero de tu opcion: ", (choice) => {
        switch (choice) {
            case "1":
                //3 dentro poner la logica para q se ejectuten las diferentes opciones
                addTask();
                break;
            case "2":
                listTasks();
                break;
            case "3":
                completeTask();
                break;
            case "4":
                console.log(chalk.greenBright("Saliendo del manejador de tareas"));
                rl.close(); //este metodo cierra la terminal devolviendote el control de esta

                //DATO: si ejectutas el programa con nodemon la opcion 4 no termina de funcionar correctamente ya q es como q se reinicia
                //si lo corres con node app.js si funciona bien 
                break;

            default:
                console.log(chalk.redBright("Esa opcion no esta disponible"));
                //aca tenes q hacer recusividad ya q al poner una opcion invalida tenes q mostrarle devuelta el menu y las opcion
                displayMenu();
                choseOption();
                break;
        }
    }); //el metodo question permite hacer una pregunta e interacctuar con la terminal
}

displayMenu();
choseOption();