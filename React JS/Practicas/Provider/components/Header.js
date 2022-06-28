import React from "react";

const Header = ({
  theme,
  handleTheme,
  text,
  handleLanguage,
  auth,
  handleAuth,
}) => {
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
          id="light"
          onClick={handleTheme}
          value="light"
        ></input>
        <label htmlFor="light">{text.headerLight}</label>
        <input
          type="radio"
          name="theme"
          id="dark"
          onClick={handleTheme}
          value="dark"
        ></input>
        <label htmlFor="dark">{text.headerDark}</label>
        <button onClick={handleAuth}>
            {auth ? text.buttonLogout : text.buttonLogin}
        </button>
      </header>
    </div>
  );
};

export default Header;
