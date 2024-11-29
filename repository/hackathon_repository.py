from infrastructure.db.connection import pg_connection
from persistent.db.hackathon import Hackathon
from sqlalchemy import insert, select


class HackathonRepository:
    def __init__(self) -> None:
        self._sessionmaker = pg_connection()

    async def create_hackathon(self, name: str, task_description: str, start_of_registration: str, end_of_registration: str, start_of_hack: str, end_of_hack: str, amount_money: float, type: str) -> None:
        stmp = insert(Hackathon).values({
            "name": name,
            "task_description": task_description,
            "start_of_registration": start_of_registration,
            "end_of_registration": end_of_registration,
            "start_of_hack": start_of_hack,
            "end_of_hack": end_of_hack,
            "amount_money": amount_money,
            "type": type
        })

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    async def get_hackathon_by_id(self, hack_id: int) -> dict | None:
        stmp = select(Hackathon).where(Hackathon.hack_id == hack_id).limit(1)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row = resp.fetchone()
        if row is None:
            return None

        return dict(row)
