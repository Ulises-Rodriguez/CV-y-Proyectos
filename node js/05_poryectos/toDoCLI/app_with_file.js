//el modulo file system es para q cada ves q el usuario crea una tarea esta se agregue a un archivo de texto 
//fijate q no importamos el readFile y writeFile comun (asincrono) sino q importamos el q corre de forma sincrona
//imagina q estan varios usuarios ejecutando el mismo archivo de texto, podriamos tener conflictos de q un usuario inserta algo antes q otro y q por ejem a 2 les de el mismo numero (pensalo como si fuera una cuenta bancaria compartida, vos no queres permitir q se hagan 2 extracciones al mismo tiempo ya q podria no haber fondos suficientes para las 2)
import {readFileSync, writeFileSync} from 'fs';
import { createInterface } from "readline";
import chalk from "chalk";

const tasks = [];
//1 creamos la variable donde vamos a guardar la referncia al archivo de texto (recorda q si no esta creado en la primera lectura readFile lo crea, wirte tambien)
const DB_FILE = "tasks.txt"

const rl = createInterface({
    input: process.stdin,
    output: process.stdout
})

const displayMenu = () => {
    console.log(chalk.yellow.bold("📝 listaDeTareas 📝"));
    console.log("1. Agregar tarea");
    console.log("2. Listar tareas");
    console.log("3. Completar tarea");
    console.log("4. Salir");
}

//2 ahora vamos a crear un funcion q se encarguen de la lectura
const loadTasks = ()=>{
    //2.1 usamos un try catch para manejar el error en caso de q no se encuentre el archivo o no pueda ser creado
    try {
        //2.2 creamos la variable data q es donde se va a guardar la lectura del archivo
        const data = readFileSync(DB_FILE,"utf-8");
        //2.3 lines se va a encargar de ir leyendo linea a linea, por cada objeto de la tarea vamos a agregar un salto de linea
        //como lo q nos llega en data es un string (array de caracteres para ser mas exacto) con split lo q hacemos es al string q nos llega dividirlo en los elementos de un array (lines) cada ves q encuentre el salto de linea
        const lines = data.split("\n");

        //esta linea es mas precucion q otra cosa (cuendo iniciamos la app el array siempre deberia estar vacio pero bueno no pasa nada por tomar precauciones)
        tasks.length = 0;

        //2.4 agregamos a tasks las tareas q tengamos de lines
        lines.forEach(line=> {
            //este if para asegurarnos por si se escapa algun espacio en blanco y con trim removemos los espacios en blacno
            if (line.trim() !== "") {
                //este | lo usamos para q en el txt se dividan las tareas y q separa cual es el contenido de task y completed
                //podrias guardarlos como objetos pero tendiras q convertirlos a formato JS
                //otra opcion seria con fetch y un json y tabajar con async y await
                const [task,completed] = line.split("|");
                //agregamos las tareas de esta manera para q asi el valor de completed se guarda como un bool ya q sino nos va a llegar como "false" o "true" (string)
                tasks.push({task,completed : completed === true});
                
            }

            //la otras seria asi pero tendrias q modificar el completeTask para q analice con string en ves de bool
            // lines.forEach(line=> tasks.push(line))
        })

        console.log(chalk.green.bold("Las tareas se cargaron con exito desde DB"));
    } catch (error) {
        console.log(chalk.red.bold("No hay tareas por hacer"));
    }
}

//3 una funcion q permita la escritura en el archivo
const saveTask = ()=>{
    //este es el pip q usamos en para dividir las tareas en el txt
    const data = tasks.map(task => `${task.task}|${task.completed}`).join("\n");
    writeFileSync(DB_FILE,data,"utf-8");
    console.log("Tarea agregada con exito a la DB")
}

//4 modificamos addTask para q ahora la tarea añadida al array tasks estas se añadan al txt
const addTask = () => {
    rl.question(chalk.bgBlueBright("Escribe la tarea: "), (task) => {
        tasks.push({
            task,
            completed: false
        });

        console.log(chalk.greenBright("La tarea se agrego con exito!"));

        console.log(tasks);

        //4.1 ejecutamos la fun de salvar la tarea
        //y como saveTask trabaja de forma sincrona hasta q saveTask no termine no va a mostrarse el menu y las opciones 
        saveTask();

        displayMenu();
        choseOption();
    })
}

//como el array tasks es donde se van a guardar tanto las tareas nuevas como las q estan en el txt no hace falta modificiar nada de la listTask (se podria hacer una apertura del txt pero seria inecesario ya q lo hacemos en otra fun)
const listTasks = () => {
    console.log(chalk.bgCyanBright("\nTareas por hacer\n"));

    !tasks.length ? console.log(chalk.bgRedBright.bold("No hay tareas pendientes")) : tasks.forEach((task, index) => {
        let status = task.completed ? "✔️" : "❌";
        
        if (task.completed) {
            console.log(chalk.bgGreenBright.bold(`${index + 1}. ${status} - ${task.task}`));
        } else {
            console.log(chalk.bgRedBright.bold(`${index + 1}. ${status} - ${task.task}`));
        }
    });

    displayMenu();
    choseOption();
}


//5 aca tambien necesitamos modificar la fun ya q cuando modifiquemos el campor de la tarea completada de false a true tenemos q guardar el cambio
const completedTask = ()=>{
    rl.question(chalk.bgBlueBright.bold("Ingresa el numero de la tarea completada: "),(taskNum)=>{
        
        const index = parseInt(taskNum) - 1;

        if (index >= 0 && index < tasks.length) {
            tasks[index].completed = true;
            //5.1 ejecutamos saveTask para guardar el cambio de la tarea
            saveTask();
            console.log(chalk.green.bold("Tarea completada con exito ✔️"));
        } else {
            console.log(chalk.red.bold("Numero de Tarea invalido"));
        }

        displayMenu();
        choseOption();
    })
}

const choseOption = () => {
    rl.question("Elige una opcion, escribe el numero de tu opcion: ", (choice) => {
        switch (choice) {
            case "1":
                addTask();
                break;
            case "2":
                listTasks();
                break;
            case "3":
                completedTask();
                break;
            case "4":
                console.log(chalk.greenBright("Saliendo del manejador de tareas"));
                rl.close();
                break;

            default:
                console.log(chalk.redBright("Esa opcion no esta disponible"));
                displayMenu();
                choseOption();
                break;
        }
    });
}

//antes de mostrar el menu y las opciones cargamos el txt
loadTasks();
displayMenu();
choseOption();
