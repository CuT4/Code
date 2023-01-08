"strict mode";

const cambiarTamaño=(tamaño)=>{
    return ()=>{
        document.querySelector(".lorem").style.fontSize=`${tamaño}px`;
    }
}
px12=cambiarTamaño(12);
px14=cambiarTamaño(14);
px16=cambiarTamaño(16);

document.querySelector(".px-12").addEventListener("click", px12);
document.querySelector(".px-14").addEventListener("click", px14);
document.querySelector(".px-16").addEventListener("click", px16);

console.log(document.querySelector(".lorem").style)
