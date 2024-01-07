<html>
    <head>
        <title>Irregular Statements</title>
        <!-- Do not forget to remove the <code>debug</code> parameter -->
    </head>
    <body style="background-color:#282c34;margin:auto;text-align:center;margin-top:10%;">
    <form action="/index.php" method="post">
        <textarea type="text" rows="15" cols="100" id="inputtext" name="inputtext" placeholder="PHP bad" style="border-top-style:hidden;border-right-style:hidden;border-left-style:hidden;border-bottom-style:groove;"></textarea><br><br>
        <input type="text" id="find" name="find" placeholder="PHP" style=""><br><br>
        <input type="text" id="replace" name="replace" placeholder="JS" style=""><br><br>
        <input type="submit" value="Replace">
    </form>
<?php
    error_reporting(E_ERROR | E_PARSE);
    if (isset($_GET["debug"])) {
        highlight_file("./index.php");
    }
    if ($_SERVER["REQUEST_METHOD"] === "POST" && (!isset($_POST["inputtext"]) || !isset($_POST["find"]) || !isset($_POST["replace"]))) {
        die("<p style='color:#ff443e;font-weight:bold;'>Must enter inputtext, find and replace term</p>");
    } else {
        $out=preg_replace($_POST["find"], $_POST["replace"], $_POST["inputtext"]);
        echo "<textarea type='text' rows='15' cols='100' name='output' readonly='readonly'>" . $out . "</textarea>";
    }
?>
    </body>
</html>
