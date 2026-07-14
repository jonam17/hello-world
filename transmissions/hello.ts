// TRANSMISSION 02 // TYPESCRIPT — types keep the signal clean.

type Signal = { node: string; payload: string; status: "ONLINE" | "OFFLINE" };

const firstTransmission: Signal = {
  node: "00",
  payload: "Hello, World",
  status: "ONLINE",
};

console.log(`[NODE ${firstTransmission.node}] ${firstTransmission.payload}`);
