import React, { useContext } from 'react'
import { Context } from '../context/Context'

export const Precio = () => {
    const {cart} = useContext(Context);

    return <li>Total: ${Math.round(cart["precioTotal"] * 100) / 100}</li>
}
