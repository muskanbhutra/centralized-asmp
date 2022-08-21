function addwish(e, id)
{

	console.log(e.target.parentElement.parentElement.parentElement.parentElement.parentElement)
	e.target.parentElement.parentElement.parentElement.parentElement.parentElement.style.display="none"
	url='/asmp/fav/'+id+'/'
	console.log(url)
	$.ajax({
		url: url,
		type: "GET",
		dataType: "json",
		success: (data) => {
		  console.log(data);
		},
		error: (error) => {
		  console.log(error);
		}
	  });
}
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
