import React, { useState, useEffect, useContext } from "react";
import CrudContext from "./CrudContext/CrudContext";

const initialForm = {
  name: "",
  constelacion: "",
  id: null,
};

function CrudFormApi() {
  const { createData, updateData, dataToEdit, setDataToEdit } = useContext(CrudContext);

  const [form, setForm] = useState(initialForm);

  useEffect(() => {
    if (dataToEdit) {
      setForm(dataToEdit);
    } else {
      setForm(initialForm);
    }
  }, [dataToEdit]);

  const handleChange = (e) => {
    // console.log(e)
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
    // console.log(form)
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!form.name || !form.constelacion) {
      alert("Datos inclopletos");
      return;
    }

    if (form.id === null) {
      createData(form);
    } else {
      updateData(form);
    }

    handleReset();
  };

  const handleReset = (e) => {
    setForm(initialForm);
    setDataToEdit(null);
  };

  return (
    <div>
      <h3>{dataToEdit ? "Editar" : "Agregar"}</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="nombre"
          onChange={handleChange}
          value={form.name}
        ></input>
        <input
          type="text"
          name="constelacion"
          placeholder="constelacion"
          onChange={handleChange}
          value={form.constelacion}
        ></input>
        <input type="submit" value="enviar" onSubmit={handleSubmit}></input>
        <input type="reset" value="limpiar" onClick={handleReset}></input>
      </form>
    </div>
  );
}

export default CrudFormApi;
