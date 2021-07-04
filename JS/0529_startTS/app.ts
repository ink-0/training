const positions2D = [
  { x: 2, y: 3 },
  { x: 4, y: 5 },
];
interface positionType {
  x: number;
  y: number;
  [key: string]: number;
}
const getPositionBy = (position: positionType[], key: string) => {
  return position.map((v) => v[key]);
};

const result: number[] = getPositionBy(positions2D, 'y');

console.log(result);
