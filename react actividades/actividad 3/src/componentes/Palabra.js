import React, { useContext, useEffect} from "react";
import { Contexto } from "../contexto/Contexto";

const Palabra = () => {
  const {palabra,misLetras,setMisLetras} = useContext(Contexto);

  const crearLineas = ()=>{
    let aux = [];

    for (let i = 0; i < palabra.length; i++) {
      aux.push(palabra[i])  
    }

    return aux.map((l,index)=>(
      misLetras.indexOf(l)===-1 ? <div className="linea" key={index}></div>
      : <div className="linea" key={index}>{l}</div>  
    ))
  }

  useEffect(() => {
    setMisLetras(misLetras)
  }, [misLetras,setMisLetras])
  

  return (
    <>
      <div className="palabraContainer">
        {/* {palabra} */}
        {crearLineas()}
      </div>
    </>
  );
};

export default Palabra;
