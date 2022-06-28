import React, { useState } from 'react';

const initialForm = {
    artist: "",
    song: "",
};

const SongForm = ({ handleSearch, handleSaveSong }) => {

    //recorda q lo ideal es tener los formularios controlados a travez de una variable de estado
    const [form, setForm] = useState(initialForm);
    //esta variable es para hacer q se el boton de Agregar cancion no este disponible hasta q la cancion se alla buscado xq sino se podria guardar una cancion q no trae nada
    const [isDisable, setIsDisable] = useState(true);

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!form.artist || !form.song) {
            alert("Datos incompletos");
            setIsDisable(true);
            return;
        }

        handleSearch(form);
        setForm(initialForm);
        setIsDisable(false);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" name="artist" placeholder='Nombre del interprete interprete' onChange={handleChange} value={form.artist}></input>
                <input type="text" name="song" placeholder='Nombre de la cancion' onChange={handleChange} value={form.song}></input>
                <input type="submit" value="Enviar"></input>
                <input type="button" onClick={handleSaveSong} value="Agregar Cancion" disabled={isDisable && "disable"}></input>
            </form>
        </div>
    )
}

export default SongForm;