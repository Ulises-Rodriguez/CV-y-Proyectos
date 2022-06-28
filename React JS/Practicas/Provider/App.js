import MyPage from "./components/MyPage";
import MyPageContext from "./components/MyPageContext";
import CrudApi from "./CrudApi/CrudApi";
import { CrudProvider } from "./CrudApi/CrudContext/CrudContext";

function App() {
  return (
    <div>
      <h1>React Context</h1>
      <a
        href="https://es.reactjs.org/docs/context.html"
        target="_blank"
        rel="noreferrer"
      >
        Documentacion
      </a>
      <CrudProvider>
        <CrudApi></CrudApi>
      </CrudProvider>
      <hr></hr>
      <MyPageContext></MyPageContext>
      <hr></hr>
      <MyPage></MyPage>
    </div>
  );
}

export default App;
