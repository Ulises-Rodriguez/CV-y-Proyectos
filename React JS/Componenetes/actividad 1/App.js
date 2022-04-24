import './App.css';
import './miCss.css';
import React,{useState} from 'react';
import ReyesComponente from './ficheros App/componentes/actividad 1/ReyesComponente';


const App = () => {

  const reyes = [
    {
      nombre: "Atanagildo",
      color: "darkolivegreen",
      precio: 178
    }, {
      nombre: "Ervigio",
      color: "crimson",
      precio: 169
    }, {
      nombre: "Ataúlfo",
      color: "peru",
      precio: 81
    }, {
      nombre: "Leogivildo",
      color: "darkmagenta",
      precio: 126
    }, {
      nombre: "Recesvinto",
      color: "royalblue",
      precio: 141
    }, {
      nombre: "Sisebuto",
      color: "teal",
      precio: 69
    }
  ]

  const [totalPago, setTotalPago] = useState(0);

  return (
    <>
      <div className='pagoTotal'>Total a pagar: ${totalPago}</div>
      <div className='container'>
        <ReyesComponente rey={reyes[0].nombre} color={reyes[0].color} precio={reyes[0].precio} img="https://www.html6.es/img/rey_atanagildo.png" setTotalPago={setTotalPago}></ReyesComponente>
        <ReyesComponente rey={reyes[1].nombre} color={reyes[1].color} precio={reyes[1].precio} img="https://www.html6.es/img/rey_ervigio.png" setTotalPago={setTotalPago}></ReyesComponente>
        <ReyesComponente rey={reyes[2].nombre} color={reyes[2].color} precio={reyes[2].precio} img="https://www.html6.es/img/rey_ataulfo.png" setTotalPago={setTotalPago}></ReyesComponente>
        <ReyesComponente rey={reyes[3].nombre} color={reyes[3].color} precio={reyes[3].precio} img="https://www.html6.es/img/rey_leogivildo.png" setTotalPago={setTotalPago}></ReyesComponente>
        <ReyesComponente rey={reyes[4].nombre} color={reyes[4].color} precio={reyes[4].precio} img="https://www.html6.es/img/rey_recesvinto.png" setTotalPago={setTotalPago}></ReyesComponente>
        <ReyesComponente rey={reyes[5].nombre} color={reyes[5].color} precio={reyes[5].precio} img="https://www.html6.es/img/rey_sisebuto.png" setTotalPago={setTotalPago}></ReyesComponente>        
      </div>
    </>
  )
}

export default App;