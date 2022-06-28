import React, { useContext } from "react";
import CrudContext from "./CrudContext/CrudContext";
import CrudTableRowApi from "./CrudTableRowApi";

function CrudTableApi() {
    //dato nosotros cuando pasamos por propiedades al db le llamamos data pero en el contexto se llama db por lo cual podemos crearle un alias para solucionar este problema (la otra es cambiar data y poner db de una XD)
  const { db : data } = useContext(CrudContext);

  return (
    <div>
      <h3>Tabla de datos</h3>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Constelacion</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {data.length > 0 ? (
            data.map((el) => <CrudTableRowApi key={el.id} el={el}/>)
          ) : (
            <tr>
              <td colSpan="3">Sin datos</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default CrudTableApi;
