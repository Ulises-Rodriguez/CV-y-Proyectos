import { createContext, useEffect, useState } from "react";
import { helpHTTP } from "../../helpers/helpHTTP";

const CrudContext = createContext();

const CrudProvider = ({children})=>{

    const [db, setDb] = useState(null);
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
                setDb(res);
                setErr(null);
            } else {
                setDb(null);
                setErr(res);
            }
        })

        setLoading(false);
    }, [url]);
    //no le pases como dependencia api xq se mete en bucle por mas q la consola te diga q se lo pongas jajja

    const createData = (data) => {
        // console.log(data);
        data.id = Date.now();

        let options = { body: data, headers: { "content-type": "application/json" } }

        api.post(url, options).then(res => {
            // console.log(res);
            if (!res.err) {
                setDb([...db, res]);
            } else {
                setErr(res)
            }
        })
    };

    const updateData = (data) => {
        let endpoint = `${url}/${data.id}`;

        let options = { body: data, headers: { "content-type": "application/json" } };

        api.put(endpoint, options).then(res => {
            // console.log(res);
            if (!res.err) {
                let newData = db.map(el => el.id === data.id ? data : el);
                setDb(newData);
            } else {
                setErr(res)
            }
        })

    };

    const deleteData = (id) => {
        let isDelete = window.confirm(`Estas seguro de eliminar el registro con el id: ${id}?`);

        if (isDelete) {
            let endpoint = `${url}/${id}`;
            let options = { headers: { "content-type": "application/json" } };

            api.del(endpoint, options).then(res => {
                console.log(res);
                if (!res.err) {
                    let newData = db.filter((el) => el.id !== id);
                    setDb(newData);
                } else {
                    setErr(res);
                }
            })
        } else {
            return;
        }
    };

    const data = {
        db,
        dataToEdit,
        setDataToEdit,
        err,
        loading,
        createData,
        updateData,
        deleteData,
    }

    return(
        <CrudContext.Provider value={data}>{children}</CrudContext.Provider>
    )
}


export {CrudProvider};
export default CrudContext;