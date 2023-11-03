import React, { useEffect, useState } from 'react'
import { loadingFun } from '../funJS/asyncMocks';

export const cargar = () => {

    const [loading, setLoading] = useState(false);

    useEffect(() => {
        loadingFun()
            .then(cargando => setLoading(cargando))
    }, [])

  return {loading}
}