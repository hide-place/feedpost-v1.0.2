// Get elements from the HTML document
const usernameInput = document.getElementById('usernameInput');
const postInput = document.getElementById('postInput');
const postBtn = document.getElementById('postBtn');
const postFeed = document.getElementById('posts');
const username = document.getElementById('username');
const postText = document.getElementById('postText');
const addPostBtn = document.getElementById('add');
const main = document.getElementById('main');

// Function to get the current date and time in a formatted string
function getCurrentFormattedDateTime() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // getMonth() is zero-based
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    return `${year}/${month}/${day} ${hours}:${minutes}`;
}

// Function to publish a post
function publishPost() {
    var time = getCurrentFormattedDateTime();
    var usernameInputValue = usernameInput.value;
    var postInputValue = postInput.value;

    // Check if both username and post input fields are not empty
    if (usernameInputValue !== '' && postInputValue !== '') {
        // Create a new post element and insert it at the beginning of the post feed
        postFeed.insertAdjacentHTML('afterbegin', `
            <div class="post">
                <h3>@${usernameInputValue}</h3>
                <p>${postInputValue}</p>
                <p class="time">${time}</p>
            </div>
        `);

        // Clear the post input field and hide the main section
        postInput.value = '';
        main.style.display = 'none';
    }
}

// Function to show or hide the main section
function showOrHideMain() {
    if (main.style.display === 'none') {
        main.style.display = 'flex';
    } else if (main.style.display === '') {
        main.style.display = 'flex';
    } else {
        main.style.display = 'none';
    }
}


// Add event listeners to the post button and add post button
postBtn.addEventListener('click', publishPost);
addPostBtn.addEventListener('click', showOrHideMain);