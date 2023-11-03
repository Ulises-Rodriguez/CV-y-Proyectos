import React, { useState } from 'react'

export const Counter = ({ stock, setCantidad }) => {

    const [count, setCount] = useState(0);

    const incrementar = () => {
        if (stock > count) {
            setCount(prevCount => prevCount + 1);
            setCantidad(prevCantidad => prevCantidad + 1);
        }

    }

    const decrementar = () => {
        if (count !== 0) {
            setCount(prevCount => prevCount - 1);
            setCantidad(prevCantidad => prevCantidad - 1);
        }
    }

    return (
        <>
            <div className='divBtnCounterContainer'>
                <button onClick={decrementar}>-</button>
                <p>{count}</p>
                <button onClick={incrementar}>+</button>
            </div>
        </>
    )
}
