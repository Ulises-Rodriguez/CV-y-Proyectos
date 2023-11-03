import React from 'react';

export const ItemListContainer = ({ mensaje }) => {

    return (
        <>
            <div className='msgContainer'>
                <p className='msg'>{mensaje}</p>
            </div>
        </>
    )
}
