import React, { useState } from "react";
import Footer from "./Footer";
import Header from "./Header";
import Main from "./Main";

const initialTheme = "ligth";
const initialLanguage = "es";

const translations = {
  es: {
    headerTitle: "Mi aplicación SIN Context API",
    headerSubtitle: "Mi cabecera",
    headerLight: "Claro",
    headerDark: "Oscuro",
    buttonLogin: "Iniciar Sesión",
    buttonLogout: "Cerrar Sesión",
    mainWelcome: "Bienvenid@ invitad@",
    mainHello: "Hola Usuari@",
    mainContent: "Mi contenido principal",
    footerTitle: "Mi pié de página",
  },
  en: {
    headerTitle: "My application without Context API",
    headerSubtitle: "My header",
    headerLight: "Light",
    headerDark: "Dark",
    buttonLogin: "Login",
    buttonLogout: "Logout",
    mainWelcome: "Welcome Guest",
    mainHello: "Hello User",
    mainContent: "My main content",
    footerTitle: "My footer",
  },
};

const initialAuth = null;

const MyPage = () => {
  const [theme, setTheme] = useState(initialTheme);
  const [language, setLanguage] = useState(initialLanguage);
  //al objetos podes acceder con la notacion del . pero tambien con los [], osea poner translations[language] es lo mismo q poner translations.es
  const [text, setText] = useState(translations[language]);
  const [auth, setAuth] = useState(initialAuth);

  // console.log(text);

  const handleTheme = (e) => {
    // console.log(e);
    // console.log(e.target.value);
    if (e.target.value === "light") {
      setTheme("light");
    } else {
      //recorda q a todos los componentes les pasamos theme como propiedad y definimos en el index.css una clase llamada dark
      setTheme("dark");
    }
  };

  const handleLanguage = (e) => {
    // console.log(e.target.value);
    if (e.target.value === "es") {
      setLanguage("es");
      setText(translations.es);
    } else {
      setLanguage("en");
      setText(translations.en);
    }
  };

  const handleAuth = (e)=>{
    if (auth) {
      setAuth(null);
    } else {
      setAuth(true);
    }
  };

  return (
    <div className="my-page">
      <Header
        theme={theme}
        text={text}
        handleTheme={handleTheme}
        handleLanguage={handleLanguage}
        auth = {auth}
        handleAuth={handleAuth}
      ></Header>
      <Main theme={theme} text={text} auth={auth}></Main>
      <Footer theme={theme} text={text}></Footer>
    </div>
  );
};

export default MyPage;
