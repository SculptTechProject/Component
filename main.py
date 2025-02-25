import asyncio
from db import db, connect_db, disconnect_db


async def main():
    await connect_db()  # Połączenie z bazą

    # Tworzenie tabeli (automatycznie przy migracji)
    await db.test.create(data={"name": "Example"})

    # Pobranie wszystkich rekordów
    records = await db.test.find_many()
    print(records)

    await disconnect_db()  # Zamknięcie połączenia


# Uruchomienie event loopa
asyncio.run(main())
