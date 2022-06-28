import React from "react";
import { useNavigate } from "react-router-dom";

const SongTableRow = ({ id, el, handleDeleteSong }) => {
  
  console.log(el);

  let {bio,search} = el;
  let avatar = bio.artists[0].strArtistThumb;
  let avatarStyle = {
    width:"40px",
    heigth:"40px",
  }

  let navigate = useNavigate();

  return (
    <tr>
      <td>
        <img style={avatarStyle} src={avatar} alt={search.artist}></img>
      </td>
      <td>{search.artist}</td>
      <td>{search.song}</td>
      <td>
        <button onClick={() => navigate(`/canciones/${id}`)}>Ver</button>
        <button onClick={() => handleDeleteSong(id)}>Eliminar</button>
      </td>
    </tr>
  );
};

export default SongTableRow;
