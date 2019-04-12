//housekeeping to set up IIFE, and fake namespace for our util
(function (global) {
    // Set up a namespace for our utility, we will attach things we want to
    //expose to outside world
    let ajaxUtils = {};
// Returns an HTTP request object
    function getRequestObject() {
        if (global.XMLHttpRequest) {
            return (new XMLHttpRequest());
        }
        else {
            global.alert("Ajax is not supported!");
            return(null);
        }
    }

    // Makes an Ajax GET request to 'requestUrl', we will use this in our script
    ajaxUtils.sendGetRequest =
        //@Params: requestURL: were to go on the server
        //         responseHandler: a function that handles the result of
        //                          what the server returns
        //         isJsonResponse: boolean...
        function (requestUrl, responseHandler, isJsonResponse) {
            //define our object of power!

            let request = getRequestObject();
            //set up the parameters of the request, to a function OBJECT
            //NOT A Function return value!!!! Very important.
            request.onreadystatechange = function () {
                handleResponse(request, responseHandler, isJsonResponse);
            };
            //sent off asynchronously
            request.open("GET", requestUrl, true);
            request.send(); //if using post, send this function body params
        };


    // Only calls user provided 'responseHandler'
    // function if response is ready
    // and not an error
    function handleResponse(request,
                            responseHandler,
                            isJsonResponse) {
        if ((request.readyState == 4) &&
            (request.status == 200)) {

            // Default to isJsonResponse = true
            if (isJsonResponse == undefined) {
                isJsonResponse = true;
            }

            //if its JSON, parse the text, otherwise
            if (isJsonResponse) {
                //passes the parsed object to our handle function
                //note that our handle function is defined in script.js
                responseHandler(JSON.parse(request.responseText));
            } else {
                //pass request the the handle function we defined in script.js
                responseHandler(request.responseText);
            }
        }
    }


    // Expose utility to the global object, IIFE
    global.$ajaxUtils = ajaxUtils;
})(window);

