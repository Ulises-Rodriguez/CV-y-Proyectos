import { TYPES } from "../actons/crudActions";

export const crudInitialState = {
    db : null
};

export const crudReducer = (state,action)=>{
    switch (action.type) {
        case TYPES.READ_ALL_DATA:{
            console.log(action.payload);
            return{
                ...state,
                db : action.payload.map((data)=>data)
            }
        }
        case TYPES.CREATE_DATA:{
            console.log(action.payload);
            return{
                //hace una copia del estado actual y pegale el db
                ...state,
                // ahora db va a ser una copia del la base de datos actual y le vas a agregar lo q tenga payload
                db : [...state.db, action.payload]
            }
        }
        //en este caso no vamos a necesitar el READ_ONE_DATA ya q cuando carga toda la pagina por primera ves se trae todos los datos de la tabala, por lo cual para editar un valor no hace falta en este caso. Ahora si para actualizar un valor en particular dependiera de hacer una nueva peticon a la api en ese caso si lo necesitariomos
        // case TYPES.READ_ONE_DATA:{
            
        // }
        case TYPES.UPDATE_DATE:{
            console.log(action.payload);
            //el payload va a ser el objeto q trae el nombre, constelacion, id
            let newData = state.db.map(el => el.id === action.payload.id ? action.payload : el);

            return{
                ...state,
                db : newData
            }
        }
        case TYPES.DELETE_DATA:{
            //en este caso va a ser el id del elemento q queromos eliminar
            console.log(action.payload);
            // y en este caso no es action.payload.id ya q el payload ya es el id
            let newData = state.db.filter((el) => action.payload !== el.id);

            return{
                ...state,
                db : newData
            }
        }
        case TYPES.NO_DATA:{
            return crudInitialState;
        }
        default:
            return state;
    }
};