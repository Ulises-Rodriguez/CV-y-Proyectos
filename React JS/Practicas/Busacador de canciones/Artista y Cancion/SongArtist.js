import React from 'react';

const SongArtist = ({ artist }) => {
    return (
        <section>
            <h3>{artist.strArtist}</h3>
            <img src={artist.strArtistThumb} alt={artist.strArtist}></img>
            <p>{artist.inBornYear} - {artist.intDiedYear || "Presente"}</p>
            <p>{artist.strCountry}</p>
            <p>{artist.strGenre} - {artist.strStyle}</p>
            <a href={`http://${artist.strWebSite}`} target="_blank" rel='noreferrer'>Sitio web</a>
            <p>{artist.strBiographyEN}</p>
        </section>
    )
}

export default SongArtist;