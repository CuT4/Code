// chat.js
const messageForm = document.querySelector("#message-form");
const messageInput = document.querySelector("#message-input");
const messagesContainer = document.querySelector("#messages-container");

// Registrando el Service Worker
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js").then(() => {
    console.log("Service worker registrado.");
  });
}

// Escuchando el envío del formulario
messageForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const message = messageInput.value;
  const messageElement = document.createElement("div");
  messageElement.classList.add("from_chat");
  messageElement.innerText=message;
  messagesContainer.appendChild(messageElement);
  // Enviando mensaje a la página "chat2.html"
  navigator.serviceWorker.getRegistration().then((registration) => {
    registration.active.postMessage({
      type: "message",
      message: message,
      sourcePage: "chat.html",
      targetPage: "chat2.html",
    });
  });
  messageInput.value = "";
});

// Escuchando mensajes recibidos del Service Worker
navigator.serviceWorker.addEventListener("message", (event) => {
  if (event.data.type === "message" && event.data.sourcePage === "chat2.html") {
    const message = event.data.message;
    const messageElement = document.createElement("div");
    messageElement.classList.add("from_chat2");
    messageElement.innerText = message;
    messagesContainer.appendChild(messageElement);
  }
});


