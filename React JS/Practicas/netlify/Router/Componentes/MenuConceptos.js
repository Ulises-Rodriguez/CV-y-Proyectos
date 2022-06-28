import React from "react";
import { Link, NavLink } from "react-router-dom";

// Para la ultima actualización de react-router-dom, no es necesario especificar la propiedad exact en el NavLink, ademas la propiedad 'activeClassName' debe estar en minúsculas:

// <nav>
//                 <NavLink activeclassname="active" to="/">Home</NavLink>
//                 <NavLink activeclassname="active" to="/about">About</NavLink>
//                 <NavLink activeclassname="active" to="/contact">Contac</NavLink>
// </nav>


const MenuConceptos = () => {
  return (
    <nav>
      <ol>
        {/* de esta forma podemos movernos entre nuestras rutas pero cada vez q cambiamos se carga o mejor dicho renderiza todo el DOM otra ves (inspecciona los elementos para ver el cambio) */}
        <li>
          <span>Menu con enlaces html (no recomendado)</span>
          <a href="/">Home</a>
          <a href="/acerca">Acerca</a>
          <a href="/contacto">Contacto</a>
        </li>
        <li>
          {/* este componente Link funciona igual q una etiqueta <a></a> pero con la diferencia de q en ves de usar href se usa to y bueno la otra diferencia mas obvia es q uno es un componenete y el otro una etiqueta html
          otra diferencia es q tiene q ir dentro de el compoenente q envuelve todo --> Router*/}
          {/* ademas si los inspeccionas se ve q son elementos <a></a> pero trabajados internamentes con la logica de React Router DOM */}
          <span>Componente Link</span>
          <Link to="/">Home</Link>
          <Link to="/acerca">Acerca</Link>
          <Link to="/contacto">Contacto</Link>
          <Link to="/no-exitste">Error 404</Link>
        </li>
        <li>
            {/* se comporta igual q link  */}
            <span>Componente nav Link</span>
            {/* activeclassname nos permite dar una propiedad css */}
            <NavLink to="/" activeclassname="active">Home</NavLink>
            <NavLink to="/acerca" activeclassname="active">Acerca</NavLink>
            <NavLink to="/contacto" activeclassname="active">Contacto</NavLink>
        </li>
        <li>
          <span>Parametros</span>
          <Link to="/usuario/Tino">Tino</Link>
          <Link to="/usuario/Ludmi">Ludmi</Link>
        </li>
        <li>
          <span>Parametros de consulta</span>
          <Link to="/productos">Productos</Link>
        </li>
        <li>
          <span>Redirecciones</span>
          <Link to="/about">About</Link>
          <Link to="/contact">Contact</Link>
        </li>
        <li>
          <span>Rutas Anidadas</span>
          <Link to="/react">React</Link>
        </li>
        <li>
          <span>Rutas privadas</span>
          <Link to="/login">Login</Link>
          <Link to="/loginOut">LoginOut</Link>
          <Link to="/dashboard">Dashboard</Link>
        </li>
      </ol>
    </nav>
  );
};

export default MenuConceptos;
