import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "index.css";
import { BrowserRouter } from "react-router-dom";
import { AuthContextProvider } from "providers/AuthContextProvider";
import "bootstrap/dist/css/bootstrap.min.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthContextProvider>
        <App />
      </AuthContextProvider>
    </BrowserRouter>
  </React.StrictMode>,
);
