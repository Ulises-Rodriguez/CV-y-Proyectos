import React, { useContext } from 'react'
import { Context } from '../context/Context'

export const Formulario = () => {

    const {cliente,setCliente} = useContext(Context);

    const datosCliente = (e)=>{

        setCliente({
            ...cliente,
            [e.target.id] : e.target.value
        })

    }

    return (
        <>
            <div className='container-fluid'>
                <div className="mb-3">
                    <label htmlFor="name" className="form-label">Nombre</label>
                    <input type='text' onChange={datosCliente} className="form-control" id="name" placeholder="ingrese su nombre" />
                </div>
                <div className="mb-3">
                    <label htmlFor="apellido" className="form-label">Apellido</label>
                    <input type='text' onChange={datosCliente} className="form-control" id="apellido" placeholder="ingrese su apellido" />
                </div>
                <div className="mb-3">
                    <label htmlFor="celular" className="form-label">Celular</label>
                    <input type='number' onChange={datosCliente} className="form-control" id="celular" placeholder="ingrese su numero" />
                </div>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email</label>
                    <input type="email" onChange={datosCliente} className="form-control" id="email" placeholder="ingrese su email" />
                </div>
                <div className="mb-3">
                    <label htmlFor="email2" className="form-label">Confirmar Email</label>
                    <input type="email" onChange={datosCliente} className="form-control" id="email2" placeholder="cofirme su email" />
                </div>
            </div>
        </>
    )
}
