import React from "react";
import { AuthProvider } from "../context/AuthContext";
import { LanguageProvider } from "../context/LanguageContext";
import { ThemeProvider } from "../context/ThemeContext";
import FooterContext from "./FooterContext";
import HeaderContext from "./HeaderContext";
import MainContext from "./MainContext";

const MyPageContext = () => {
  return (
    <div className="my-page">
      {/* el orden de cual va a dentro de cual no importa realmente */}
      <ThemeProvider>
        {/* entonces si comparas ahora en el caso de la props theme, en este caso nuetros 3 componentes ya no la necesitan ya q la van a estar consumiendo del Provider 
        No olvidar q ahora hay q editar los componentes ya q el theme y handleTheme ya no las extrae de las props, tenemos q hacer q las extraiga del archivo del contexto*/}
        <LanguageProvider>
          <AuthProvider>
            <HeaderContext></HeaderContext>
            <MainContext></MainContext>
            <FooterContext></FooterContext>
          </AuthProvider>
        </LanguageProvider>
      </ThemeProvider>
    </div>
  );
};

export default MyPageContext;
