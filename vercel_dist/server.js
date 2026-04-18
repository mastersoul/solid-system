const WebSocket = require("ws");

const PORT = process.env.PORT || 10000;

const wss = new WebSocket.Server({ port: PORT });

let players = {};

wss.on("connection", (ws) => {

  ws.on("message", (msg) => {
    try {
      const data = JSON.parse(msg);

      players[data.id] = data;

      const payload = JSON.stringify(players);

      wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(payload);
        }
      });

    } catch (e) {
      console.log("Invalid message");
    }
  });

  ws.on("close", () => {
    // optional: cleanup
  });

});

console.log("WebSocket server running on port", PORT);