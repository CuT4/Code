document.addEventListener("DOMContentLoaded", function() {
    // Seleccionando elementos del DOM
    const messageForm = document.querySelector("#message-form");
    const messageInput = document.querySelector("#message-input");
    const messagesContainer = document.querySelector("#messages-container");
  
    // Escuchando el envío del formulario
    messageForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const message = messageInput.value;
      // Enviando mensaje a la página "chat.html"
      const messageElement = document.createElement("div");
      messageElement.classList.add("from_chat2");
      messageElement.innerText=message;
      messagesContainer.appendChild(messageElement);
      navigator.serviceWorker.getRegistration().then((registration) => {
        registration.active.postMessage({
          type: "message",
          message: message,
          sourcePage: "chat2.html",
          targetPage: "chat.html",
        });
      });
      messageInput.value = "";
    });
  
    // Escuchando mensajes recibidos del Service Worker
    navigator.serviceWorker.addEventListener("message", (event) => {
      if (event.data.type === "message" && event.data.sourcePage === "chat.html") {
        const message = event.data.message;
        const messageElement = document.createElement("div");
        messageElement.classList.add("from_chat");
        messageElement.innerText = message;
        messagesContainer.appendChild(messageElement);
      }
    });
  });
  
