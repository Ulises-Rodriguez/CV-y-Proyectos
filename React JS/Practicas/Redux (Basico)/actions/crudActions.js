// export const TYPES = {
//     CREATE_DATA : "CREATE_DATA",
//     READ_ALL_DATA : "READ_ALL_DATA",
//     //READ_ONE_DATA : "READ_ONE_DATA",
//     UPDATE_DATE : "UPDATE_DATE",
//     DELETE_DATA : "DELETE_DATA",
//     NO_DATA : "NO_DATA",
// }

import { CREATE_DATA, DELETE_DATA, NO_DATA, READ_ALL_DATA, UPDATE_DATE } from "../types";

export const createAction = (data)=>({type : CREATE_DATA, payload : data});
export const readAllAction = (data)=>({type : READ_ALL_DATA, payload : data});
export const updateAction = (data)=>({type : UPDATE_DATE, payload : data});
export const deleteAction = (id)=>({type : DELETE_DATA, payload : id});
export const noAction = ()=>({type : NO_DATA});