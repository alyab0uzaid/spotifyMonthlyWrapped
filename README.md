# Spotify Monthly Wrapped Web App

This project is a Flask-based web app that interacts with the Spotify API to create a custom playlist with your top songs from the last month. Users can log in with their Spotify account, and the app will generate a playlist called "Last Month's Top Songs" based on their recent listening habits.

## Features
- OAuth-based login to Spotify
- Fetch top 10 tracks from the last month (short-term listening data)
- Automatically create a playlist with these tracks in the user's Spotify account

## Tech Stack
- Python
- Flask
- Spotipy (Spotify Web API library for Python)
- HTML (for simple frontend display)

## Prerequisites
To run this project locally, you will need:
- Python 3.6+
- Spotify Developer account (create your app to get the client ID and secret)
- Flask
- Spotipy library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/spotify-monthly-wrapped.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd spotify-monthly-wrapped
    ```

3. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your Spotify credentials**:

    - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    - Create a new app and get your `CLIENT_ID` and `CLIENT_SECRET`.
    - Update the `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` in the `app.py` file with your app credentials.

5. **Run the Flask app**:

    ```bash
    python app.py
    ```

6. **Visit the app**:

    - Open a browser and go to `http://127.0.0.1:5000/`.
    - You will be prompted to log in to Spotify.
    - Once logged in, the app will automatically create a playlist with your top tracks from the last month.

## Usage

- After starting the app, you'll be redirected to Spotify to log in.
- Once authenticated, the app will create a playlist in your account with the top 10 songs you listened to over the last month.
- The playlist is named `"Last Month's Top Songs"` and is set to private by default.

## Environment Variables

This app requires the following environment variables, which you can set up in the `app.py` or use a `.env` file:

- `SPOTIPY_CLIENT_ID` - Your Spotify App's client ID
- `SPOTIPY_CLIENT_SECRET` - Your Spotify App's client secret
- `SPOTIPY_REDIRECT_URI` - The redirect URI you've set in your Spotify App settings (e.g., `http://127.0.0.1:5000/redirect`)
