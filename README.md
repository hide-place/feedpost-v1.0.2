# FeedPost using Flask and Firebase

This project is a simple web application that allows users to post messages and view them in real-time. It uses Flask as the backend framework, HTML, CSS, and JavaScript for the frontend, and Firebase Realtime Database for data storage.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/hide-place/feedpost-v1.0.2.git
cd feedpost
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install flask firebase-admin
```

4. Create a Firebase project and enable the Realtime Database:
   - Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project.
   - Click on "Realtime Database" in the left menu and then "Create Database".
   - Choose "Start in test mode" and select your preferred location.
   - Click on "Enable" to enable the Realtime Database.

5. Generate a service account key file:
   - In the Firebase Console, go to "Project Settings" > "Service accounts".
   - Click on "Generate new private key" and save the JSON file to your project directory (e.g., `serviceAccount.json`).

6. Update the `Certificate` variable in `database.py` with the path to your `serviceAccount.json` file.

7. Run the Flask app:
```bash
python app.py
```

## Usage

- Open your web browser and navigate to `http://localhost:9000`.
- You should see the FeedPost homepage with a header, a "+" button, and a section for posting messages.
- Enter your name and a message in the input fields, and click the "POST" button to publish your message.
- The message will be displayed on the page and added to the Firebase Realtime Database.
- Other users who visit the page will see the new messages in real-time.

## Code Structure

- `app.py`: The main Flask application file. Defines routes and handles requests.
- `database.py`: Contains functions for interacting with the Firebase Realtime Database.
- `static/scripts/script.js`: JavaScript file for handling user interactions and updating the post feed.
- `static/styles/style.css`: CSS file for styling the web application.
- `templates/index.html`: The HTML template for the FeedPost homepage.



## Future Features

- Implement user authentication to allow only authenticated users to post messages.
- Add support for deleting messages.
- Improve the UI/UX of the web application.

## Known Issues

- The `@store_post_data` function is not currently being used in the project. You can track its progress or contribute to its implementation in the future.


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


## License

This project is licensed under the MIT License. See the [LICENSE](License.md) file for more information.
