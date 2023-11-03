import { alertSweet } from '../funJS/alertSweet'


export const comprobarDatos = (obj)=>{
    const { email, email2 } = obj;

    for (const key in obj) {
        if (obj[key] === "") {
            alertSweet('error','Ocurrio un problema','Todos los campos del formulario deben de estar completos')
            return false;
        }
    }

    if (email !== email2) {
        alertSweet('error','Ocurrio un problema','Los campos "Email" y "Confirmar Email" deben de ser iguales')
        return false;
    }

    return true;
}