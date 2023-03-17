import React, { createContext, useEffect, useState } from "react";
import { PALABROS } from "../assets/array";

//creacion del contexto
export const Contexto = createContext();

export const Datos = ({ children }) => {
  const [numRandom, setNumRandom] = useState(
    Math.floor(Math.random() * PALABROS.length)
  );
  const [pregunta, setPregunta] = useState(PALABROS[numRandom]["pregunta"]);
  const [palabra, setPalabra] = useState(PALABROS[numRandom]["palabro"]);
  const [count, setCount] = useState(0);
  const [correct,setCorrect] = useState(0);
  const [misLetras, setMisLetras] = useState([]);

  useEffect(() => {
    setNumRandom(Math.floor(Math.random() * PALABROS.length));
    setCount(count);
    setPalabra(palabra);
    setPregunta(pregunta);
    setCorrect(correct);
    setMisLetras(misLetras)
  }, [numRandom, pregunta, palabra,count,correct,misLetras]);

  return (
    <Contexto.Provider
      value={{
        numRandom,
        setNumRandom,
        palabra,
        setPalabra,
        pregunta,
        setPregunta,
        PALABROS,
        count,
        setCount,
        correct,
        setCorrect,
        misLetras,
        setMisLetras
      }}
    >
      {children}
    </Contexto.Provider>
  );
};
