import { useState } from 'react';
import './App.css';
import Reyes from './componentes/Reyes';

const reyes = [
  {
    nombre : "Ervigio",
    vacas : 3,
    img : "https://www.html6.es/img/rey_ervigio.png"
  },{
    nombre : "Atanagildo",
    vacas : 6,
    img : "https://www.html6.es/img/rey_atanagildo.png"
  },{
    nombre : "Ataulfo",
    vacas : 11,
    img : "https://www.html6.es/img/rey_ataulfo.png"
  },{
    nombre : "Leogivildo",
    vacas : 2,
    img : "https://www.html6.es/img/rey_leogivildo.png"
  },
]

function App() {

  const [titulo, setTitulo] = useState("Vota por tu rey favorito");    
  const [aux, setAux] = useState(0)

  const sumar = (nombre,contador)=>{

    if (aux === 0) {
      setTitulo("Vota por tu rey favorito");
      setAux(aux+1);
    } else {
      setTitulo(<div>Has votado {contador} por {nombre}</div>);
    }
  }
  
  return (
    <>
      <div className="App">
        <h1>{titulo}</h1>
        <div className='reyesContainer'>
          <Reyes onAction={sumar} nombre={reyes[0].nombre} vacas={reyes[0].vacas} img={reyes[0].img}></Reyes>
          <Reyes onAction={sumar} nombre={reyes[1].nombre} vacas={reyes[1].vacas} img={reyes[1].img}></Reyes>
          <Reyes onAction={sumar} nombre={reyes[2].nombre} vacas={reyes[2].vacas} img={reyes[2].img}></Reyes>
          <Reyes onAction={sumar} nombre={reyes[3].nombre} vacas={reyes[3].vacas} img={reyes[3].img}></Reyes>
        </div>
      </div>
    </>
      
  );
}

export default App;
