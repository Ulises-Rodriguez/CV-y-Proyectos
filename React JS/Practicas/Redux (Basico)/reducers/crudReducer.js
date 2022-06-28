import { CREATE_DATA, DELETE_DATA, NO_DATA, READ_ALL_DATA, UPDATE_DATE } from "../types";

export const initialState = {
    db : [],
};

//no te olvides de inicializar o darle por defecto un valor al state xq de no hacerlo la primera ves q carga la pagina va a dar error de q crud esta undefined
export const crudReducer = (state=initialState,action)=>{
    switch (action.type) {
        case READ_ALL_DATA:{
            console.log(action.payload);
            return{
                ...state,
                db : action.payload.map((data)=>data)
            }
        }
        case CREATE_DATA:{
            console.log(action.payload);
            return{
                ...state,
                db : [...state.db, action.payload]
            }
        }
        case UPDATE_DATE:{
            console.log(action.payload);
            let newData = state.db.map(el => el.id === action.payload.id ? action.payload : el);

            return{
                ...state,
                db : newData
            }
        }
        case DELETE_DATA:{
            console.log(action.payload);
            let newData = state.db.filter((el) => action.payload !== el.id);

            return{
                ...state,
                db : newData
            }
        }
        case NO_DATA:{
            return initialState;
        }
        default:
            return state;
    }
};