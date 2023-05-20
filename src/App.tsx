import React, { useState } from "react";
import { Keyboard } from "./components/Keyboard";
import { keyboardRows } from "./keys";

export function App() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1 className="title">Default Keyboard</h1>
      <Keyboard rows={keyboardRows} />
    </div>
  );
}
