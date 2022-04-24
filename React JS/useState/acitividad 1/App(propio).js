import './App.css';
import './miCss.css';
import React,{useState} from 'react';

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

  const [contador,setContador] = useState(0);
  const [nombre,setNombre] = useState(reyesGodos[0].nombre);
  const [aficion,setAficion] = useState(reyesGodos[0].aficion);

  const siguiente = ()=>{
    setContador(contador + 1);
    setNombre(reyesGodos[contador].nombre);
    setAficion(reyesGodos[contador].aficion);
  };

  if (contador === 3) {
    setContador(0);
  };

  return (
    <>
      {/* Esto es un comentario dentro del return*/}
      {/* Crear un <div> y un <button> */}
      <button onClick={siguiente}>Ver Siguiente</button>
      <div className='contenedorInfo'>
        La aficion principal de <b className='reyNombre'>{nombre}</b> es <b className='reyAficion'>{aficion}</b>
      </div>
    </>
  )
}
export default App;