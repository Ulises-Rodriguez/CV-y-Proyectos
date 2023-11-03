import React, { useContext} from 'react'
import { Context } from '../context/Context'
import { Formulario } from '../components/Formulario';
import { BtnOpcionesCompra } from '../components/BtnOpcionesCompra';
import { BtnRealizarCompra } from '../components/BtnRealizarCompra';
import { ResumenCompra } from '../components/ResumenCompra';

export const Checkout = () => {
    const { cart, isLogin} = useContext(Context);


    if (cart["productos"].length === 0) {
        return <h1>El carrito esta vacio</h1>
    }


    return (
        <>
            <div className='container-fluid'>
                <ResumenCompra />
                {!isLogin ? <div className='container-fluid'>
                    <div className='container-fluid'>
                        <Formulario />
                    </div>
                </div> : ""}
                <div className='container-fluid'>
                    <BtnOpcionesCompra opcion={"Reset"} />
                    <BtnRealizarCompra />
                </div>
            </div>
        </>

    )
}
