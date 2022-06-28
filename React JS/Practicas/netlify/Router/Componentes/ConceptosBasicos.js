import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Navigate,
  Routes,
  HashRouter,
} from "react-router-dom";
import Acerca from "../pages/Acerca";
import Contacto from "../pages/Contacto";
import Error404 from "../pages/Error404";
import Home from "../pages/Home";
import Login from "../pages/Login";
import LoginOut from "../pages/LoginOut";
import Productos from "../pages/Productos";
import ReactTopics from "../pages/ReactTopics";
import Usuario from "../pages/Usuario";
import MenuConceptos from "./MenuConceptos";
import PrivateRoute from "./PrivateRoute";
import { useState } from "react";

const ConceptosBasicos = () => {

  const [auth, setAuth] = useState(false)

  return (
    <div>
      <h2>Hash Router</h2>
      <HashRouter>
       <MenuConceptos/>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/acerca" element={<Acerca/>}></Route>
          <Route path="/contacto" element={<Contacto/>}></Route>
          <Route path="/usuario/:username" element={<Usuario/>}></Route> 
          <Route path="/productos" element={<Productos/>}></Route> 
          <Route path="/productos" element={<Productos/>}></Route>
          <Route path="/about"  element={ <> <Navigate to="/acerca" /> </> } />
          <Route path="/contact" element={<Navigate to="/contacto" />}></Route>
          <Route path="react/*" element= {<ReactTopics/>} />
          <Route path="/login" element={<Login setAuth={setAuth}/>}></Route>
          <Route path="/loginOut" element={<LoginOut setAuth={setAuth}></LoginOut>}></Route>
          <Route path="dashboard" element={<PrivateRoute auth={auth}/>}/>
          <Route path="*" element={<Error404/>}></Route>
        </Routes>
      </HashRouter>
      {/* <hr></hr>
      <h2>ConceptosBasicos</h2>
      <Router>
        <MenuConceptos></MenuConceptos>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/acerca" element={<Acerca/>}></Route>
          <Route path="/contacto" element={<Contacto/>}></Route>
          <Route path="/usuario/:username" element={<Usuario/>}></Route> 
          <Route path="/productos" element={<Productos/>}></Route> 
          <Route path="/productos" element={<Productos/>}></Route>
          <Route path="/about"  element={ <> <Navigate to="/acerca" /> </> } />
          <Route path="/contact" element={<Navigate to="/contacto" />}></Route>
          <Route path="react/*" element= {<ReactTopics/>} />
          <Route path="/login" element={<Login setAuth={setAuth}/>}></Route>
          <Route path="/loginOut" element={<LoginOut setAuth={setAuth}></LoginOut>}></Route>
          <Route path="dashboard" element={<PrivateRoute auth={auth}/>}/>
          <Route path="*" element={<Error404/>}></Route>
        </Routes>
      </Router> */}
    </div>
  );
};

export default ConceptosBasicos;
