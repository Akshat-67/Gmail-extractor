# Legal Workflow AI Browser Agent (Starter)

This project uses [Browser Use](https://github.com/browser-use/browser-use) and Google's Gemini API to automate Gmail tasks.

## Features
- **Persistent Session:** Remembers your Gmail login after the first time.
- **Automated Search:** Searches for "RM", "Registry", and "Sale deed" in Gmail.
- **Metadata Extraction:** Extracts subject, sender, and date from found emails.

## Prerequisites
- Python 3.11 or higher
- A Google Gemini API Key

## Setup Instructions

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Install Playwright Browsers:**
    ```bash
    playwright install chromium
    ```

3.  **Configure Environment Variables:**
    - Open the `.env` file.
    - Ensure your `GOOGLE_API_KEY` is correctly set.

4.  **Run the Agent:**
    ```bash
    python main.py
    ```

## Important Notes for First Run
- When you run the script for the first time, a browser window will open.
- **Manual Action Required:** You will likely need to log in to your Gmail account manually.
- Once logged in, the agent will proceed with the search task.
- On subsequent runs, the agent will use the saved session in the `user_data` folder and should not require you to log in again.

## Project Structure
- `main.py`: The entry point for the AI agent.
- `requirements.txt`: Python dependencies.
- `.env`: Secret configuration (API keys).
- `user_data/`: (Generated after first run) Stores browser profile and cookies.
