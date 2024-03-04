import asyncio
import logging
from src.main import main

if __name__ == "__main__":
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        encoding="utf-8",
        handlers=[logging.FileHandler("src/logging.log")],
    )
    asyncio.run(main())
