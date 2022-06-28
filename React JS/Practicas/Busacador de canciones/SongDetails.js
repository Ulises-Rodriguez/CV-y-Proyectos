import React from 'react';
import Message from '../Components/Message';
import SongArtist from './Artista y Cancion/SongArtist';
import SongLyric from './Artista y Cancion/SongLyric';

const SongDetails = ({ search, lyric, bio }) => {

    if (!lyric || !bio) {
        return null;
    } else {
        return (
            <>
                {lyric.error || lyric.err || lyric.name === "AbortError" ? <Message msg={`Error: no existe la cancion ${search.song}`} bgColor="#dc3545"></Message> : <SongLyric title={search.song} lyrics={lyric.lyrics}></SongLyric>}
    
                {bio.artists ? <SongArtist artist={bio.artists[0]}></SongArtist> : <Message msg={`Error: no existe el interprete ${search.artist}`} bgColor="#dc3545"></Message>}
            </>
        )
    }

}

export default SongDetails;