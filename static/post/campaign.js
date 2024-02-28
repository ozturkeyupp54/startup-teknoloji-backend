const editButton = document.querySelector(".editButton")
const editTable = document.querySelector(".editTable")
const allOS = document.querySelector(".allOS")
const ulOs = document.querySelector(".ulOs")
const allBrowsers = document.querySelector(".allBrowsers")
const ulBrowsers = document.querySelector(".ulBrowsers")



editButton.addEventListener("click",()=>{
    console.log("click")
    editTable.classList.toggle("d-none")
})

allOS.addEventListener("click",()=>{
    ulOs.classList.toggle("d-none")
})
allBrowsers.addEventListener("click",()=>{
    ulBrowsers.classList.toggle("d-none")
})