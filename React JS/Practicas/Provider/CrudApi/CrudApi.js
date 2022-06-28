import React, { useContext} from "react";
import Loader from "../Loader/Loader";
import Message from "../Message/Message";
import CrudContext from "./CrudContext/CrudContext";
import CrudFormApi from "./CrudFormApi";
import CrudTableApi from "./CrudTableApi";

function CrudApi() {

    const {loading, err, db} = useContext(CrudContext);

  return (
    <div>
      <h2>Crud Api CON Context API</h2>
      <article className="grid1-2">
          {/* <CrudProvider>...</CrudProvider> esto aca no lo puedo hacer ya q no puedo usar el provedor y el consumo de los datos en el mismo archivo, por lo cual al Povider tenes q llamarlo en esete caso en app*/}
        <CrudFormApi></CrudFormApi>
        {loading && <Loader></Loader>}
        {err && (
          <Message
            msg={`Error ${err.status} : ${err.statusText}`}
            bgColor={"#dc3545"}
          ></Message>
        )}
        {db && (
          <CrudTableApi></CrudTableApi>
        )}
      </article>
    </div>
  );
}

export default CrudApi;
