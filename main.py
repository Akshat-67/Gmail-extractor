import os
import asyncio
from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatGoogle

# Load environment variables from .env file
load_dotenv()

async def main():
    # 1. Configure the Browser
    # The 'user_data' directory will be created in your project folder.
    # This stores session data (cookies, etc.) so that after you log in once, you stay logged in.
    data_dir = os.path.join(os.getcwd(), "user_data")

    # We initialize the Browser directly with the user_data_dir for persistence
    browser = Browser(
        user_data_dir=data_dir,
        headless=False, # Set to True if you want to hide the browser
    )

    # 2. Initialize the LLM (Gemini)
    # Using ChatGoogle from browser_use for better compatibility with the agent
    # Model: gemini-2.5-flash (as requested by user)
    llm = ChatGoogle(
        model="gemini-2.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    # 3. Define the Task
    task = (
        "Go to https://mail.google.com/. "
        "If not logged in, wait for the user to log in manually. "
        "Search for emails containing: RM OR Registry OR 'Sale deed'. "
        "Find the first 5 matching emails. "
        "For each email, extract the Subject, Sender, and Date. "
        "Print these details to the console."
    )

    # 4. Initialize the Agent
    agent = Agent(
        task=task,
        llm=llm,
        browser=browser
    )

    # 5. Run the Agent
    print("Starting Browser Use Agent...")
    print(f"Session data will be stored in: {data_dir}")
    print("Please monitor the browser window. You may need to log in to Gmail manually the first time.")

    try:
        result = await agent.run()
        print("\n--- Task Result ---")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
