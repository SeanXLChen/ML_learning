import React from "react";
import { useState, useContext } from "react";

const ParameterContext = React.createContext();

export default function ParameterProvider({ children }) {

  const [SVM, setSVM] = useState(null);

  return (
    <ParameterContext.Provider value={{ SVM, setSVM }}>
      {children}
    </ParameterContext.Provider>
  );
}

const useParameter = () => useContext(ParameterContext);

export { ParameterProvider, useParameter };
