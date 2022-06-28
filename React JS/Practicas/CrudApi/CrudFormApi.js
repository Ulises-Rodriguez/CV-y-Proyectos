import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const initialForm = {
    name: "",
    constelacion: "",
    id: null
}

function CrudFormApi({ createData, updateData, dataToEdit, setDataToEdit }) {

    const [form, setForm] = useState(initialForm);
    let navigate = useNavigate();

    useEffect(() => {
        if (dataToEdit) {
            setForm(dataToEdit);
        }
        else {
            setForm(initialForm);
        }
    }, [dataToEdit])


    const handleChange = (e) => {
        // console.log(e)
        setForm({
            ...form,
            [e.target.name]: e.target.value
        })
        // console.log(form)
    }


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
    }
// navigate(`/santos/editar/${id}`);
    const handleReset = (e) => {
        setForm(initialForm);
        setDataToEdit(null);
        navigate("/santos")
    }

    return (
        <div>
            <h3>{dataToEdit ? "Editar" : "Agregar"}</h3>
            <form onSubmit={handleSubmit}>
                <input type="text" name='name' placeholder='nombre' onChange={handleChange} value={form.name}></input>
                <input type="text" name='constelacion' placeholder='constelacion' onChange={handleChange} value={form.constelacion}></input>
                <input type="submit" value="enviar" onSubmit={handleSubmit}></input>
                <input type="reset" value="limpiar" onClick={handleReset}></input>
            </form>
        </div>
    )
}

export default CrudFormApi;