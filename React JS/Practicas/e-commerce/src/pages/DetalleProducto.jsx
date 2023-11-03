import React from 'react'
import { useParams } from 'react-router-dom'
import { obtenerProducto } from '../funJS/obtenerProducto';
import { ComporbarCategoria } from '../components/ComprobarCategoria';
import { useGetFSC } from '../customHooks/useGetFSColecction';
import { cargar } from '../funJS/cargar';
import { Loading } from '../components/Loading';
import { NotFound } from './NotFound';

export const DetalleProducto = ({ url }) => {

    const { id } = useParams();

    const {loading} = cargar();

    const {productos} = useGetFSC(url);

    const producto = obtenerProducto(id,productos);

    return (
        <>
        {loading ? ((producto !== undefined) ? <ComporbarCategoria producto={producto} /> : <NotFound />) : <Loading/>}
        </>
    )
}
