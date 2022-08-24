// On clicking the department section fire this ajax

$(".department").click(function() {
    var depart = $(this).attr("data-dept")
    if (depart) {
        // Create Ajax Call
        $.ajax({
            url: "", 
            data: {
                'depart': depart
            },
            dataType: 'json',
            success: function (data) {
                console.log("hello")
                $("#speaker").load(" #speaker");
                $('.mentorcardwrap').empty()
                $.each(data, function(index) {
                    $('.mentorcardwrap').append(Card(data[index]));
                    console.log(data)
                }); 
            }
        });
      } else {
        alert("All fields must have a valid value.");
    }
    return false;
});



$(".mentorcard").click(function() {

  console.log("Hello")
  if($(this).is(":checked")) { 
    $.ajax({
        url: '/addSession',
        data: { SpkrId:$(this).attr("data-ID") },
        dataType: 'json',
        success: function (data) {
          console.log("Hello")
        }
    });
    } else {
        $.ajax({
        });
    }

})

$('.hello').click(function() {
  console.log("hello")
})




function Card(data) {
    
    const string = `
    <div>`+data.name+`</div>
    <div class="mentorcard">
      <div class="mentorcardinner">
        <div class="mentorcardfront">
          <div class="mentorid">Mentor ID : `+data.name+`</div>
          <div class="mentorinfo">
          `+data.name+`
          </div>
          <div class="mentorinfo">
          `+data.name+`, `+data.name+`
          </div>
          <div class="mentorinfo">`+data.name+`</div>
          <div class="mentorinfo">
          `+data.name+`, `+data.name+`
          </div>
          <center>
            <input type="checkbox" id="Attending" class="SpeakerPref" data-ID=`+data.speaker_id+`/><label for="switch1"
              >Toggle</label
            >
              <input type="submit" value=`+data.name+` name="Attend" />
          </center>
          <input class="updateSession" type="checkbox">
        </div>
        <div class="mentorcardback">
          <div class="mentorinfo mentordesc">`+data.name+`</div>
          <div class="mentorbtnwrap">
            <div
              class="mentorbtn1 mentorbtn"
              onclick="rotatecardback(event)"
            >
              Back
            </div>
            <div class="mentorbtn2 mentorbtn">
              <a href="/asmp/fav/`+data.name+`">Wishlist</a>
            </div>
          </div>
          
        </div>
      </div>
    </div>    
    `
    return string
}