import { useState } from "react";
import "./App.css";
import BotonCambio from "./componentes/BotonCambio";
import BotonContador from "./componentes/BotonContador";
import BotonImg from "./componentes/BotonImg";
import BotonTexto from "./componentes/BotonTexto";
import Pantalla from "./componentes/Pantalla";

function App() {

  const [res, setRes] = useState("Texto Inicial");
  const [colores, setColores] = useState("white");
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="divContenedor">
        <BotonTexto setRes={setRes}></BotonTexto>
        <BotonImg setRes={setRes}></BotonImg>
        <BotonCambio colores={colores} setColores={setColores}></BotonCambio>
        <BotonContador count={count} setCount={setCount}></BotonContador>
      </div>
      <div className="divPantalla">
        <Pantalla res={res} count={count} setCount={setCount} colores={colores}></Pantalla>
      </div>
    </>
  );
}

export default App;
