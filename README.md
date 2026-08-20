# Music N More

A lightweight desktop music player built with Python for managing and playing a local music library.

## Features

* **Local Music Playback** — Play songs stored in a local music library.
* **Playback Controls** — Play, pause, stop, skip, and control playback.
* **Song Information** — Retrieve and display song metadata and duration.
* **Progress Tracking** — Track playback progress and seek through songs.
* **Local Music Library** — Load songs from the project's music directory.
* **CSV-Based Song Data** — Store and manage song information using CSV.
* **Desktop GUI** — Interactive interface built with Tkinter.

## Tech Stack

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| **Python**  | Core application logic    |
| **Tkinter** | Graphical user interface  |
| **Pygame**  | Audio playback            |
| **Mutagen** | MP3 metadata and duration |
| **CSV**     | Song data management      |

## Project Structure

```text
musicnmore/
├── songs/              # Local music library
├── main.py             # Main application
├── music.csv           # Song/library data
├── music.ico           # Application icon
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites

Make sure Python 3 is installed.

Install the required dependencies:

```bash
pip install pygame mutagen
```

Tkinter is included with most standard Python installations.

### Installation

Clone the repository:

```bash
git clone https://github.com/AbhiBD/musicnmore.git
```

Navigate to the project directory:

```bash
cd musicnmore
```

Install the dependencies:

```bash
pip install pygame mutagen
```

Add your `.mp3` files to the `songs/` directory.

Run the application:

```bash
python main.py
```

## How It Works

Music N More uses a simple local-library architecture:

```text
             ┌─────────────────┐
             │   Local Songs   │
             │    /songs/      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Song Metadata  │
             │  CSV / Mutagen  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Tkinter GUI    │
             │                 │
             │  Song Selection │
             │  Controls       │
             │  Progress Bar   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Pygame Mixer    │
             │ Audio Playback  │
             └─────────────────┘
```

The application uses local audio files and song data while Python libraries handle playback, metadata extraction, and the graphical interface.

## Project Scope

Music N More was developed as a practical Python application to explore GUI development, audio playback, file handling, and event-driven programming.

The project demonstrates:

* GUI development with **TKinter**
* Event-driven programming
* Audio playback with **PyGame**
* MP3 metadata extraction with **mutagen**
* File and directory handling
* CSV data management
* Playback state and progress tracking
* Interactive desktop application development
