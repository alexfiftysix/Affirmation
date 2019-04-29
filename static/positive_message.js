console.log(base_url);
// TODO: Link to this file

// console.log(window.history);
history.pushState({seed: seed_value}, "affirmation", window.location);
// TODO: Back behaviour should still work as expected
//   History is pushed to avoid back sending the user to the previous site (not page)
//   But this now makes the user need to press back twice to go back one affirmation

function go_back() {
    if (window.history.length !== 3) {
        // TODO: Make this actually work - currently only works on brand new tabs
        // May be able to use cookies to store states?
        window.history.go(-2);
    }
}

document.addEventListener("keydown", event => {
    // If users press 'enter' or 'right arrow' the page refreshes, showing a new affirmation
    console.log(event.keyCode);
    if (event.keyCode === 13 || event.keyCode === 39) {
        console.log(window.location);
        window.location.replace(base_url);
    }

    // if user presses left arrow, go to previous affirmation
    else if (event.keyCode === 37) {
        console.log(window.history);
        go_back();
    }
});