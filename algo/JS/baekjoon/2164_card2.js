const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim();

// while (numArr.length > 1) {
//   numArr.shift();
//   numArr.push(numArr.shift());
// }

// console.log(numArr[0]);

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this._size = 0;
  }

  add(value) {
    const newNode = new Node(value);

    if (!this.head) {
      this.head = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
    }

    this.tail = newNode;
    this._size++;

    return newNode;
  }

  getHead() {
    return this.head.value;
  }

  removeHead() {
    this.head = this.head.next;
    this.head.prev = null;
    this._size--;
  }

  getSize() {
    return this._size;
  }
}

const cards = new LinkedList();
console.log('클래스', cards);

for (let i = 1; i <= input; i++) {
  cards.add(i);
}
console.log('zkdfjl', cards);

while (cards.getSize() !== 1) {
  cards.removeHead();
  cards.add(cards.getHead());
  cards.removeHead();
}

console.log(cards.getHead());
