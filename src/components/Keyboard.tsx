import React from "react";
import { KeyboardKey } from "~/types";

interface KeyboardProps {
  rows: KeyboardKey[][];
}

export const Keyboard = (props: KeyboardProps) => {
  return (
    <div>
      {props.rows &&
        props.rows.map((row, index) => {
          return (
            <ul className="row" key={index}>
              {row.map((keyObj, index) => {
                return (
                  <li className={keyObj.class} key={index}>
                    {keyObj.type === "double" ? (
                      <>
                        <span>{keyObj.primary}</span>
                        <span>{keyObj.shift}</span>
                      </>
                    ) : (
                      <span>{keyObj.shift}</span>
                    )}
                  </li>
                );
              })}
            </ul>
          );
        })}
      ;
    </div>
  );
};
