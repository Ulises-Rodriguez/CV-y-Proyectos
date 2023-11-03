import React from 'react'
import { useState } from 'react';
import { createContext } from 'react'

export const Context = createContext();

export const ContextWrapper = ({ children }) => {
    // card
    const [cart, setCart] = useState({
        productos : [],
        precioTotal : 0
    });

    const [cliente,setCliente] = useState({
        name : "",
        apellido : "",
        celular : "",
        email : "",
        email2 : ""
    })

    {/* aca falta hacer una opcion para loguearse desde la la navbar */}
    const [isLogin, setIsLogin] = useState(false);


    const calcularPrecioTotal = () => {
        return cart["productos"].reduce((acumulador, producto) => acumulador + producto.cantidad * producto.precio, 0);
    };

    const objetoProps = {
        cart,
        setCart,
        cliente,
        setCliente,
        calcularPrecioTotal,
        isLogin,
        setIsLogin
    }

    return (
        <Context.Provider value={{ ...objetoProps }}>
            {children}
        </Context.Provider>
    )
}

