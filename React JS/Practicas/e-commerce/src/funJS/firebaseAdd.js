import { addDoc, collection, getFirestore } from "firebase/firestore";

export const addToFireStore = async (nombreColeccion, obj) => {

        const db = getFirestore();

        const docRef = await addDoc(collection(db, nombreColeccion),obj);

        return docRef.id;
}