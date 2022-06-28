import React,{useReducer} from 'react';
import { TYPES } from '../useReducer/actons/shoppingActions';
import { shoppingInitialState, shoppingReducer } from '../useReducer/reducers/shoppingReducer';
import CartItem from './CartItem';
import ProductItem from './ProductItem';

const ShoppingCart = () => {

  const [state, dispatch] = useReducer(shoppingReducer, shoppingInitialState);
  
  const {products,cart} = state;

    const addToCart = (id)=>{
      dispatch({type : TYPES.ADD_TO_CART, payload : id});
    };

    const delFromCart = (id , all = false)=>{
      if (all) {
        dispatch({type : TYPES.REMOVE_ALL_FROM_CART, payload : id});
      }else{
        dispatch({type : TYPES.REMOVE_ONE_FROM_CART, payload : id});
      }
    };

    const clearCart = ()=>{
      dispatch({type : TYPES.CLEAR_CART})
    };

  return (
    <div>
        <h2>Carrito de compras</h2>
        <h3>Productos</h3>
        <article className='box grid-responsive'>
            {products.map((product)=><ProductItem key={product.id} data={product} addToCart={addToCart}></ProductItem>)}
        </article>
        <h3>Carrito</h3>
        <article className='box'>
          <button onClick={clearCart}>Limpiar carrito</button>
          {/* si pones {} no funciona tienen q ser () */}
          {cart.map((item,index)=>(<CartItem key={index} data={item} delFromCart={delFromCart}></CartItem>))}
        </article>
    </div>
  )
}

export default ShoppingCart;