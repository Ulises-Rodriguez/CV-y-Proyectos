import Idiomas from './ficheros App/El CONTEXTO de React (useContext)/Actividad 1/componentes/Idiomas';
import Info from './ficheros App/El CONTEXTO de React (useContext)/Actividad 1/componentes/Info';
import Provider from './ficheros App/El CONTEXTO de React (useContext)/Actividad 1/contexto/Provider';
import './miCss.css';


const App = () => {

  return (
    <Provider>
      <div className='banderas'>
        <Idiomas></Idiomas>
      </div>
      <div className='contenido'>
        <Info></Info>
      </div>
    </Provider>
  )
}

export default App;

