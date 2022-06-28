import { TYPES } from "../actons/contadorActions";

export const contadorInitialState = {
  contador: 0,
};

export const contadorInit = (contadorInitialState) => {
  return { contador: contadorInitialState.contador + 100 };
};

export const contadorReducer = (state, action) => {
  switch (action.type) {
    case TYPES.RESET:
      return contadorInitialState;
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
