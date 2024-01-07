<?php

echo "<!DOCTYPE html>";
require_once("header.html");

echo "<h1 class='c'>Spooky dogs</h1>";
echo "<body>";
if (isset($_GET['img'])) {
	echo "<div class='view'>";
	echo load_img($_GET['img']);
	echo "</div>";
} else {
	echo "<div class='grid-container'>";
	foreach (glob("images/*") as $img):
		echo "<div class='grid-item'>";
		echo "<a href='?img=".$img."'>";
		echo load_img($img);
		echo "</a>";
		echo "</div>";
	endforeach;
	echo "</div>";
};

echo "</body>";
echo "</html>";


function load_img($s) {
	return "<img src='data:image/png;base64,".base64_encode(file_get_contents(sanitize_input($s)))."'>";
}


// Protect against hackers trying to steal my files
function sanitize_input($s) {
	return preg_replace("/\.\.\//", "", $s);
};




// Flag is in /flag
?>
