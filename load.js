"use strict";

const TICK = 5 * 1000;
const KEK_FLOW_SPEED = 0.000175972222222;
const MAX_UNLOAD_SPEED = 0.000025;
const MIN_UNLOAD_SPEED = 0.000016666666667;
class Belt {
  constructor(width, offset, direction) {
    this.width = width;
    this.offset = offset;
    this.direction = direction;
  }
  setOffset(offset) {
    this.offset = offset;
  }
  setDirection(direction) {
    this.direction = direction;
  }
}
class Container {
  constructor(capacity, content) {
    this.capacity = capacity;
    this.content = content;
    this.contentToCapacityPercent = (
      (this.content / this.capacity) *
      100
    ).toFixed(2); 
    this.minContent = capacity * Container.MIN_CAPACITY_RATIO;
    this.maxContent = capacity * Container.MAX_CAPACITY_RATIO;
  }
  load(content) {
    this.content += content;
    this.contentToCapacityPercent = (
      (this.content / this.capacity) *
      100
    ).toFixed(2);
  }
  unload(content) {
    this.content -= content;
    this.contentToCapacityPercent = (
      (this.content / this.capacity) *
      100
    ).toFixed(2);
  }
}
Container.MAX_CAPACITY_RATIO = 0.9;
Container.MIN_CAPACITY_RATIO = 0.3;
const containers = [];
for (let index = 0; index < 6; index++) {
  const container = new Container(200, (Math.random() * (1 - 0.5) + 0.5) * 200);
  containers.push(container);
}
const belt = new Belt(4, 0, "left");
const getCurrentContainer = (belt, containers) =>
  belt.direction === "left"
    ? containers[belt.offset]
    : containers[belt.offset + belt.width];
let container = getCurrentContainer(belt, containers);
(function loop() {
  setTimeout(() => {
    const unloadSpeed =
      Math.random() * (MAX_UNLOAD_SPEED - MIN_UNLOAD_SPEED) + MIN_UNLOAD_SPEED;
    containers.forEach((container) => {
      container.unload(TICK * unloadSpeed);
    });
    console.dir(containers);
    console.dir(belt);
    if (container.content < container.minContent) {
      container.load(TICK * KEK_FLOW_SPEED);
      return loop();
    }
    const idx = containers.reduce(
      (acc, container, idx) =>
        container.content < containers[acc].content ? idx : acc,
      0
    );
    if (idx > 2) {
      belt.setDirection("right");
      belt.setOffset(idx - belt.width);
    } else {
      belt.setDirection("left");
      belt.setOffset(idx);
    }
    container = getCurrentContainer(belt, containers);
    if (container.content >= container.maxContent) return loop();
    container.load(TICK * KEK_FLOW_SPEED);
    loop();
    // console.log()
  }, TICK);
})();