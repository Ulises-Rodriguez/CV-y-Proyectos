import React from "react";

const Imagen = ({ srcImg, count }) => {
  return (
    <>
      <div className="ImgContainer">
        {
          <img
            src={srcImg}
            alt=""
            style={
              count !== 0 ? { visibility: "visible" } : { visibility: "hidden" }
            }
          ></img>
        }
      </div>
    </>
  );
};

export default Imagen;
