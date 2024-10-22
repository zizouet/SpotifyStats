# SpotifyStats

SpotifyStats is an application designed to analyze your Spotify listening habits and generate insightful reports. Discover what is the song you hate the most, how much time you spend listening to each artist, and explore other cool features.
In the output/ directory you can find an example report !

## Table of Contents

- [Features](#features)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Total Listening Time**: Get the total duration of your listening activity.
- **Top Songs**: Identify your most played songs.
- **Top Artists**: Discover your favorite artists.
- **Top Albums**: See which albums you listen to the most.
- **Listening Time of Day**: Analyze what time of day you listen to music the most.
- **Most Skipped Songs**: Find out which songs you skip the most.
- **PDF Report**: Generate a detailed PDF report of your listening habits.
- **More to Come**: Stay tuned for additional features and insights.

## Project Architecture

- **src/**: Contains all the code necessary for the application to run.
- **output/**: Contains all the data analysis generated by the application, presented in a PDF report.
- **data/**: Contains data to run the analysis.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SpotifyStats.git
    cd SpotifyStats
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your Spotify data files in the `data/` directory, the data should be .json files from the spotify [extended streaming history](https://www.spotify.com/account/privacy/).

2. Run the main routine to generate the analysis and report:
    ```bash
    python src/main.py
    ```

3. The generated PDF report will be available in the `output/` directory.

## Examples

Here are some examples of the data and insights you can get from SpotifyStats:

- **Total Listening Time**: See how much time you spend listening to music.
- **Top Songs**: Identify your most played songs.
- **Top Artists**: Discover your favorite artists.
- **Top Albums**: See which albums you listen to the most.
- **Listening Time of Day**: Analyze what time of day you listen to music the most.
- **Most Skipped Songs**: Find out which songs you skip the most.

And much more to come ! Don't hesitate to tell me your best data ideas !

## License

This project is licensed under the GLP V3.0 License - see the [LICENSE](LICENSE) file for details.

---

Enjoy analyzing your Spotify data with SpotifyStats!
