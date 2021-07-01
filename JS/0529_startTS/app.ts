const positions2D = [
  { x: 2, y: 3 },
  { x: 4, y: 5 },
];

const getPositionBy = (position, key) => {
  return position.map((v) => v[key]);
};

const result: number[] = getPositionBy(positions2D, 'y');
