import React, { createRef, useRef } from 'react';

function Referencias() {

    let refBtn = useRef();
    let refMenu = useRef();

    console.log(refMenu, refBtn);

    const handelToggleMenu = (e) => {
        if (refBtn.current.textContent === "Menu") {
            refBtn.current.textContent = "cerrar";
            refMenu.current.style.display = "block";
        } else {
            refBtn.current.textContent = "Menu";
            refMenu.current.style.display = "none";
        }
    }

    // const handelToggleMenu = (e) => {
    //     const menu = document.getElementById("menu");

    //     if (e.target.textContent === "menu") {
    //         e.target.textContent = "cerrar";
    //         menu.style.display = "block";
    //     } else {
    //         e.target.textContent = "menu";
    //         menu.style.display = "none";
    //     }
    // }

    return (
        <>
            <h2>Referencias</h2>
            <button id='menu-btn' ref={refBtn} onClick={handelToggleMenu}>Menu</button>
            <nav id='menu' ref={refMenu} style={{ display: "none" }}>
                <a href='#'>Seccion 1</a><br />
                <a href='#'>Seccion 2</a><br />
                <a href='#'>Seccion 3</a><br />
                <a href='#'>Seccion 4</a><br />
                <a href='#'>Seccion 5</a><br />
            </nav>

        </>
    )
}

export default Referencias;