// Event handling, this loads all JS after HTML tags are defined, but
//before CSS, bootstrap, images, etc are process. (JQuery JavaScript)
$(function () {

    $(".navbar-toggler").blur(function () {
            $("#navbarSupportedContent").collapse('hide');
    });

});


//going to implement as an IIFE when I get back, note this is separate from
//dynamic webpage functions. oh. woops
(function (global) {
    //eliminate document.querySelector("DOM....) with a JQuery $
    $(function () {
        // Unobtrusive event binding, fuck this function
        document.querySelector("#button")
            .addEventListener("click", function () {
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
            });

        });

})(window);
