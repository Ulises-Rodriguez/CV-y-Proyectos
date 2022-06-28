import { createContext, useState } from "react";

//con "createContext()" se crea un contexto
const ThemeContext = createContext();

const initialTheme = "light";

const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(initialTheme);

  const handleTheme = (e) => {
    // console.log(e);
    // console.log(e.target.value);
    if (e.target.value === "light") {
      setTheme("light");
    } else {
      setTheme("dark");
    }
  };

  const data = {
      theme,
      handleTheme,
  };

  return (
    // con el Provider provemos (damos) las props q van a usar los children
    //se recomineda pasar un objeto con las props q se le van a pasar
    //el nombre no tiene q ser value
    <ThemeContext.Provider value={data}>{children}</ThemeContext.Provider>
  );
};

export { ThemeProvider };
export default ThemeContext;
