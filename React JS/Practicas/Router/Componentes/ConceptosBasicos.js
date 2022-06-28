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

// - En la versión 6 (https://reactrouter.com/docs/en/v6/hooks/use-navigate) el modulo "Switch" fue remplazado por "routes" por lo cual la importación también cambiará 
// Ejemplo: import { Routes ,Route } from 'react-router-dom';
// -Otro cambió fue que ya no es necesario agregar la propiedad "exact" en las rutas

// -También creo que la sintaxis para definir las rutas a cambiado

// de: <Route path="/" component={Home} />
//  a: <Route path='/welcome' element={<Home/>} />

// Por si alguien le sirve - Hoy 1/18/2022 la version de react router es ahora v6-.
// en la version 6 el componente <Switch> ya no existe , ahora es <Routes> .
// dentro del componente <Routes> ya no se pueden agregar etiquetas JSX todos los hijos de <Routes> tienen que ser componentes.
// en la etiqueta <Route> 
//         Antes: <Route path="/miPath" component={Componente} /> -v5
//         Ahora: <Route path="/miPath" element={<Componente/>}/ > - v6
      
// Esto ya no es permitido:  <Route path="/miPath" children={<Componente/>} /> 
// el atributo exact ya no es necesario porque ahora no sucede el inconveniente de los paths al momento de declarar el / al inicio

// si hay algo que me falto, disculpen, espero haber ayudado a alguien :,3

//deefinico con ruta declarativa
const ConceptosBasicos = () => {

  const [auth, setAuth] = useState(false)

  return (
    <div>
      <h2>Hash Router</h2>
      {/* esta parte es medio complicada asi q atento --> de la forma de abajo de crear las rutas <Router>... cuando lo montas con "build" imagina q el usuario entra a http://localhost:3000/react/props y lo guarda en favoritos o recarga la pagina parado desde ahi la pagina va a dar error 404 ya q va a buscar en la carpeta de build algo q haga referencia a react/props y no lo va a encontrar por lo cual va a tirar error (para q esto no le pasara tendria q iniciar desde el home pero entonces es inutil q guarde cierta parte de la pagina en favoritos xq no va a poder entrar directamente desde ahi) para solucionar este problema usamos el # q nos lo proporciona el <HashRouter> (se puede hacer lo mismo con javascript vanilla (mirar el video mas tarde)) 
      
      y en los <Link> en el to no hace falta poner /#/... el <HashRouter> lo agrega a todo lo q este dentro de el
      
      Recorda q para ver q no sale el error 404 es necesario usar el comando build y live-server o algo parecido
      
      Esto del <HashRouter> es util cuando no tengas una estrategia del lado del backend (osea q no tengas un soporte de q el servidor te va a responder cierto contenido osea cuando no hagas renderizado del lado del servidor o no tengas una carpeta preparada para esa ruta en ese momento utilizas la tecnica del # a traves del React Router), cuando pordia pasar esto --> imagina q tenes una aplicacion q simplemente visualiza la informacion a nivel de frontend q consumis desde una api
      */}
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

      {/* recorda q no es buena practica tener 2 Routers en la misma pagina para eso estan las rutas anidadas */}
     
      <hr></hr>
      <h2>ConceptosBasicos</h2>
      {/*esto en el caso de q lo trabaje con etiquetas <a> <MenuConceptos></MenuConceptos> */}
      <Router>
        {/* si trabajo el nav con el compoenente Link este tiene q ir dentro de Router pero fuera de Routes */}
        <MenuConceptos></MenuConceptos>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/acerca" element={<Acerca/>}></Route>
          <Route path="/contacto" element={<Contacto/>}></Route>
          {/* esto de la /: es la forma q muchas librerias tienen de poner un valor de forma dinamica (se pueden poner mas de una osea /:user/:age) */}
          <Route path="/usuario/:username" element={<Usuario/>}></Route> 
          <Route path="/productos" element={<Productos/>}></Route> 
          <Route path="/productos" element={<Productos/>}></Route>
          {/* Redirecciones */}
          <Route path="/about"  element={ <> <Navigate to="/acerca" /> </> } />
          <Route path="/contact" element={<Navigate to="/contacto" />}></Route>
          {/* Rutas Anidadas */}
          <Route path="react/*" element= {<ReactTopics/>} />
          {/* Rutas Privadas  */}
          <Route path="/login" element={<Login setAuth={setAuth}/>}></Route>
          <Route path="/loginOut" element={<LoginOut setAuth={setAuth}></LoginOut>}></Route>
          {/* <Route path="/dashboard" element={<Dashboard/>}></Route> */}
          <Route path="dashboard" element={<PrivateRoute auth={auth}/>}/>
          {/* <Route path="dashboard" element={auth ? <Dashboard /> : <Navigate to="/login" />}/> */}
          {/* el * es algo asi como un comodin aca lo usamos para especificar cualquier otra pagina q no allamos definido
          tambien es importante definir la ruta del error al final para evitar problemas de jerarquias */}
          <Route path="*" element={<Error404/>}></Route>
        </Routes>
      </Router>
    </div>
  );
};

export default ConceptosBasicos;
