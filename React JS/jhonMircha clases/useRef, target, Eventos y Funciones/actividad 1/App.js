import imgreySisebuto from './imagenesReyes/rey_sisebuto.png'
import imgreyAtanagildo from './imagenesReyes/rey_atanagildo.png'
import './App.css';
import {useRef} from 'react';

function App() {

  const refCaja = useRef();

  const incrementar = (value)=>{
    value.target.innerHTML = Number(value.target.innerHTML) + 1;
    if (value.target.innerHTML >= 10) {
      value.target.innerHTML = 1;
    }
    if (value.target.innerHTML >= 8) {
      value.target.style.backgroundColor = "#f00";
    } else {
      value.target.style.backgroundColor = "#fff";
    }
    //es necesario poner la condicion del q analiza si es >= 8 despues de >= 10 xq sino cuando llegue a 10 pasa al 1 pero no le cambia el color, esto debido a q cuando llega a 10 no tiene nada debajo para comprobar 
    //ademas si en la condicion q analiza >= 8  ponemos en ves de "if" "else if" nos da el mismo problema
  };

  const convertir = ()=>{
    refCaja.current.innerHTML = Number(refCaja.current.innerHTML) * 2;
  };

  const cambioImagen = (img)=>{
    if (img.target.src.includes("rey_atanagildo")) {
      img.target.src = imgreySisebuto;  
    } else {
      img.target.src = imgreyAtanagildo;
    }
  };

  const lectura = (num)=>{
    refCaja.current.innerHTML = num.target.value;
  };

  return (
    <>
    <div className="caja" onClick={incrementar} ref={refCaja}>1</div>
    <button onClick={convertir}>Aceptar</button>
    <div>
      <img src={imgreyAtanagildo} onClick={cambioImagen}/>
    </div>
    <input className="campo" onChange={lectura}/>
    </>
  );
}

export default App;
