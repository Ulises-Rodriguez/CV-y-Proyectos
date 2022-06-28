import React from "react";
import { useLocation, useNavigate } from "react-router-dom";

const Productos = () => {
  //para q te aparescan en el serach tenes q definirlo en la url de la pagina http://localhost:3000/productos?inicio=1&fin=20
  // let location = useLocation();
  // console.log(location);

  let { search } = useLocation();
  let query = new URLSearchParams(search);
  //console.log(query);

  const limit = 20;
  let start = parseInt(query.get("inicio")) || 1;
  let end = parseInt(query.get("fin")) || limit;
  //console.log(start,end);


  let navigate = useNavigate();
  //console.log(navigate);

  const handlePrev = (e) => {
    navigate({ search: `?inicio=${start - limit}&fin=${end - limit}` });
  };
  const handleNext = (e) => {
    navigate({ search: `?inicio=${start + limit}&fin=${end + limit}` });
  };

//   const handlePRev = () => {
//     navigate(`?inicio=${start - LIMIT}&fin=${end - LIMIT}`);
//   };
//   const handleNext = () => {
//     navigate(`?inicio=${start + LIMIT}&fin=${end + LIMIT}`);
//   };

  return (
    <div>
      <h3>Productos</h3>
      <p>
        Mostrando productos <b>{start}</b> al <b>{end}</b>
      </p>
      {start > limit && <button onClick={handlePrev}>Atras</button>}
      <button onClick={handleNext}>Adelante</button>
    </div>
  );
};

export default Productos;
