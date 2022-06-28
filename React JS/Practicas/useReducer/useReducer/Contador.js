import React, { useState, useReducer } from "react";

const initialState = {
  contador: 0,
};

const init = (initialState)=>{
  return {contador : initialState.contador + 100};
};

const TYPES = {
    INCREMENTAR : "INCREMENTAR",
    INCREMENTAR_5 : "INCREMENTAR_5",
    DECREMENTAR : "DECREMENTAR",
    DECREMENTAR_5 : "DECREMENTAR_5",
    RESET : "RESET",
}

const reducer = (state, action) => {
  switch (action.type) {
    case TYPES.RESET:
        return initialState;
    case TYPES.INCREMENTAR:
      return { contador: state.contador + 1 };
    case TYPES.INCREMENTAR_5:
      return { contador: state.contador + action.payload };
    case TYPES.DECREMENTAR:
      return { contador: state.contador - 1 };
    case TYPES.DECREMENTAR_5:
      return { contador: state.contador - action.payload };
    default:
      return state;
  }

  return state;
};

const Contador = () => {
  //   const [count, setCount] = useState(0);

  const [state, dispatch] = useReducer(reducer, initialState, init);

  // const sumar = ()=>{
  //     setCount(count+1);
  // };

  const reset = ()=>{
    dispatch({type : TYPES.RESET});
  };

  const sumar = () => {
    dispatch({type : TYPES.INCREMENTAR});
  };

  const sumar5 = () => {
    dispatch({ type: TYPES.INCREMENTAR_5, payload : 5});
  };

  // const restar = ()=>{
  //     setCount(count-1);
  // };

  const restar = () => {
    dispatch({ type: TYPES.DECREMENTAR });
  };

  const restar5 = () => {
    dispatch({ type: TYPES.DECREMENTAR_5, payload : 5});
  };

  return (
    <div>
      <h2>Contador Reducer</h2>
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

export default Contador;
