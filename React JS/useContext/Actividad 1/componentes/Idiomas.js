import React, { useContext } from 'react'
import Contexto from '../contexto/Contexto'
import Provider from '../contexto/Provider';

function Idiomas() {

  const {alumno} = useContext(Contexto);
  const {setAlumno} = useContext(Contexto);


  const sustitucion = (posicion)=>{
    setAlumno(
      alumno.map((dato, indice) =>
        indice == 3 ? { ...dato, idioma: posicion }
          : { ...dato }
      )
    );
  }

  const cambio1 = ()=>{
    sustitucion(0);
  }

  const cambio2 = () => {
    sustitucion(1);
  }

  const cambio3 = () => {
    sustitucion(2);
  }

  return (
    <>
      <div className='banderas'>
        <div className='bandera' onClick={cambio1}><img src='./idiomas/spain.jpg'></img></div>
        <div className='bandera' onClick={cambio2}><img src="./idiomas/uk.png"></img></div>
        <div className='bandera' onClick={cambio3}><img src="./idiomas/francia.png"></img></div>
      </div>
    </>
  )
}

export default Idiomas;