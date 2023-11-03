import './App.css';
import './miCss.css';
import React, { useState } from 'react';

const App = () => {
  const reyesGodos = [
    {
      nombre: "Ataúlfo",
      aficion: "comer toros sin pelar",
    }, {
      nombre: "Recesvinto",
      aficion: "leer a Hegel en arameo",
    }, {
      nombre: "Teodorico",
      aficion: "la cría del escarabajo en almíbar"
    }
  ]

  const [contador, setContador] = useState(0);
  const [mensaje, setMensaje] = useState("");

  const siguiente = () => {
    setContador(contador + 1); //tener en cuanta q la primera actualizacion se realiza al final de los {} por lo cual contador cuando sea llamado en setMensaje, contador sera = 0
    if ((contador + 1) >= reyesGodos.length) {
      setContador(0);
    }

    setMensaje(<h2>La aficion principal de <span className='rojo'>{reyesGodos[contador].nombre}</span> es <span className='verde'>{reyesGodos[contador].aficion}</span></h2>) //aca escribe con {} a pesar de q esta fuera del return debido a q usa las etiquetas
  };

  return (
    <>
      {/* Esto es un comentario dentro del return*/}
      {/* Crear un <div> y un <button> */}
      <button onClick={siguiente}>Ver Siguiente</button>
      <div className='contenedorInfo'>{mensaje}</div>
    </>
  )
}
export default App;