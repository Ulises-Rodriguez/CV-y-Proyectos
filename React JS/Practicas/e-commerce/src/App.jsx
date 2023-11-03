import './App.css';
import { Layout } from './components/Layout';
import { Routes, Route } from 'react-router-dom';
import { Home } from './pages/Home';
import { Consolas } from './pages/Consolas';
import { ConsolaDetalle } from './pages/ConsolaDetalle';
import { Figuras } from './pages/Figuras';
import { Juegos } from './pages/Juegos';
import { JuegosDetalles } from './pages/JuegosDetalles';
import { ContextWrapper } from './context/Context';
import { DetalleProducto } from './pages/DetalleProducto';
import { Checkout } from './pages/Checkout';
import { NotFound } from './pages/NotFound';

function App() {
  return (
    <>
      <ContextWrapper>
          <Layout>
            <Routes>
              <Route path='/' element={<Home />} />
              <Route path='/:id' element={<DetalleProducto url={'juegosRetro'} />} />
              <Route path='/figuras' element={<Figuras />} />
              <Route path='/figuras/:id' element={<DetalleProducto url={'figuras'} />} />
              <Route path='/consolas' element={<Consolas />} />
              <Route path='/consolas/:id' element={<ConsolaDetalle />} />
              <Route path='/consolas/:id/:consola' element={<DetalleProducto url={'consolas'} />} />
              <Route path='/juegos' element={<Juegos />} />
              <Route path='/juegos/:id' element={<JuegosDetalles />} />
              <Route path='/juegos/:id/:juego' element={<DetalleProducto url={'juegos'} />} />
              <Route path='/checkout' element={<Checkout />} />
              <Route path='/notfound' element={<NotFound />} />
              <Route path='*'  element={<NotFound/>} />
            </Routes>
          </Layout>
      </ContextWrapper>
    </>
  );
}

export default App;
