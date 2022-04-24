//esto si la carpeta de imagenes estuviera dentro de src
import imgReyAtanagildo from './imagenesReyes/rey_atanagildo.png';
import imgReyLeogivildo from './imagenesReyes/rey_leogivildo.png';
import imgReySisebuto from './imagenesReyes/rey_sisebuto.png';
import tino from './imagenesReyes/tino.png';
import './App.css';
import './miCss.css';


function App() {

  const reyNombres = ["Rey Sisebuto", "Rey Leogivildo", "Rey Atanagildo"];

  const cambiarImg = (img)=>{
    
    if (img.target.src.includes("sisebuto")) {
      img.target.src = tino;
      img.target.parentNode.style.background = "#fff";
     
    }
    else if (img.target.src.includes("leogivildo")) {
      img.target.src = tino;
      img.target.parentNode.style.background = "#fff";
    }
    else if (img.target.src.includes("atanagildo")) {
      img.target.src = tino;
      img.target.parentNode.style.background = "#fff";
    }
    else {
      img.target.src = "";
      img.target.parentNode.style.background = "#fff";
    }
  }

  //analizar los casos de cada rey por separado es al pedo ya que todos reaccionan al mismo evento 
  //ademas usando el visibility evita q el texto se vaya hacia arriba 
  const cambiarImgDeCurso = (img)=>{
    if (img.target.src.includes("tino")) {
      img.target.style.visibility = "hidden";
    } else {
      img.target.src = tino;
      img.target.parentNode.style.background = "#fff";
    }
  }

  const cambiarNombre = (imgName)=>{
    if (imgName.target.innerHTML == "Tino") {
      imgName.target.innerHTML = "";
    }
    else {
      imgName.target.innerHTML = "Tino";
    }
  }

  return (
    <div className='container'>
      <div className="reySisebuto">
        <img className="reySisebuto__imagen" src={imgReySisebuto} onClick={cambiarImg}/>
        <div className="reySisebuto__nombre" onClick={cambiarNombre}>
          {reyNombres[0]}
        </div>
      </div>
      <div className="reyLeogivildo">
        <img className="reyLeogivildo__imagen" src={imgReyLeogivildo} onClick={cambiarImg}/>
        <div className="reyLeogivildo__nombre" onClick={cambiarNombre}>
          {reyNombres[1]}
        </div>
      </div>
      <div className="reyAtanagildo">
        <img className="reyAtanagildo__imagen" src={imgReyAtanagildo} onClick={cambiarImg}/>
        <div className="reyAtanagildo__nombre" onClick={cambiarNombre}>
          {reyNombres[2]}
        </div>
      </div>
    </div>
  );
}

export default App;
