import React, { useState, useEffect } from "react";
import Loader from "../Components/Loader";
import Message from "../Components/Message";
import { helpHTTP } from "../helpers/helpHTTP";
import CrudFormApi from "./CrudFormApi";
import CrudTableApi from "./CrudTableApi";
import {
  BrowserRouter,
  HashRouter,
  NavLink,
  Routes,
  Route,
} from "react-router-dom";
import Error404 from "../Router/pages/Error404";

function CrudApi() {
  const [db, setDb] = useState(null);
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
        setDb(res);
        setErr(null);
      } else {
        setDb(null);
        setErr(res);
      }
    });

    setLoading(false);
  }, []);

  const createData = (data) => {
    // console.log(data);
    data.id = Date.now();

    let options = {
      body: data,
      headers: { "content-type": "application/json" },
    };

    api.post(url, options).then((res) => {
      console.log(res);
      if (!res.err) {
        setDb([...db, res]);
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
      console.log(res);
      if (!res.err) {
        let newData = db.map((el) => (el.id === data.id ? data : el));
        setDb(newData);
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
        console.log(res);
        if (!res.err) {
          let newData = db.filter((el) => el.id !== id);
          setDb(newData);
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
      {/* el basename es una propiedad q nos permite poner una ruta base (osea la parte de la ruta q todos tienen) */}
      <HashRouter>
        <header>
          <h2>Crud api con rutas:</h2>
          <NavLink to="/santos" activeclassname="active">
            Santos
          </NavLink>
          <NavLink to="/santos/agregar" activeclassname="active">
            Agregar
          </NavLink>
        </header>
        <Routes>
          <Route
            path="/santos"
            element={
              <>
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
              </>
            }
          ></Route>
          <Route
            path="/santos/agregar"
            element={
              <CrudFormApi
                createData={createData}
                updateData={updateData}
                dataToEdit={dataToEdit}
                setDataToEdit={setDataToEdit}
              ></CrudFormApi>
            }
          ></Route>
          <Route
            path="/santos/editar/:id"
            element={
              <CrudFormApi
                createData={createData}
                updateData={updateData}
                dataToEdit={dataToEdit}
                setDataToEdit={setDataToEdit}
              ></CrudFormApi>
            }
          ></Route>
          <Route path="/*" element={<Error404 />}></Route>
        </Routes>
      </HashRouter>
    </div>
  );
}

export default CrudApi;
