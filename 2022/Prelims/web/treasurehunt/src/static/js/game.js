//from Javascript for Kids by No Starch Press
// Get a random number from 0 to size
var getRandomNumber = function(size) {
    return Math.floor(Math.random() * size);
};
// Calculate distance between click event and target
var getDistance = function(event, target) {
    var diffX = event.offsetX - target.x;
    var diffY = event.offsetY - target.y;
    return Math.sqrt((diffX * diffX) + (diffY * diffY));
};
// Get a string representing the distance
var getDistanceHint = function(distance) {
    //add if statement here to tell the person how close they are!
    $("#distance").text("You are " + Math.round(distance) + " pixels away");
}
// Set up our vaariables
var width = 500;
var height = 500;
var clicks = 0;

function makeTarget() {
    return {
        x: getRandomNumber(width),
        y: getRandomNumber(height)
    }
}

function findgoldenb00ty(){return undefined}

function showtreasure() { $("#treasure-quest").text(`Well done! You have unlocked a new treasure quest!
    Hidden in this web page are four treasures. All the treasure parts start with the letter g,
    end before a new line, and contain the text b00ty and, if ordered alphabetically and combined,
    will form a valid flag.`) }

// Create a random target location
var target = makeTarget();
// Add a click handler to the img element
$("#map").click(function(event) {
    clicks++;
    // Get distance between click event and target
    var distance = getDistance(event, target);
    // Convert distance to a hint
    var distanceHint = getDistanceHint(distance);
    // Update the #distance element with the new hint
    $("#distance").text(distanceHint);
    // If the click was close enough, tell them they won
    if (distance < 8) {
        alert("Found the treasure in " + clicks + " clicks!");
        clicks = 0;
        target = makeTarget();
        $("#distance").text("Can you find it again?");
        showtreasure();
    }
});
