import React from 'react'
import { Productos } from './Productos';

const array = [
    "https://m.media-amazon.com/images/I/81s7B+Als-L._SL1500_.jpg",
    "https://thegameisland.com/cdn/shop/products/57_6ee06d87-18f0-4e35-8206-531a405268c0_800x.jpg?v=1612803353",
    "https://http2.mlstatic.com/D_NQ_NP_671397-MLA71504170436_092023-O.webp",
]

export const Consolas = () => {

    return <Productos url={"consolas"} array={array} />
}
