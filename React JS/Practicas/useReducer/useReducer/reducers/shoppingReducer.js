import { TYPE, TYPES } from "../actons/shoppingActions";

export const shoppingInitialState = {
  products: [
    {
      id: 1,
      name: "Poducto 1",
      price: 100,
    },
    {
      id: 2,
      name: "Poducto 2",
      price: 200,
    },
    {
      id: 3,
      name: "Poducto 3",
      price: 300,
    },
    {
      id: 4,
      name: "Poducto 4",
      price: 400,
    },
    {
      id: 5,
      name: "Poducto 5",
      price: 500,
    },
    {
      id: 6,
      name: "Poducto 6",
      price: 600,
    },
  ],
  cart: [],
};

export const shoppingReducer = (state, action) => {
  switch (action.type) {
    case TYPES.ADD_TO_CART: {
      let newItem = state.products.find(
        (product) => product.id === action.payload
      );

      let itemInCart = state.cart.find((item) => item.id === newItem.id);

      return itemInCart
        ? {
            ...state,
            cart: state.cart.map((item) =>
              item.id === newItem.id
                ? { ...item, quantity: item.quantity + 1 }
                : // si al item lo pones entre {} no da error pero hace q cuando agregas varios de un producto distinto al anterior los pisa
                  item
            ),
          }
        : { ...state, cart: [...state.cart, { ...newItem, quantity: 1 }] };
    }
    case TYPES.REMOVE_ONE_FROM_CART: {
      // busca dentro del estado, en el carrito, encuentra, te voy a pasar un item, por cada item evalua lo siguente, del item.id q sea igual al action.payload
      let itemToDelete = state.cart.find((item) => item.id === action.payload);
      // al igual q con el add q haciamos q aumentara la cantidad de quantity aca hacemos lo mismo pero al reves pero tenemos q controlar cuando la cantidad llegue a 0 xq sino vamos a empezar a tener negativos cantidad de productos
      return itemToDelete.quantity > 1
        ? {
            // hacemos una copia del estado con la ayuda del spread oprator y luego nos enfocamos en atributo cart
            ...state,
            // accedemos a la propiedad cart y usamos el map para generar un nuevo arreglo
            // caso quantity > 1 : por cada item q te pase va a evaluar item.id corresponde al action.payload entonces si el item coincide con el payload le restamos 1 a la cantidad quantity caso contrario retornamos el item tal cual esta
            // caso contrario : cuando no sea mayor q 1 entoces es el utlimo elemento q nos queda , entonces hacemos una copia del estado y luego modificamos el carrito del state.cart filtra por cada item q resive este filtro evaluan q cuando el item.id sea =! al action.payload se va a agregar a este nuevo arreglo
            cart: state.cart.map((item) =>
              item.id === action.payload
                ? { ...item, quantity: item.quantity - 1 }
                : item
            ),
          }
        : {
            ...state,
            cart: state.cart.filter((item) => item.id !== action.payload),
          };
    }
    case TYPES.REMOVE_ALL_FROM_CART: {
      return {
        ...state,
        cart: state.cart.filter((item) => item.id !== action.payload),
      };
    }
    case TYPES.CLEAR_CART: {
      return shoppingInitialState;
    }
    default:
      return state;
  }
};
