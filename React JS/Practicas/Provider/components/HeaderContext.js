import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";
import LanguageContext from "../context/LanguageContext";
import ThemeContext from "../context/ThemeContext";

const HeaderContext = () => {
  //recorda q tambien podrias darle un nombre y despues acceder a los valores con "nombre".theme, etc
  //useContext recive como parametro el contexto q se a creado oseatenemos q llamar a ThemeContext
  const { theme, handleTheme } = useContext(ThemeContext);
  const {text,handleLanguage} = useContext(LanguageContext);
  const {auth,handleAuth} = useContext(AuthContext);
  
  return (
    <div>
      <header className={theme}>
        <h2>{text.headerTitle}</h2>
        <h3>{text.headerSubtitle}</h3>
        <select name="languaje" onChange={handleLanguage}>
          <option value="es">Español</option>
          <option value="en">English</option>
        </select>
        <input
          type="radio"
          name="theme"
          id="light-context"
          onClick={handleTheme}
          value="light"
        ></input>
        <label htmlFor="light-context">{text.headerLight}</label>
        <input
          type="radio"
          name="theme"
          id="dark-context"
          onClick={handleTheme}
          value="dark"
        ></input>
        <label htmlFor="dark-context">{text.headerDark}</label>
        <button onClick={handleAuth}>
          {auth ? text.buttonLogout : text.buttonLogin}
        </button>
      </header>
    </div>
  );
};

export default HeaderContext;
