import React, { useContext, useEffect, useRef, useState } from "react";
import { Contexto } from "../contexto/Contexto";
import Imagen from "./Imagen";
import aImg1 from "../assets/el_ahorcado1.png";
import aImg2 from "../assets/el_ahorcado2.png";
import aImg3 from "../assets/el_ahorcado3.png";
import aImg4 from "../assets/el_ahorcado4.png";
import aImg5 from "../assets/el_ahorcado5.png";
import aImg6 from "../assets/el_ahorcado6.png";

const Letras = () => {
  const {
    numRandom,
    setNumRandom,
    palabra,
    setPalabra,
    setPregunta,
    PALABROS,
    count,
    setCount,
    correct,
    setCorrect,
    misLetras,
    setMisLetras
  } = useContext(Contexto);

  const divContainer = useRef(null);

  const [srcImg, setSrcImg] = useState("");

  const verificar = (e) => {
    let letra = e.target.innerHTML;
    setMisLetras([...misLetras,letra]);


    if (letra === "RESET") {

      let divLength = divContainer.current.children.length;

      setNumRandom(Math.floor(Math.random() * PALABROS.length));
      setPregunta(PALABROS[numRandom]["pregunta"]);
      setPalabra(PALABROS[numRandom]["palabro"]);
      setCount(0);
      setCorrect(0);
      setMisLetras([]);

      for (let btn = 0; btn < divLength; btn++) {
        divContainer.current.children[btn].style = "";
      }

    } else if (palabra.includes(letra)) {
      e.target.style.backgroundColor = "green";
      setCorrect(correct+1);
    } else {
      setCount(count + 1);
      e.currentTarget.style.backgroundColor = "red";
    }

  };

  const crearLetras = () => {
    const letras = [
      "reset",
      "a",
      "b",
      "c",
      "d",
      "e",
      "f",
      "g",
      "h",
      "i",
      "j",
      "k",
      "l",
      "ñ",
      "m",
      "n",
      "o",
      "p",
      "q",
      "r",
      "s",
      "t",
      "u",
      "v",
      "w",
      "x",
      "y",
      "z",
    ];

    return letras.map((letra) => (
      <button
        key={letra}
        type="button"
        className="btnLetra"
        onClick={verificar}
      >
        {letra.toUpperCase()}
      </button>
    ));
  };

  useEffect(() => {
    if (count === 1) {
      setSrcImg(aImg1);
    } else if (count === 2) {
      setSrcImg(aImg2);
    } else if (count === 3) {
      setSrcImg(aImg3);
    } else if (count === 4) {
      setSrcImg(aImg4);
    } else if (count === 5) {
      setSrcImg(aImg5);
    } else if (count === 6) {
      setSrcImg(aImg6);
      alert("Has perdido dale al boton de reset");
    }
    
    if (correct === palabra.length) {
      alert("Has ganado dale al boton de reset para jugar de nuevo");
      setCorrect(0);
    }
    
  }, [count,correct,palabra,setCorrect]);

  return (
    <>
      <div className="btnContainer" ref={divContainer}>
        {crearLetras()}
      </div>
      <Imagen count={count} srcImg={srcImg}></Imagen>
    </>
  );
};

export default Letras;
