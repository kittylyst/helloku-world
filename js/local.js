

function blah(date) {
    return {date: "Blep"}
}

function popup() {
    alert( "Handler called." );
  }

  $(document).ready(function() {
    $("#trigger").click(function() {
        $.get("/date", function(data, status){
            // var date = JSON.parse(data);
            $("#datetime").html(data);
        }); 
    });
});

