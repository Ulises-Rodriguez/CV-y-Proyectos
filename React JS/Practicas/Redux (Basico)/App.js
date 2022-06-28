import TeoriaRedux from "./components/TeoriaRedux";
import { Provider } from "react-redux";
import store from "./store";
import Contador from "./components/Contador";
import ShoppingCart from "./components/ShoppingCart";
import CrudApi from "./components/CrudApi";

function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <h1>Redux</h1>
        <hr></hr>
        <CrudApi></CrudApi>
        <hr></hr>
        <ShoppingCart></ShoppingCart>
        <hr></hr>
        <Contador></Contador>
        <hr></hr>
        <TeoriaRedux></TeoriaRedux>
      </div>
    </Provider>
  );
}

export default App;
