import React, { useContext } from "react";
import { Contexto } from "../contexto/Contexto";

const Pregunta = () => {
  const { pregunta } = useContext(Contexto);

  return (
    <>
      <h1 className="pregunta">{pregunta}</h1>
    </>
  );
};

export default Pregunta;
