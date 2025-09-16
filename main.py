import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

async def main():
    print(os.getenv("OPEN_API_KEY"))
    print("Hello World")

if __name__ == '__main__':
    asyncio.run(main())