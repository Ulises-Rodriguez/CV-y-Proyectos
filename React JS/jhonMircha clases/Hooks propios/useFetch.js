import { useEffect, useState } from "react";

export const useFetch = (url) => {
    const [data, setData] = useState(null);
    //esta variable se encarga de ver si la peticion esta pendiente o no. false --> peticion hecha, true caso contrario
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getData = async (url) => {
            //con el try probamos a hacer la peticion en caso de error tiramos el error con throw el q tiramos lo recive catch
            //en caso de estar todo bien se ejecuta el else
            try {
                let res = await fetch(url);

                //validacion
                //caso en q la rerspuesta (res) tenga algun problema 
                if (!res.ok) {
                    throw { err: true, status: res.status, statusText: !res.statusText ? "ocurrio un error" : res.statusText }
                } else {
                    let data = await res.json();

                    //actualizamos las 3 variables de estado
                    //como la peticion fue hecha ya no esta pendiente por lo caul cambiamos su valor a false
                    setIsPending(false);
                    //en data guardamos todo lo q convertimos a json
                    setData(data);
                    //el error lo ponemos en false para indicar q esta todo bien
                    setError({ err: false });
                }
            } catch (err) {
                setIsPending(true);
                setError(true);
            }
        }
        getData(url);
    }, [url]);

    return { data, isPending, error }

    //aca estoy retornando un objeto (puedo retornar lo q quiera [],string,etc)
    //en este caso devuelvo un objeto q ademas usa los shorthand recorda q si la propiedad se llama igual al valor no hace falta ponerlo, osea data : data
}