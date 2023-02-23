let version="version 1";
//Adding event listeners
self.addEventListener("install", ()=>{
    console.log("Service worker successfully installed");
    caches.open(version).then(cache=>{
        cache.add("offLoad.html").then(res=>{
            console.log("Info in cache");
        }).catch(e=> {
            console.error(e);
        })
    })
});
//If the Service Worker is active, it notifies us and deletes existing cache
self.addEventListener("active", ()=>{
    console.log("Service worker is currently active");
    //If the cache is different form the version we want, it is deleted
    caches.keys().then(key=>{
        return Promise.all(
            key.map(cache=>{
                if(cache!==version){
                    console.log("Old cache deleted");
                    return caches.delete(cache);
                }
            })
        )
    })
});
//Listening a fetch event or petition
self.addEventListener("fetch", (e)=>{
    e.respondWidth(async function(){
        const respuestaEnCache=await caches.match(e.request);
        if (respuestaEnCache) return respuestaEnCache;
        else return e.request;
    });
});
//Listening a message event
self.addEventListener("message", (e)=>{
    console.log(`Service worker received this message: ${e.data}`);
    e.source.postMessage("Message received");
})