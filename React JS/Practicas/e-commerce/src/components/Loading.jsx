import React from 'react'

export const Loading = () => {
    return (
        <div className="spinnerContainer">
            <h1 className='cargandoTitulo'>Cargando los productos...</h1>
            <div className="spinner-border spinner" role="status" aria-hidden="true"></div>
        </div>
    )
}
