import React from 'react'

function Actividad4({reyes}) {
  
  const sumar = (element)=>{
    ++element.target.innerHTML;
  }

  const resultado = reyes.filter(element => element.reinado > 10 && element.vacasComidas > 10).map(element => <div key = {element.nombre}>{element.nombre}<div className='numero' onClick={sumar}>0</div></div>)

  return (
    <>
      {resultado}
    </>
  );
}

export default Actividad4;