import React from 'react'
import { Link } from 'react-router-dom'

export const BtnDetalle = ({url}) => {

    return (
        <>
            <Link to={`/${url}`}>
                <button>Detalles</button>
            </Link>
        </>
    )
}
