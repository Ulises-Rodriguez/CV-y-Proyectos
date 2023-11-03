import React, { useContext } from 'react';
import Contexto from '../contexto/Contexto'

function ProfesoraImg() {

    const {alumno} = useContext(Contexto);
    const idioma = alumno[3].idioma;
    const foto = `./idiomas/${alumno[idioma].foto}`

  return (
    <div className='profesora'>
        <h1>{alumno[idioma].boton1}</h1>
        <div>
            <img src={foto}></img>
        </div>
        <div className='nombre'>{alumno[idioma].nombre}</div>
    </div>
  )
}

export default ProfesoraImg;