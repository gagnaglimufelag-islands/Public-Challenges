<html>
    <head>
        <title>🐘 PHP Frick 🐘</title>
        <!-- Do not forget to remove the <code>debug</code> parameter -->
    </head>
    <body style="background-color:#282c34;margin:auto;text-align:center;margin-top:10%;">
    <form action="/index.php" method="post">
        <textarea type="text" rows="15" cols="100" id="value" name="value" placeholder="PHP FRICK ME UP!" style="border-top-style:hidden;border-right-style:hidden;border-left-style:hidden;border-bottom-style:groove;"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>     
<?php 
    error_reporting(E_ERROR | E_PARSE);
    if ($_SERVER["REQUEST_METHOD"] === "GET") {
        if (isset($_GET["debug"])) {
            highlight_file("./index.php");           
        } else {
        }
    }
    else {
        if (empty($_POST) || !isset($_POST) || !isset($_POST["value"])) {
            die("<p style='color:#dcdcdc;font-weight:bold;'>NO >:(</p>");
        }
        if (!preg_match("/^[=$!_\[\]\(\)+.;]*$/", $_POST["value"])) {
            die("<p style='color:#dcdcdc;font-weight:bold;'>NO >:(</p>");
        }
        try {
            eval($_POST["value"]);
        } catch (ParseError $e) {
            echo "<p style='color:#ff443e;font-weight:bold;'>Failed Horribly</p>";
        }
    }
?> 
    </body>
</html>
