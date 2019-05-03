//dude this does NOT need to be in an IIFE, because script is placed
$(".navbar-toggler").blur(function () {
    $("#navbarSupportedContent").collapse('hide');
});


//we will use this to display random companies after user selects a sector
function shuffle(a) {
    //note this is the fisher yates shuffle algorithm.
    for (var i = a.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}



//This keeps object functions and variables independent of outside code, IIFE
(function (global) {
    //fake namespace object to expose.
    var infoObj = {};
    //the server side html to be inject
    var navHTML = "aSyncHTML/nav.html";
    var contributeHTML = "aSyncHTML/contributions.html";
    var header1HTML = "aSyncHTML/header1.html";
    //urls to our sectors stuff
    var sectorsJSON = "data/sectorData/sectorData.json";
    var sectorsTitleHTML = "aSyncHTML/sectors-title.html";
    var sectorHTML = "aSyncHTML/sector.html";

    //format to build our doc will be data/[shortName]/companiesData.json
    var companiesJSON = "data/";
    var companiesTitleHTML = "aSyncHTML/companies-title.html";
    var companyHTML = "aSyncHTML/company.html";

    //this is to maintain a list of companies the user will be tracking!
    var chosenCompanies = [];
    var alreadySent = [];

    //TODO: toggle on and off. These two functions are behind creating our array of companies
    //that the user wants to track.
    infoObj.mark = function (obj) {
        console.log("This is a test if mark works.");
        obj.style.border = "10px solid teal";
    }
    infoObj.addCompany = function (obj) {
        if (!chosenCompanies.includes(obj.innerHTML)) {
            chosenCompanies.push(obj.innerHTML);
        }
        //for testing, remove for final product
        console.log(chosenCompanies);
    }

    //TODO: make it so this toggles on and off...
    infoObj.change1 = function (obj) {
        document.getElementById("submit1").value="You submitted!";
        document.getElementById("submit1").style.background ="yellow";

    }
    infoObj.change2 = function (obj) {
        document.getElementById("submit2").value="You submitted!";
        document.getElementById("submit2").style.background ="yellow";
    }

    infoObj.lockIn = function (obj) {
        //convert this t
        var myJSONString = JSON.stringify(chosenCompanies);
        if (chosenCompanies.length == 0) {
            document.getElementById("lockIn").innerText = "You have not Picked anything";
            document.getElementById("lockIn").style.background = "red";

        }
        else if (alreadySent.includes(myJSONString)) {
            document.getElementById("lockIn").innerText = "Already Submitted These!";
            document.getElementById("lockIn").style.background = "red";
        }
        else {
            document.getElementById("lockIn").innerText = "Data Sent!";
            document.getElementById("lockIn").style.background = "yellow";
            document.getElementById("lockIn").style.color = 'black';
            alreadySent.push(myJSONString);
        }
        console.log(myJSONString);
    }



    //convenience method to insert HTML at a given selector, nice, helprs...
    var insertHtml = function (selector, html) {
        //woah this is some smooth sexy Jquery
        $(selector).html(html);
    };
    //creates loader gif while asynchronous javascript fetches data
    var showLoading = function (selector) {
        var html = "<div class='text-center'>";
        //this is working don't touch. Move onto navbar navigations
        html += "<img src='images/arbitraries/ajax-loader.gif'></div>";
        insertHtml(selector, html);
    };
    //some new shit for new dynamic html insertions (the images)
    var insertProperty = function (string, propName, propValue) {
        //oh, the string is the entire html, so this trick makes fuckin sense
        var propToReplace = "{{" + propName + "}}";
        //damn i finally get it. Holy shit.
        string = string.replace(new RegExp(propToReplace, "g"), propValue);
        return string;
    }
    var insertCompany = function (string, propName, propValue) {
        //oh, the string is the entire html, so this trick makes fuckin sense
        var propToReplace = propName;
        //damn i finally get it. Holy shit.
        string = string.replace(new RegExp(propToReplace, "g"), propValue);
        return string;
    }

    //DOMCONTload.. does this immediately page is loading... differnt than click event below
    $(function (event) {
        //show user a loading icon while they wait for page load
        showLoading("#navbar");
        showLoading("#main-content");
        showLoading("#main-content");
        //dynamic load navbar
        $ajaxUtils.sendGetRequest(navHTML, function (responseText) {
            //same action as below, just keen use of JQuery.
            insertHtml("#navbar", responseText);
        }, false);
        //dynamic load section1
        $ajaxUtils.sendGetRequest(header1HTML, function (responseText) {
            //same action as below, just keen use of JQuery.
            insertHtml("#main-content", responseText);
        }, false);

    });


    infoObj.loadContributions = function () {
        showLoading("#main-content");
        $ajaxUtils.sendGetRequest(contributeHTML, function (responseText) {
            //same action as below, just keen use of JQuery.
            insertHtml("#main-content", responseText);
        }, false);
    }

    infoObj.loadCompanies = function () {
        showLoading("#main-content");
        $ajaxUtils.sendGetRequest(sectorsJSON,
            //its JSON first (true), but next call its not (false)
            buildAndShowCompaniesHTML, true);
    }

    // Builds HTML for the categories page based on the data from the server
    function buildAndShowCompaniesHTML(categories) {
        // Load title snippet of categories page
        $ajaxUtils.sendGetRequest(
            //process the title HTML first, then companies in a for loop
            sectorsTitleHTML,
            function (companiesTitleHTML) {
                // Retrieve single company snippet
                $ajaxUtils.sendGetRequest(
                    sectorHTML,
                    function (companyHTML) {
                        //start building up the rows of icons
                        var categoriesViewHtml =
                            buildSectorsViewHTML(categories,
                                companiesTitleHTML,
                                companyHTML);
                        //finally, insert the built up html
                        insertHtml("#main-content", categoriesViewHtml);
                    },
                    false);
            },
            false);
    }

    //now build up our categories snippet
    function buildSectorsViewHTML(categories,
                                  companiesTitleHTML,
                                  companyHTML) {
        var finalHtml = companiesTitleHTML;
        finalHtml += "<div class='row'>";
        //correct data... yes, why is this for loop not being entered
        // Loop over categories
        for (var i = 0; i < categories.length; i++) {
            // companyHTML is one div from companies-snippet
            var html = companyHTML;
            //from json
            var sector = categories[i].sectorName;
            var picName = categories[i].picName;
            var shortName = categories[i].shortName;

            //replace the propName (companyName) in the html with name.
            //this is repetitive, to be reduced.
            html =
                insertProperty(html, "sector", sector);
            //replace the propName (picName) in the html with name.
            html =
                insertProperty(html, "picName", picName);
            //and finally, inject shortname, so we can load other content
            html =
                insertProperty(html, "shortName", shortName);


            finalHtml += html;
        }
        //close built up html and return
        finalHtml += "</div>";
        finalHtml += '<p id="companyButtons"><button id=\"backToHomeScreen\" class=\"button\" onclick=\"window.location.href=\'index.html\'\">HOME SCREEN</button>'
        return finalHtml;
    }



    //TODO: make this display user data, with a json object from header1
    infoObj.loadJSONText = function () {
        //How we will manipulate the data in the remote file
        var callback = function (res) {
            var message =
                res.firstName + " " + res.lastName
            if (res.likesProgramming) {
                message += " likes programming";
            } else {
                message += " gets it done";
            }
            message += " and uses ";
            message += res.numberOfCoffees + 1;
            message += " coffees for productivity.";
            message += " this was an asynchronous call" +
                " to info.json. Good job."

            document.querySelector("#jsonData")
                .innerHTML = "<h2>" + message + "</h2>";
        }
        //note that callback is not evaluated until the callback is achieved
        // Call server to get the data
        $ajaxUtils
            .sendGetRequest("data/info.json", callback, true);
    };


    //DOMCONTload.. does this immediately page is loading... differnt than click event below
    $(function (event) {
        //@param [shortName] from sector.html why is mt shortName still in mustache not
        infoObj.loadCompanyInfo = function (shortName) {
            //working
            console.log(shortName);
            //not working
            $ajaxUtils.sendGetRequest(
                //e.g. data/fs/companiesData.json, almost had terr error
                companiesJSON + shortName + "/companiesData.json",
                buildAndShowCompaniesHTML, true);
        }

        //sector companies is now a json object (an array of objects really)
        function buildAndShowCompaniesHTML(sectorCompanies) {
            $ajaxUtils.sendGetRequest(
                //build the title of the new screen
                companiesTitleHTML,
                function (companiesTitleHTML) {
                    //retrieve a single company, to be random for user XP
                    $ajaxUtils.sendGetRequest(
                        //dealing with a single company
                        companyHTML, function (companyHTML) {
                            var companiesViewHTML = buildMenuItemsViewHTML(sectorCompanies,
                                companiesTitleHTML, companyHTML);
                            insertHtml("#main-content", companiesViewHTML);
                        },
                        false);
                },
                false);
        }

        //remember, sectorCompanies is a json object right now. Use like an object
        function buildMenuItemsViewHTML(sectorCompanies, companiesTitleHTML, companyHTML) {
            //working
            companiesTitleHTML =
                insertProperty(companiesTitleHTML, "sector", sectorCompanies[0].sector)
            //build with the title first
            var finalHtml = companiesTitleHTML;
            //begin a row so it can be bootstrap responsive
            finalHtml += "<section class='row'>";
            //I'm a genius.
            var shuffledCompanies = shuffle(sectorCompanies);
            //loop over categories, note this makes only 4 display of the 8
            for (var i = 0; i < shuffledCompanies.length / 2; i++) {
                //this is the only way I know we can make sure it will get unique companies yikes
                var companyNumber = "company"+i;
                var html = companyHTML;
                html = insertProperty(html, "companyName", shuffledCompanies[i].companyName);
                html = insertProperty(html, "sectorShortName", shuffledCompanies[i].sectorShortName);
                html = insertProperty(html, "shortName", shuffledCompanies[i].shortName);
                html = insertCompany(html, "addMe", companyNumber);

                finalHtml += html;

                //create hidden div to make each element unique so we can access it later...
                //working.
                finalHtml += '<div style="display: none;" id="'+companyNumber+'">'+shuffledCompanies[i].companyName+'</div>';
            }
            //this is where we will put the button. Oh dear lord this is so disorganized
            //but I think I can put the companies in an array and whatever they select
            //uh oh
            finalHtml += "</section>";
            finalHtml += '<div><p id="companyButtons"><button id=\"backButton\" class=\"button\" onclick=\"$infoObj.loadCompanies()\">Back to Sectors!</button>' +
                '<button id=\"lockIn\" class=\"button\" onclick=\"$infoObj.lockIn()\">Lock in Companies!</button>' +
                '</p></div>';
            console.log(finalHtml);

            return finalHtml;
        }
    });


    //var the obj be seen
    global.$infoObj = infoObj;
})(window);



