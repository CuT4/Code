"use strict";

caches.open("archivos-estaticos").then(cache=> {
    cache.add("cache.html")
});

// cache.add()
// cache.addAll()
// cache.delete()
// cache.match()
// cache.matchAll()
