import React from 'react';
import {Link} from 'react-router-dom';

export const LiElementos = ({ nombre, url }) => {
    return (
        <li className="nav-item">
            <Link to={url} className='nav-link'>{nombre}</Link>
            {/* <a className="nav-link" aria-current="page" href={url}>{nombre}</a> */}
        </li>
    )
}
