import React, { useContext, useState } from 'react'
import Contexto from '../contexto/Contexto';
import Lugar from './Lugar';
import ProfesoraImg from './ProfesoraImg';

function Info() {
    const {alumno} = useContext(Contexto);
    //console.log(alumno);

    const idioma = alumno[3].idioma; //xq 3? --> en provider q es donde definimos nuesntrom array es la posicion donde esta idioma q tiene guardado elo valor 0

    const [ocultar1,setOcultar1] = useState(false);
    const [ocultar2, setOcultar2] = useState(false);

    const mostrar1 = ()=>{
        setOcultar1(!ocultar1);
        setOcultar2(false);
    }
    
    const mostrar2 = () => {
        setOcultar2(!ocultar2);
        setOcultar1(false);
    }

  return (
    <>
        <h1>{alumno[idioma].titulo}</h1>
        <h2>{alumno[idioma].texto}</h2>
        <div className='botones'>
            <button onClick={mostrar1}>{alumno[idioma].boton1}</button>
            <button onClick={mostrar2}>{alumno[idioma].boton2}</button>
        </div>
        {ocultar1
            ? < ProfesoraImg ></ProfesoraImg>
            : null
        }
        {ocultar2
            ? <Lugar></Lugar>
            : null
        }
        
    </>
  )
}

export default Info;