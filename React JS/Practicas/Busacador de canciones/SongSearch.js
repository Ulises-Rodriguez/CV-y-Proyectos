import React, { useEffect, useState } from "react";
import { HashRouter, Link, Route, Routes } from "react-router-dom";
import Loader from "../Components/Loader";
import { helpHTTP } from "../helpers/helpHTTP";
import Error404 from "../Router/pages/Error404";
import SongPage from "../Router/pages/SongPage";
import SongDetails from "./SongDetails";
import SongForm from "./SongForm";
import SongTable from "./SongTable";

//recorda q la api de las canciones daba problemas xq ahora era de pago o algo asi, ademas daba problemas por los CORDS (asi q es muy probable q no ande pero la idea del ejercicio es reutilizar componentes y React Router)

//a mySongsInit le asignamos el valor parseado (xq sino nos viene en texto) de mySongs guardado en localStorage pero si no lo encuentra o todavia no se creo le asignamos un array vacio
let mySongsInit = JSON.parse(localStorage.getItem("mySongs")) || [];

function SongSearch() {
  const [search, setSearch] = useState(null);
  const [lyric, setLyric] = useState(null);
  const [bio, setBio] = useState(null);
  const [loading, setLoading] = useState(false);
  //variable para poder guardar nuestras canciones favoritas
  const [mySongs, setMySongs] = useState(mySongsInit);


  useEffect(() => {
    if (search == null) {
      return;
    }

    const fetchData = async () => {

      const { artist, song } = search;
      console.log(search)

      let artistURL = `https://www.theaudiodb.com/api/v1/json/2/search.php?s=${artist}`;
      let songURL = `https://api.lyrics.ovh/v1/${artist}/${song}`;

      // console.log(artistURL, songURL);

      setLoading(true);

      //CREO Q EL CODIGO ESTA BIEN PERO POR UN PROBLEMA DE LA PAGINA DE LIRYCS NO TE DEJA BUSCAR LA CANCION POR LO Q EL PROMISE DA PROBELMAS
      const [artistRes, songRes] = await Promise.all([
        helpHTTP().get(artistURL),
        helpHTTP().get(songURL),
      ]);

      // console.log(artistRes, songRes);

      setBio(artistRes);
      setLyric(songRes);

      setLoading(false);
    };

    fetchData();

    localStorage.setItem("mySongs", JSON.stringify(mySongs));
  }, [search, mySongs]);

  const handleSearch = (data) => {
    // console.log(data);
    setSearch(data);
  };

  const handleSaveSong = () => {
    alert("Cancion guardada en favoritas");
    let currentSong = {
      search,
      lyric,
      bio,
    }

    let songs = [...mySongs,currentSong];

    setMySongs(songs);
    setSearch(null);
    localStorage.setItem("mySongs",JSON.stringify(songs));
  }

  const handleDeleteSong = (id) => {
    alert(`Eliminando canion con el id:${id}`);
    let isDelete = window.confirm("Estas seguro de eliminar esta cancion");

    if (isDelete) {
      // cuando el indice sea distinto del id lo agragas a mySongs y con este filtro excluimos la cancion q queremos eleminar
      let songs = mySongs.filter((el,index)=> index !== id);
      setMySongs(songs);
      localStorage.setItem("mySongs",JSON.stringify(songs));
    }
  }

  return (
    <>
      <HashRouter>
        <header>
          <h2>SongSearch</h2>
          <Link to="/canciones">Home</Link>
        </header>
        {loading && <Loader></Loader>}
        <article className="grid1-2">
          <Routes>
            <Route
              path="/canciones"
              element={
                <>
                  <SongForm handleSearch={handleSearch} handleSaveSong={handleSaveSong}></SongForm>
                  <SongTable mySongs={mySongs} handleDeleteSong={handleDeleteSong}></SongTable>
                  {search && !loading && (
                    <SongDetails
                      search={search}
                      lyric={lyric}
                      bio={bio}
                    ></SongDetails>
                  )}
                </>
              }
            ></Route>
            {/* xq le paso a SongPage mySongs? bueno esto es xq en mySongs tengo la info q se guarda en localStorage, al pasarle todo luego en SongPage hago un filtro para q me mueste solo la cancion q coincida con el id, por eso le paso el conjunto de las canciones */}
            <Route path="/canciones/:id" element={<SongPage mySongs={mySongs}></SongPage>}></Route>
            <Route path="/*" element={<Error404></Error404>}></Route>
          </Routes>
        </article>
      </HashRouter>
    </>
  );
}

export default SongSearch;