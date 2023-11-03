import React, { useEffect } from 'react';

const Pantalla = ({res,count,setCount,colores}) => {

    useEffect(() => {
      setCount(count);
    },[setCount,count])
    

  return (
    <>
        <div style={{backgroundColor : colores}}>{res}</div>
        <div>{count}</div>
    </>
  )
}

export default Pantalla;