import asyncio
from db import db, connect_db, disconnect_db
from prisma import Json


async def main() -> None:
    await connect_db()  # Połączenie z bazą

    processor = await db.processor.create(data={
        "producer": "AMD",
        "name": "Ryzen 7 7800X",
        "socket": "AM5",
        "chipsets": Json({
            'supported': ["B650", "X670", "X670E"]
        }),
        "architecture": "Zen 4",
        "timing": "4.2 GHz Base / 5.4 GHz Boost",
        "cores": 8,
        "threads": 16,
        "Unlocked_multiplier": True,
        "market": "X-kom"
    })

    await disconnect_db() # Rozłączenie z bazą

if __name__ == "__main__":
    asyncio.run(main())