import React, { useState, useEffect, useReducer } from 'react';
import { helpHTTP } from '../helpers/helpHTTP';
import Loader from '../Loader/Loader';
import Message from '../Message/Message';
import { TYPES } from '../useReducer/actons/crudActions';
import { crudInitialState, crudReducer } from '../useReducer/reducers/crudReducer';
import CrudFormApi from './CrudFormApi';
import CrudTableApi from './CrudTableApi';

function CrudApi() {

    //const [db, setDb] = useState(null);
    const [state, dispatch] = useReducer(crudReducer, crudInitialState);
    const {db} = state; 

    const [dataToEdit, setDataToEdit] = useState(null);
    const [err, setErr] = useState(null);
    const [loading, setLoading] = useState(false);

    let api = helpHTTP();
    let url = "http://localhost:5000/santos";

    useEffect(() => {
        setLoading(true);

        api.get(url).then(res => {
            console.log(res);
            if (!res.err) {
                // con el type indicamos la operacion q queremos realizar y con el payload mandamos la informacion adicional, q en este caso va a ser res q es donde esta toda la respuesta de nuetra peticion (osea la info dentro del db.json)
                dispatch({type : TYPES.READ_ALL_DATA, payload : res});
                //setDb(res);
                setErr(null);
            } else {
                //en este caso no mandamos el payload xq NO_DATA se encarga de poner la db en null
                dispatch({type : TYPES.NO_DATA})
                //setDb(null);
                setErr(res);
            }
        })

        setLoading(false);
    }, [url])



    const createData = (data) => {
        // console.log(data);
        data.id = Date.now();

        let options = { body: data, headers: { "content-type": "application/json" } }

        api.post(url, options).then(res => {
            //console.log(res);
            if (!res.err) {
                // aca lo mismo con el type indicamos q vamos a ejecutar la accion crear un nuevo dato y con el payload pasamos los datos nuevos q escribimos en el formulario 
                dispatch({type : TYPES.CREATE_DATA, payload : res});
                //setDb([...db, res]);
            } else {
                setErr(res)
            }
        })
    }

    const updateData = (data) => {
        let endpoint = `${url}/${data.id}`;

        let options = { body: data, headers: { "content-type": "application/json" } };

        api.put(endpoint, options).then(res => {
            //console.log(res);
            if (!res.err) {
                //esta ya no la necesitamos aca xq la implementacion va a estar en el reducer
                // let newData = db.map(el => el.id === data.id ? data : el);
                dispatch({type : TYPES.UPDATE_DATE, payload : data});
                //setDb(newData);
            } else {
                setErr(res)
            }
        })

    }

    const deleteData = (id) => {
        let isDelete = window.confirm(`Estas seguro de eliminar el registro con el id: ${id}?`);

        if (isDelete) {
            let endpoint = `${url}/${id}`;
            let options = { headers: { "content-type": "application/json" } };

            api.del(endpoint, options).then(res => {
                //console.log(res);
                if (!res.err) {
                    // let newData = db.filter((el) => el.id !== id);
                    //en este caso el payload no tiene q ser un objeto sino simplemente el id del elemento q quiero eliminar
                    dispatch({type : TYPES.DELETE_DATA, payload : id});
                    //setDb(newData);
                } else {
                    setErr(res);
                }
            })
        } else {
            return;
        }
    }

    return (
        <div>
            <h2>Crud Api</h2>
            <article className='grid1-2'>
                <CrudFormApi createData={createData} updateData={updateData} dataToEdit={dataToEdit} setDataToEdit={setDataToEdit}></CrudFormApi>
                {loading && <Loader></Loader>}
                {err && <Message msg={`Error ${err.status} : ${err.statusText}`} bgColor={"#dc3545"}></Message>}
                {db && <CrudTableApi data={db} setDataToEdit={setDataToEdit} deleteData={deleteData}></CrudTableApi>}
            </article>
        </div>
    )
}

export default CrudApi;