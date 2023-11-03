import React, { useEffect, useState } from 'react';

const Reyes = ({nombre,vacas,img,onAction}) => {

    const [contador, setContador] = useState(0);

    const votar = ()=>{
        setContador(contador+1);
    }

    useEffect(() => {
        onAction(nombre,contador);
    },[contador]);
    

  return (
    <>
        <div className='reyContainer'>
            <h2 className='nombre'>{nombre}</h2>
            <h3 className='vacas'>{vacas}</h3>
            <img src={img} alt='' className='imgRey'></img>
            <div className='btnContainer'>
                <button className='btnVotar' onClick={votar}>votar</button>
                <div className='contador'>{contador}</div>
            </div>
        </div>
    </>
  )
}

export default Reyes;