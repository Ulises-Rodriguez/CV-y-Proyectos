import { useEffect } from "react";
import { useState } from "react";

const useFetch = ( url ) => {

    const [productos, setProductos] = useState([]);

    const productosFetch = async (url) => {
        const res = await fetch(url);
        const data = await res.json();

        setProductos([...data]);
    }

    useEffect(() => {

        productosFetch(url);

    }, [])

    return { productos };

}

export default useFetch;