import React from "react";
import { useParams } from "react-router-dom";
import SongDetails from "../../Busacador de canciones/SongDetails";

const SongPage = ({mySongs}) => {

    let {id} = useParams();
    console.log(id,mySongs,mySongs[id]);

    let currentSong = mySongs[id];

    let {search,lyric,bio} = currentSong;

  return <SongDetails search={search} lyric={lyric} bio={bio}></SongDetails>;
};

export default SongPage;
