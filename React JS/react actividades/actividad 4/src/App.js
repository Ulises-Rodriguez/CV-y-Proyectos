import './App.css';
import Comida from './componentes/Comida';
import { datos } from "./datos";
import { useState } from 'react';


function App() {

  const [productos, setProductos] = useState(datos);
  const [misProductos, setMisProductos] = useState([]);

  return (
    <>
      <Comida productos={productos} setProductos={setProductos} misProductos={misProductos} setMisProductos={setMisProductos}></Comida>
    </>
  );
}

export default App;
