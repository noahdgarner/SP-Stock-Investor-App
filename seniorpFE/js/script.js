//replaced DOMContentLoaded, so this will load immediately after HTML
$(function () {

    $(".navbar-toggler").blur(function () {
            $("#navbarSupportedContent").collapse('hide');
    });

});


//This keeps object functions and variables independent of outside code
//Uses an IIFE, meaning all this is executed
(function (global) {

    let obj = {};
    //the object we will expose
    let contentHTML = "aSyncHTML/mainContents.html";
    //convenience method to insert HTML at a given selector, nice
    // Convenience function for inserting innerHTML for 'select'
    let insertHtml = function (selector, html) {
        //woah this is some smooth sexy Jquery
        $(selector).html(html);
    };
    // Show loading icon inside element identified by 'selector'.
    let showLoading = function (selector) {
        let html = "<div class='text-center'>";
        //this is working don't touch. Move onto navbar navigations
        html += "<img src='images/ajax-loader.gif'></div>";
        insertHtml(selector, html);
    };
    //working
    document.addEventListener("DOMContentLoaded", function (event) {
        //show user a loading icon while they wait for page load
        showLoading("#main-content");
        //we can use this object because its global in util.js!!
        //issues our AJAX request'
        $ajaxUtils.sendGetRequest(contentHTML, function (responseText) {
            document.querySelector("#main-content")
                .innerHTML = responseText;
        }, false);
    });


     obj.loadJSONText = function () {
                // Call server to get the data
                $ajaxUtils
                    .sendGetRequest("data/info.json",
                        function (res) {
                            let message =
                                res.firstName + " " + res.lastName
                            if (res.likesProgramming) {
                                message += " likes programming";
                            } else {
                                message += " doesn't like Chinese food";
                            }
                            message += " and uses ";
                            message += res.numCoffees + 1;
                            message += " coffees for productivity.";
                            message += " this was an asynchronous call" +
                                "to info.json. Good job."

                            document.querySelector("#buttonReaction")
                                .innerHTML = "<h2>"+message+"</h2>";
                        }, true);
            };


    global.$obj = obj;

})(window);


