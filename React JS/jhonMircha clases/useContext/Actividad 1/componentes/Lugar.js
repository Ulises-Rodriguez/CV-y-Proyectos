import React, { useContext } from 'react'
import Contexto from '../contexto/Contexto';

function Lugar() {

    const {alumno} = useContext(Contexto);
    const idioma = alumno[3].idioma;

  return (
    <div className='lugar'>
        <h1>{alumno[idioma].boton2}</h1>
        <div className='textoLugar'>    
            {alumno[idioma].direccion}
        </div>
    </div>
  )
}

export default Lugar;