import React, { useState, useEffect } from "react";
import Hora from "./Hora";

function RelojUseEffect() {

    const [hora, sethora] = useState(new Date().toLocaleTimeString());
    const [visible, setVisible] = useState(false); //en principio false xq el reloj no se ve hasat q le damos al boton de iniciar

    useEffect(() => {
        let temporizador;

        if (visible) {
            temporizador = setInterval(() => {
                sethora(new Date().toLocaleTimeString());
            }, 1000)
        } else {
            clearInterval(temporizador);
        }
        return () => {
            console.log("Fase de Desmontaje");
            clearInterval(temporizador);
        }
    }, [visible])

    return (
        <>
            <h2>Reloj con Hooks</h2>
            {visible && <Hora hora={hora} />}
            <button onClick={() => setVisible(true)}>Iniciar</button>
            {/* el onClick={() => setvisible(true)} asi xq se recive algo mas q solo la funcion, si yo no tuviera q pasarle nada a setVisible entonces no haria falta la funcion flecha en el evento*/}
            <button onClick={() => setVisible(false)}>Detener</button>
        </>
    )
}

export default RelojUseEffect;