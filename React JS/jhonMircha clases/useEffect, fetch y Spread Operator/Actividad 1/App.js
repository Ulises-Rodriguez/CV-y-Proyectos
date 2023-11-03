import './App.css';
import './miCss.css';
import { useEffect, useState } from 'react';

const App = () => {

  const [joke, setJoke] = useState("");

  const newJoke = () => {
    const url = "https://api.icndb.com/jokes/random";
    const peticion = fetch(url)

    peticion.then(datos => datos.json())
      .then(lectura => {
        console.log(lectura);
        setJoke(lectura.value.joke);
      })
      .catch(console.log("error"));
  }

  useEffect(() => {
    newJoke();
  }, []);


  return (
    <>
      <button className='newJoke' onClick={newJoke}>Obtener broma del bueno de Chuck</button>
      {joke}
    </>
  )
}

export default App;