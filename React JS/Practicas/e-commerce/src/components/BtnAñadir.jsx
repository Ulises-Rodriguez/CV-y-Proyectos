import React, { useContext } from 'react'
import { Context } from '../context/Context';

export const BtnAñadir = ({ nombre, precio, cantidad }) => {

    const { cart, setCart, calcularPrecioTotal } = useContext(Context);
    
    const añadir = () => {
        
        const { productos } = cart;
        const indexProducto = cart["productos"].findIndex((producto) => producto.name === nombre);

        if (cantidad > 0) {

            if (indexProducto > -1) {
                productos[indexProducto].cantidad += cantidad;

            } else {

                const producto = {
                    id: cart["productos"].length,
                    name: nombre,
                    cantidad,
                    precio
                }

                productos.push(producto);

            }

            setCart({
                ...cart,
                productos,
                precioTotal : calcularPrecioTotal()
            })
        }
    }

    return <button type="button" onClick={añadir}>Añadir</button>
}
