

function blah(date) {
    return {date: "Blep"}
}

function popup() {
    alert( "Handler called." );
  }

  $(document).ready(function() {
    $("#trigger").click(function() {
        $("#demo").html("Hello, World!");
    });
});