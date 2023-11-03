export const obtenerProducto = (id, productos) => {
    
    return productos.find(producto => producto.id.toString() === id);
}