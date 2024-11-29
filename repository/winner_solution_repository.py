from infrastructure.db.connection import pg_connection
from persistent.db.winner_solution import WinnerSolution
from sqlalchemy import insert, select


class WinnerSolutionRepository:
    def __init__(self) -> None:
        self._sessionmaker = pg_connection()

    async def add_solution(self, hack_id: int, team_id: int, win_money: float, link_to_solution: str, link_to_prez: str, can_share: bool) -> None:
        stmp = insert(WinnerSolution).values({
            "hack_id": hack_id,
            "team_id": team_id,
            "win_money": win_money,
            "link_to_solution": link_to_solution,
            "link_to_prez": link_to_prez,
            "can_share": can_share
        })

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    async def get_solution_by_hack_and_team(self, hack_id: int, team_id: int) -> dict | None:
        stmp = select(WinnerSolution).where(
            (WinnerSolution.hack_id == hack_id) & (WinnerSolution.team_id == team_id)
        ).limit(1)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row = resp.fetchone()
        if row is None:
            return None

        return dict(row)
