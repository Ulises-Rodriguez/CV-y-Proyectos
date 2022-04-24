import React from 'react'

function ComponenteCurso({reyes}) {
    
    const ruta = "https://www.html6.es/img/rey_";
    const imagen = `${ruta}${rey.toLowerCase()}.png`;

    const resultado = reyes.map(element => {    
            <div key={element.nombre} className='rey'>
                <span className='rojo'>{element.nombre.toUpperCase()}</span> ha comido {element.reinado * element.vacasComidas * 365} vacas comidas en sus {element.reinado} <img src={imagen}></img>
            </div>
        })

    return (
        <>
            {resultado}
        </>
    )
}

export default ComponenteCurso;