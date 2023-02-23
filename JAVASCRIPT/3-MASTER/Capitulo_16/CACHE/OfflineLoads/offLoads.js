"use strict";
const sw=navigator.serviceWorker;
//Adding files to cache
caches.open("Version").then(cache=>{
    cache.add("/offLoad.html");
})
//Checking if the borowser supports Service Workers
if(sw){
    console.log("Your browser supports Service Workers");
    navigator.serviceWorker.register("Sw.js");
}
//Posting a message to the SW once this is ready and active
sw.ready.then(res=>{
    res.active.postMessage("This is a message for the service worker");
});
//Listening for messages that come form the SW
sw.addEventListener("message", (e)=>{
    console.log(`Principal script received this message: ${e.data}`);
})