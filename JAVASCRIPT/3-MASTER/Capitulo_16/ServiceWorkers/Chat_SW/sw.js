// Escuchando mensajes
self.addEventListener("message", (event) => {
  if (event.data.type === "message") {
    // Enviando mensaje a la página "chat2.html"
    self.clients
      .matchAll({
        type: "window",
        includeUncontrolled: true,
      })
      .then((clients) => {
        clients.forEach((client) => {
          if (client.url.includes(event.data.targetPage)) {
            client.postMessage({
              type: "message",
              message: event.data.message,
              sourcePage: event.data.sourcePage,
            });
          }
        });
      });
  }
});


  