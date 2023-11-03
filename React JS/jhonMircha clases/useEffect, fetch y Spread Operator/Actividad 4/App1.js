import React, { useState, useEffect } from "react";



const App = () => {

  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    console.log("Movimiento Scroll");

    const detectarScroll = () => setScrollY(window.pageYOffset);

    window.addEventListener("scroll", detectarScroll);

    return () => {
      window.removeEventListener("scroll", detectarScroll);
    }
  }, [scrollY])

  useEffect(() => {
    console.log("Fase de Montaje");
  }, [])

  useEffect(() => {
    console.log("Fase de Actualizacion");
  })

  useEffect(() => {
    return () => {
      console.log("Fase de Desmontaje");
    }
  })

  return (
    <>
      <h2>Hooks - useEffect y Ciclo de vida</h2>
      <h3>Scroll Y del navegador {scrollY}px</h3>
    </>
  );
}

export default App;

