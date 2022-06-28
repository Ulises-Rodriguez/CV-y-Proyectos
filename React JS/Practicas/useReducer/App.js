import ShoppingCart from "./components/ShoppingCart";
import CrudApi from "./CrudApi/CrudApi";
import Contador from "./useReducer/Contador";
import ContadorMejorado from "./useReducer/ContadorMejorado";

function App() {
  return (
    <div className="App">
      <CrudApi></CrudApi>
      <hr></hr>
      <ShoppingCart></ShoppingCart>
      <hr></hr>
      <ContadorMejorado></ContadorMejorado>
      <hr></hr>
      <Contador></Contador>
    </div>
  );
}

export default App;
