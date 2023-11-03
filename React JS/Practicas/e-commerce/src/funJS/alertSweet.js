import Swal from 'sweetalert2'


export const alertSweet = (icono,titulo,msg)=>{
    Swal.fire({
        icon: `${icono}`,
        title: `${titulo}`,
        text: `${msg}`,
    })
}