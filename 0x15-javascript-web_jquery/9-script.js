// Script didn't work for CORS reasons 
// Using the core $.ajax() method
$.ajax({
    // The URL for the request
    url: "https://fourtonfish.com/hellosalut/?lang=fr",

    // Whether this is a POST or GET request
    type: "GET",

    // The type of data we expect back
    dataType: "json",
})
    // Code to run if the request succeeds (is done);
    // The response is passed to the function
    .done(function (data) {
        console.log(data);
        $("DIV#hello").text(data.hello);
    })
    // Code to run if the request fails; the raw request and
    // status codes are passed to the function
    .fail(function (xhr, status, errorThrown) {
        alert("Sorry, there was a problem!");
        console.log("Error: " + errorThrown);
        console.log("Status: " + status);
        console.dir(xhr);
    });
