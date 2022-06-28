import React, { useContext } from "react";
import CrudContext from "./CrudContext/CrudContext";

const CrudTableRowApi = ({el}) => {
  let { name, constelacion, id } = el;

  const { setDataToEdit, deleteData } = useContext(CrudContext);

  return (
    <tr>
      <td>{name}</td>
      <td>{constelacion}</td>
      <td>
        <button onClick={() => setDataToEdit(el)}>Editar</button>
        <button onClick={() => deleteData(id)}>Eliminar</button>
      </td>
    </tr>
  );
};

export default CrudTableRowApi;
