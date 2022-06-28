import React, { useReducer } from "react";
import { TYPES } from "./actons/contadorActions";
import { contadorInit, contadorInitialState, contadorReducer } from "./reducers/contadorReducer";

const ContadorMejorado = () => {

  const [state, dispatch] = useReducer(contadorReducer, contadorInitialState, contadorInit);

  const reset = ()=>{
    dispatch({type : TYPES.RESET});
  };

  const sumar = () => {
    dispatch({type : TYPES.INCREMENTAR});
  };

  const sumar5 = () => {
    dispatch({ type: TYPES.INCREMENTAR_5, payload : 5});
  };

  const restar = () => {
    dispatch({ type: TYPES.DECREMENTAR });
  };

  const restar5 = () => {
    dispatch({ type: TYPES.DECREMENTAR_5, payload : 5});
  };

  return (
    <div>
      <h2>Contador Mejorado Reducer</h2>
      <nav>
        <button onClick={reset}>0</button>
        <button onClick={sumar}>+</button>
        <button onClick={restar}>-</button>
        <button onClick={sumar5}>+5</button>
        <button onClick={restar5}>-5</button>
      </nav>
      <h3>{state.contador}</h3>
    </div>
  );
};

export default ContadorMejorado;
