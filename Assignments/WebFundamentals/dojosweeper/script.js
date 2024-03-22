var theDojo = [[1, 0, 1, 1, 1, 0, 4, 0, 8, 0],
[3, 1, 0, 7, 0, 0, 6, 0, 8, 8],
[5, 0, 7, 0, 3, 6, 6, 6, 0, 0],
[2, 3, 0, 9, 0, 0, 6, 0, 8, 0],
[6, 0, 3, 3, 0, 2, 0, 3, 0, 4],
[0, 0, 3, 3, 0, 0, 2, 2, 3, 0],
[0, 0, 0, 0, 5, 0, 1, 2, 0, 6],
[2, 2, 2, 2, 0, 7, 1, 1, 1, 0],
[5, 2, 0, 2, 0, 0, 0, 1, 1, 2],
[9, 2, 2, 2, 0, 7, 0, 1, 1, 0]];
var dojoDiv = document.querySelector("#the-dojo");

// Creates the rows of buttons for this game
function render(theDojo) {
    var result = "";
    for (var i = 0; i < theDojo.length; i++) {
        for (var j = 0; j < theDojo[i].length; j++) {
            result += `<button class="tatami" onclick="howMany(${i}, ${j}, this)"></button>`;
        }
    }
    return result;
}

// TODO - Make this function tell us how many ninjas are hiding 
//        under the adjacent (all sides and corners) squares.
//        Use i and j as the indexes to check theDojo.
function howMany(i, j, element) {
    console.log({ i, j });

    function howMany(i, j, element) {
        var ninjasCount = 0;

        // Iterate over adjacent squares
        for (var row = i - 1; row <= i + 1; row++) {
            for (var col = j - 1; col <= j + 1; col++) {
                // Check if the indices are within theDojo bounds
                if (row >= 0 && row < theDojo.length && col >= 0 && col < theDojo[row].length) {
                    // Check if there is a ninja in the adjacent square
                    if (theDojo[row][col] === 2) {
                        ninjasCount++;
                    }
                }
            }
        }

        // Display the number of ninjas
        alert(`There are ${ninjasCount} ninjas hiding in adjacent squares.`);
    }

}

