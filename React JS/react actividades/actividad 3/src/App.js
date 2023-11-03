import './App.css';
import Palabra from './componentes/Palabra';
// import Imagen from './componentes/Imagen';
import Letras from './componentes/Letras';
import { Datos } from './contexto/Contexto';
import Pregunta from './componentes/Pregunta';


//useRef es como usar los querySelector, no te olvides di importarlo
// const refCaja = ();
//<div className="caja" ref={refCaja}
//para usarlo --> variable = refCaja.current (podes usar innerHTML o otros)

//contexto
//createContext para crear el contexto --> crear el lugar para guardar toda la info
//useContext permite acceder a esa info o modificarla
//las props siguen siendo utiles siempre y cuando tengas pocos componentes padre hijo, ya q si los componentes hijos tienen hijos es paso de propiedades se vuelve medio complicado ademas puede q el componente nieto no necesite todas las propiedades q pasa el componente abuelo(osea el padre original)
//no te olvides de importarlo --> import {Datos} from "./...." (los {} ya q Datos no es un directorio sino una variable donde se guardan los datos, no confundas el fichero donde se crear el contexto al fichero de donde se acceden a la info)
function App() {
  return (
    <>
      <Datos>
        <Pregunta></Pregunta>
        <Palabra></Palabra>
        <Letras></Letras>
      </Datos>
    </>
  );
}

export default App;
