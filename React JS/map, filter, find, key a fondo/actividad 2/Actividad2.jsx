import React from 'react'

function Actividad2({reyes}) {
  
  const borrar = (element)=>{
    element.target.parentNode.remove();
  }
  
  return (
    <>
      {reyes.filter(element => !element.nombre.includes("g")).map(element => <div key={element.nonbre}>{element.nombre} <button onClick={borrar}>Borrar</button></div>)}
    </>
  )
}

export default Actividad2;