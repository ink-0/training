const fs = require('fs');

let input = (fs.readFileSync('./test') + '').toString().trim().split('\n');

const computerCnt = Number(input.shift());
const pair = Number(input.shift());

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

const comPair = new LinkedList();
