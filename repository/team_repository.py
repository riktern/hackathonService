from infrastructure.db.connection import pg_connection
from persistent.db.team import Team
from sqlalchemy import insert, select


class TeamRepository:
    def __init__(self) -> None:
        self._sessionmaker = pg_connection()

    async def create_team(self, owner_id: int, name: str, size: int, members: list[int]) -> None:
        stmp = insert(Team).values({
            "owner_id": owner_id,
            "name": name,
            "size": size,
            "members": members
        })

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    async def get_team_by_id(self, team_id: int) -> dict | None:
        stmp = select(Team).where(Team.team_id == team_id).limit(1)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row = resp.fetchone()
        if row is None:
            return None

        return dict(row)
