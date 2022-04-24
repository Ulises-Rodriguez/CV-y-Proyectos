import './App.css';
import './miCss.css';
import { useEffect, useState } from 'react';

const App = () => {

  const [jokes, setJokes] = useState([]);

  const url = "https://api.icndb.com/jokes";
  const peticion = fetch(url);

  useEffect(()=>{
    peticion.then(datos=>datos.json())
            .then(lectura=>{
              console.log(lectura);
              lectura.value.map(chistes=>{
                  setJokes(elements => [...elements, <div className='ch' key={chistes.id}>{chistes.id}:{chistes.joke}</div>])
              })
            })
            .catch(rej=>console.log(rej));
  });

  return (
    <>
      <h1>Chistes de Chuck</h1>
      {jokes}
    </>
  )
}

export default App;

