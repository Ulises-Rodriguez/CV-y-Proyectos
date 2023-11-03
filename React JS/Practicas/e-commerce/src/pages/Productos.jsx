import React from 'react'
import { Link } from 'react-router-dom'
import { useGetFSC } from '../customHooks/useGetFSColecction';
import { cargar } from '../funJS/cargar';
import { Loading } from '../components/Loading';

export const Productos = ({ url, array = null }) => {

    const {loading} = cargar();

    const {productos} = useGetFSC(url);
    
    return (
        <>
            {loading ? <section>
                <ul className='ulLinkProductos'>
                    {productos.map((producto, index) => <li key={producto.id}>
                        <Link className='linkProductos' to={`/${url}/${producto.id}`}>
                            <div className='divLinkInfoContainer'>
                                <div>
                                    {producto.id}
                                </div>
                                {(array) && <div>
                                    <img className='imgLink' src={array[index]} alt={producto.id} />
                                </div>}
                            </div>
                        </Link>
                    </li>)}
                </ul>
            </section> : <Loading />}
        </>
    )
}
