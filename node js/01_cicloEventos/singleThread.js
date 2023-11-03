//hilo unico

//por dejecto Node es un entorno de trabajo de un hilo unico

//request --> event loop (single thread) --> cosas como los console.log se quedan en este single thread
                                       //--> cosas como lecturas de archivos entran en el event loop y son pasados a una pila (stack) de operaciones, cuando estos terminan su ejecucion vuelven al event loop y luego son devueltos al usuario

//node puede emular el funcionamiento de multi thread con los (worker thread) https://nodejs.org/dist/latest-v18.x/docs/api/worker_threads.html



console.log("inicio"); //este consol entraria al event loop se ejecutaria y se devolveria al usuario 

setTimeout(() => { //los setTimeout al ser bloqueantes entrarian al event loop, luego se pasarian al stack de callbacks, luego espera los 3 seg para ejecutarse, vuelve al event loop, se ejecuta y se devuelve al usuario
    console.log("uno");
}, 3000);

setTimeout(() => { //si bien este setTimeout tiene tiempo de espera 0 no se ejecuta inmediatamente, sigue siendo un proceso bloqueante por lo cual tambien se va al stack de callback
    console.log("dos");
}, 0);

setTimeout(() => {
    console.log("tres");
}, 0);

console.log("fin");

//no te olvides q si bien tenes procesos bloqueantes el codigo en su totalidad es asincrono
//por mas q le ubieras dado 0 a todos los setTimeout el consol de "fin" se ejecuta antes, se podria decir q el "fin" tiene mayor prioridad xq este no pasa al stack de ejecuciones en espera 
//imaginate q es como entran los setTimeout, estos se los pasa al stack de espera, entra el consol "fin" y como este no tiene q esperar por nada (y sigue estando dentro del event loop) Node le da prioridad para q se ejecute y termine antes
//osea antes de meter devuelta algo del stack de esepera, se revisa q no haya nada ejecutandoce antes en el event loop

//si bien digo q es node en realidad es JS ya q node es JS del lado del servidor asi q lo correcto es decir q JS es signel thread


//call stack (pila de ejecucion)
//LIBUV API (donde van los procesos bloqueantes)
//event queue (cola de eventos q es a donde pasan los procesos bloqueantes una ves terminan su ejecucion por la cual tengan q esperar, luego se ve si hay algo ejecutandoce en el call stack y si no hay nada se mete en esta el primer proceso q este en el event queue)

//ejem:
const fs = require('fs');

console.log("inicio del programa");

fs.readFile("archivo.txt","utf8",(err,data)=>{
    if (err) {
        throw err;
    }

    console.log(data);
})

console.log("fin del programa");

//entra el "fs" (esto esta importando un modulo de JS por lo cual no es bloqueante) al call stack, se ejecuta el "fs" y sale del call stack

//pasa a la siguiente intruccion q es el consol "inicio..."

//el "inicio ..." entra al call stack, se ejecuta y sale

//pasa a la siguiente linea y ejecuta el sf.readFile (recorda q es una operacion asincrona por lo caul lo pasa a un segundo plano) , entonces la callback q es la q espera la lectura y almacenado del archivo se pasa a LIBUV API

//al pasar a LIBUV API, mientras en ella se fs.readFile se pone a leer el archivo.txt la call stack queda libre permitiendo q se ejecute otra operacion/intruccion/linea de codigo mientras el fs.readFile termina de leer

//mientras el fs.readFile lee, en el call stack entra el consl "fin...", este se ejecuta y sale del call stack

//luego cuando el fs.readFile termina de leer sale de LIBUV API y el callback (q seria la funcion q se ejecuta dentro del fs.readFile) entra en el event queue y dentro de esta se ejecuta el contenido de la callback (q seria el if ... console.log(data))

//ahora mientras todo esto va pasando el event loop de JS sigue ejecutando otras intrucciones

//por lo caul el callback q esta esperando en el event queue espera a ver si esta libre el call stack

//y si el call stack esta vacio entonces ahi si entre el callback dentro del call stack

//y dentro del call stack se muestra la data y luego sale


//DATO: EN EL CALL STACK ENTRAN TODAS LAS INSTRUCCIONES OSEA SE VAN APILANDO (NO ES Q SOLO ENTRA UNA SOLA OPERACION A LA VES)

// ejem: con setTimeout

console.log("inicio"); //1

setTimeout(() => { //2
    console.log("uno");
}, 3000);

setTimeout(() => { //3
    console.log("dos");
}, 0);

setTimeout(() => { //4
    console.log("tres");
}, 0);

console.log("fin"); //5

//call stack: (los q estan mas abajo son los q entraron antes al call stack)
//5
//4
//3
//2
//1

//el primer console.log se imprime y sale

//ahora el call stack me queda:
//5
//4
//3
//2

//el setTimeout (2) al ser bloqueante se va a gestionar en LIBUV API

//ahora el call stack me queda:
//5
//4
//3

//lo mismo con el setTimeout (3,4)

//ahora el call stack me queda:
//5

//y el LIBUV API queda asi:
//4
//3
//2

//se ejecuta 5 y el call stack queda vacio

//una ves pasado el tiempo de 2,3,4 (como 3 y 4 tienen menor tiempo q 2 estos pasan antes al event queue)

//LIBUV API queda asi:
//2

//EVENT QUEUE queda asi:
//4
//3 --> 3 pasa antes por llegar antes al LIBUV API (si bien tiene el mismo tiempo q 4)

//ahora 3 pasa a call stack se ejecuta y sale
//luego 4 hace lo mismo q 3
//cuando 2 termina su tiempo pasa a event queue y luego hace lo mismo q 3 y 4

// y debido a esto el resultado es --> 1,5,3,4,2