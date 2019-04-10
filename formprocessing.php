<?php
// define variables and set to empty values
$firstNameErr = $lastNameErr = $dobErr = $emailErr = $risk = $xp ="";
$firstName = $lastName = $dob = $email = $risk = $xp = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["firstName"])) {
        $firstNameErr = "firstName is required";
    } else {
        $firstName = $_POST["firstName"];
        // check if firstName only contains letters and whitespace
        if (!preg_match("/^[a-zA-Z ]*$/", $firstName)) {
            $firstNameErr = "Only letters and white space allowed";
        }
    }

    if (empty($_POST["lastName"])) {
        $lastNameErr = "firstName is required";
    } else {
        $lastName = $_POST["lastName"];
        // check if firstName only contains letters and whitespace
        if (!preg_match("/^[a-zA-Z ]*$/", $lastName)) {
            $lastNameErr = "Only letters and white space allowed";
        }
    }

    if (empty($_POST["dob"])) {
        $dobErr = "Email is required";
    } else {
        $dob = $_POST["dob"];
        // check if e-mail address is well-formed
        if (!filter_var($dob, FILTER_VALIDATE_EMAIL)) {
            $dobErr = "Invalid email format";
        }
    }

    if (empty($_POST["email"])) {
        $emailErr = "Email is required";
    } else {
        $email = $_POST["email"];
        // check if e-mail address is well-formed
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $emailErr = "Invalid email format";
        }
    }

    $risk = $_POST["risk"];
    $xp = $_POST["xp"];


    echo '<h3>~Your Information~</h3>';
    echo 'Your first name is:  ' . $firstName . '<br>';
    echo 'Your last name is:  ' . $lastName . '<br>';
    echo 'Your Date of Birth is:  ' . $dob . '<br>';
    echo 'Your email address is: ' . $email . '<br>';
    echo 'Your risk tolerance is:  ' . $risk . '<br>';
    echo 'Your experience is: ' . $xp . '<br>';


    $fp = fopen('data/formdata.txt', 'w');
    $savestring = $firstName . "\n" . $lastName .
        "\n" . $email . "\n" . $dob . "\n" . $risk . "\n" . $xp;
    fwrite($fp, $savestring);
    fclose($fp);
    echo '<h1>Your data has been saved in a JSON file!</h1>';




}
