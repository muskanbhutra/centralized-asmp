
function rotatecard(e)
{
    e.target.parentElement.parentElement.parentElement.style.transform="rotateY(180deg)"
}

function rotatecardback(e)
{
    e.target.parentElement.parentElement.parentElement.style.transform="rotateY(0deg)"
}

 
function hamToggle()
{
    console.log("helloo")
    var element = document.getElementById("hamburger-6");
    element.classList.toggle("is-active");
    var element = document.getElementById("overlay");
    element.classList.toggle("toggle");
}
