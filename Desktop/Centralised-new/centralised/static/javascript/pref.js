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

function f()
{
    var value = $('#drop').val();
    $(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');

    $("."+value).removeClass('invisible');
}

 
function hamToggle()
{
    console.log("helloo")
    var element = document.getElementById("hamburger-6");
    element.classList.toggle("is-active");
    var element = document.getElementById("overlay");
    element.classList.toggle("toggle");
}


function rotatecard(e)
{
    e.target.parentElement.parentElement.parentElement.style.transform="rotateY(180deg)"
}

function rotatecardback(e)
{
    e.target.parentElement.parentElement.parentElement.style.transform="rotateY(0deg)"
}
$(document).ready(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").removeClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
});
$("#al").click(function(){
	$(".al").removeClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#core").click(function(){
	$(".al").addClass('invisible');
	$(".core").removeClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#ci").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").removeClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#design").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").removeClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#fin").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").removeClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#it").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").removeClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#manc").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").removeClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#man").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").removeClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#re").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").removeClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").addClass('invisible');
})
$("#strat").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").removeClass('invisible');
	$(".other").addClass('invisible');
})
$("#other").click(function(){
	$(".al").addClass('invisible');
	$(".core").addClass('invisible');
	$(".ci").addClass('invisible');
	$(".design").addClass('invisible');
	$(".fin").addClass('invisible');
	$(".it").addClass('invisible');
	$(".manc").addClass('invisible');
	$(".man").addClass('invisible');
	$(".re").addClass('invisible');
	$(".strat").addClass('invisible');
	$(".other").removeClass('invisible');
})
	
