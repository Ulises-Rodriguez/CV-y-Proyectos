import React from "react";
import { Navigate, Route } from "react-router-dom";
import Dashboard from "../pages/Dashboard";

const PrivateRoute = ({auth}) => {
//   let auth;
//   auth = true;
//   auth = null;

  return auth ? <Dashboard /> : <Navigate to="/login" />;

};

export default PrivateRoute;
