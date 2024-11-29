from infrastructure.db.connection import pg_connection
from persistent.db.hacker import Hacker
from sqlalchemy import insert, select, update


class HackerRepository:
    def __init__(self) -> None:
        self._sessionmaker = pg_connection()

    async def add_hacker(self, name: str, active_teams: list[int], roles: list[int]) -> None:
        stmp = insert(Hacker).values({
            "name": name,
            "active_teams": active_teams,
            "roles": roles
        })

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    async def get_hacker_by_id(self, user_id: int) -> dict | None:
        stmp = select(Hacker).where(Hacker.user_id == user_id).limit(1)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row = resp.fetchone()
        if row is None:
            return None

        return dict(row)

    async def update_hacker_roles(self, user_id: int, roles: list[int]) -> None:
        stmp = update(Hacker).where(Hacker.user_id == user_id).values({"roles": roles})

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
