import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { createAction, deleteAction, noAction, readAllAction, updateAction } from "../actions/crudActions";
import { helpHTTP } from "../helpers/helpHTTP";
import Loader from "../Loader/Loader";
import Message from "../Message/Message";
import CrudFormApi from "./CrudFormApi";
import CrudTableApi from "./CrudTableApi";

function CrudApi() {
  const state = useSelector((state) => state);
  const dispatch = useDispatch();

  const { db } = state.crud;

  const [dataToEdit, setDataToEdit] = useState(null);
  const [err, setErr] = useState(null);
  const [loading, setLoading] = useState(false);

  let api = helpHTTP();
  let url = "http://localhost:5000/santos";

  useEffect(() => {
    setLoading(true);

    api.get(url).then((res) => {
      console.log(res);
      if (!res.err) {
        dispatch(readAllAction(res));
        setErr(null);
      } else {
        dispatch(noAction());
        setErr(res);
      }
    });

    setLoading(false);
  }, [url, dispatch]);

  const createData = (data) => {
    data.id = Date.now();

    let options = {
      body: data,
      headers: { "content-type": "application/json" },
    };

    api.post(url, options).then((res) => {
      if (!res.err) {
        dispatch(createAction(res));
      } else {
        setErr(res);
      }
    });
  };

  const updateData = (data) => {
    let endpoint = `${url}/${data.id}`;

    let options = {
      body: data,
      headers: { "content-type": "application/json" },
    };

    api.put(endpoint, options).then((res) => {
      if (!res.err) {
        dispatch(updateAction(res));
      } else {
        setErr(res);
      }
    });
  };

  const deleteData = (id) => {
    let isDelete = window.confirm(
      `Estas seguro de eliminar el registro con el id: ${id}?`
    );

    if (isDelete) {
      let endpoint = `${url}/${id}`;
      let options = { headers: { "content-type": "application/json" } };

      api.del(endpoint, options).then((res) => {
        if (!res.err) {
          dispatch(deleteAction(id));
        } else {
          setErr(res);
        }
      });
    } else {
      return;
    }
  };

  return (
    <div>
      <h2>Crud Api</h2>
      <article className="grid1-2">
        <CrudFormApi
          createData={createData}
          updateData={updateData}
          dataToEdit={dataToEdit}
          setDataToEdit={setDataToEdit}
        ></CrudFormApi>
        {loading && <Loader></Loader>}
        {err && (
          <Message
            msg={`Error ${err.status} : ${err.statusText}`}
            bgColor={"#dc3545"}
          ></Message>
        )}
        {db && (
          <CrudTableApi
            data={db}
            setDataToEdit={setDataToEdit}
            deleteData={deleteData}
          ></CrudTableApi>
        )}
      </article>
    </div>
  );
}

export default CrudApi;
