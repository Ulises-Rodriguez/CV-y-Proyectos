import React from "react";
import { Link, Route,Routes } from "react-router-dom";
import Topic from "./Topic";

const ReactTopics = () => {
  return (
    <div>
      <h3>Temas de React</h3>
      <ul>
        <li>
          {/* <Link to="js">JSX</Link> */}
          <Link to="/react/jsx">JSX</Link>
        </li>
        <li>
          <Link to="/react/props">Props</Link>
        </li>
        <li>
          <Link to="/react/estado">Estado</Link>
        </li>
        <li>
          <Link to="/react/componentes">Componentes</Link>
        </li>
      </ul>
        <Routes>
          <Route
            path=""
            element={
              <>
                <h2>react docs</h2>
              </>
            }
          ></Route>
          
          {/* forma dinamica */}
          {/* aca se esta haciendo de forma general pero lo ideal seria q cada seccion tenga su propio componenete */}
          <Route path="/:topic" element={<Topic></Topic>} />
          
          {/* forma estatica */}
          {/* <Route
            path="/jsx"
            element={
              <>
                <h2>jsx docs</h2>
              </>
            }
          ></Route>
          <Route
            path="/props"
            element={
              <>
                <h2>props docs</h2>
              </>
            }
          ></Route>
          <Route
            path="/estado"
            element={
              <>
                <h2>estado docs</h2>
              </>
            }
          ></Route>
          <Route
            path="/componentes"
            element={
              <>
                <h2>componentes docs</h2>
              </>
            }
          ></Route> */}
        </Routes>
    </div>
  );
};

export default ReactTopics;
