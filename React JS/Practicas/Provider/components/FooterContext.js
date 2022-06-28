import React,{useContext} from 'react';
import ThemeContext from "../context/ThemeContext";
import LanguageContext from "../context/LanguageContext";

const FooterContext = () => {

  const {theme} = useContext(ThemeContext);
  const {text} = useContext(LanguageContext);

  return (
    <div>
        <footer className={theme}>
          <h4>{text.footerTitle}</h4>
        </footer>
    </div>
  )
}

export default FooterContext;