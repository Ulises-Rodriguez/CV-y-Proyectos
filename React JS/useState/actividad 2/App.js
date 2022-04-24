import './App.css';
import './miCss.css';
import React,{useState} from 'react';

const App = () => {

  const cambios = [
    {
      moneda: "Euro",
      cambio: 1,
    }, {
      moneda: "Peso argentino",
      cambio: 118.6,
    }, {
      moneda: "Peso colombiano",
      cambio: 4543.5,
    }, {
      moneda: "Peso mexicano",
      cambio: 23.2,
    }, {
      moneda: "Dólar",
      cambio: 1.14
    }
  ];

  const [euro, setEuro] = useState(0);
  const [arg, setArg] = useState(0);
  const [col, setCol] = useState(0);
  const [mex, setMex] = useState(0);
  const [dolar, setDolar] = useState(0);

  const modificar = (num)=>{
    setEuro(num.target.value);
    setArg(num.target.value * cambios[1].cambio);
    setCol(num.target.value * cambios[2].cambio);
    setMex(num.target.value * cambios[3].cambio);
    setDolar(num.target.value * cambios[4].cambio);
    
  }

  return (
    <>
      <div className='euroContainer'>
        <div>{cambios[0].moneda}</div>
        <input type="number" value={euro} onChange={modificar}></input>
      </div>
      <div className='pesosArgentinosContainer'>
        <div>{cambios[1].moneda}</div>
        <input type="number"value={arg} readOnly></input>
      </div>
      <div className='pesosColombianosContainer'>
        <div>{cambios[2].moneda}</div>
        <input type="number" value={col} readOnly></input>
      </div>
      <div className='pesosMexicanosContainer'>
        <div>{cambios[3].moneda}</div>
        <input type="number" value={mex} readOnly></input>
      </div>
      <div className='dolarContainer'>
        <div>{cambios[4].moneda}</div>
        <input type="number" value={dolar} readOnly></input>
      </div>
    </>
  )
}

export default App;