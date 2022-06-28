import React from 'react';

const CrudTableRowApi = ({ el, setDataToEdit, deleteData }) => {

    let { name, constelacion, id } = el;

    return (
        <tr>
            <td>{name}</td>
            <td>{constelacion}</td>
            <td>
                <button onClick={() => setDataToEdit(el)}>Editar</button>
                <button onClick={() => deleteData(id)}>Eliminar</button>
            </td>
        </tr>
    )
}

export default CrudTableRowApi;