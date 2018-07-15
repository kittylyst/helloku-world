

function blah(date) {
    return {date: "Blep"}
}

function popup() {
    alert( "Handler called." );
  }

  $(document).ready(function() {
    $("#trigger").click(function() {
        $.getJSON("/date", function(data){
            var items = [];
            $.each( data, function( key, val ) {
              items.push( "<li id='" + key + "'>" + val + "</li>" );
            });
           
            $( "<ul/>", {
              "class": "my-new-list",
              html: items.join( "" )
            }).appendTo( "body" );
        }); 
    });
});

