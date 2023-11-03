import React from 'react'

export const CarritoLi = ({nombreProducto, cantidad}) => {

    return (
        <>
            <li>
                <div>{`${nombreProducto} x${cantidad}`}</div>
            </li>
            <li><hr className="dropdown-divider" /></li>
        </>
    )
}
