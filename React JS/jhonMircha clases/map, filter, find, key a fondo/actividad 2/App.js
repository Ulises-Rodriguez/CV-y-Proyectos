import './App.css';
import './miCss.css';
import Actividad2 from './ficheros App/map, filter, find, key a fondo/actividad 2/Actividad2';


const App = () => {

  const reyes = [
    {
      nombre: "Atanagildo",
      reinado: 15,
      vacasComidas: 9
    }, {
      nombre: "Ervigio",
      reinado: 7,
      vacasComidas: 3
    }, {
      nombre: "Ataúlfo",
      reinado: 5,
      vacasComidas: 16
    }, {
      nombre: "Leovigildo",
      reinado: 18,
      vacasComidas: 3
    }, {
      nombre: "Sisebuto",
      reinado: 9,
      vacasComidas: 13
    }, {
      nombre: "Recesvinto",
      reinado: 19,
      vacasComidas: 11
    }, {
      nombre: "Teodorico",
      reinado: 33,
      vacasComidas: 12
    }
  ]
  
  return (
    <div className='container'>
      <Actividad2 reyes={reyes}></Actividad2>
    </div>
  )
}

export default App;

