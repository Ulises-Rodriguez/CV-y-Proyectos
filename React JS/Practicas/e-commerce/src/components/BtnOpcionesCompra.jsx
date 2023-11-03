import React, { useContext } from 'react'
import { Context } from '../context/Context';
import { useNavigate } from 'react-router-dom';

export const BtnOpcionesCompra = ({ opcion }) => {

    const { setCart, setCliente } = useContext(Context);

    const navigate = useNavigate();

    const opciones = (e) => {
        const { target } = e;
        const { value } = target;

        if (value === "Reset") {
            setCart({
                productos : [],
                precioTotal : 0
            });

            setCliente({})

        }
        else {
            navigate("/checkout");
        }
    }

    return <button onClick={opciones} value={opcion}>{opcion}</button>
}
