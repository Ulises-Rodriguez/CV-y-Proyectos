import React, { useState } from 'react'
import { BtnAñadir} from './BtnAñadir'
import { Counter } from './Counter'
import { BtnDetalle } from './BtnDetalle'

export const Item = ({ url,titulo, descripcion, precio, style={width : "18rem", height : "fit-content"}, stock ,children }) => {

    const [cantidad, setCantidad] = useState(0);

    return (
        <>
            <div className="card" style={style}>
                <h2>{titulo}</h2>
                {children}
                <div className="card-body divTextCard">
                    <p className="card-text">{descripcion}</p>
                    <p className="card-text">{`$${precio}`}</p>
                </div>
                <div className='divComprar'>
                    <Counter stock={stock} setCantidad={setCantidad}/>
                    <div className='btnContinaer'>
                        <BtnDetalle url={url}/>
                        <BtnAñadir nombre={titulo} precio={precio} cantidad={cantidad}/>
                    </div>
                </div>
            </div>
        </>
    )
}
