export interface KeyboardKey {
  primary: string;
  shift: string | null;
  type: string;
  class: string;
}

export interface KeyboardType {
  keyRowOne: KeyboardKey[];
  keyRowTwo: KeyboardKey[];
  keyRowThree: KeyboardKey[];
  keyRowFour: KeyboardKey[];
  keyRowFive: KeyboardKey[];
}
