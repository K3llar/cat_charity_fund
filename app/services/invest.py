import datetime as dt

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


async def check_charity_projects_for_investing(
        new_donation: Donation,
        session: AsyncSession,
):
    while new_donation.fully_invested is False:
        value = new_donation.full_amount - new_donation.invested_amount
        db_charity_project = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == False
            )
        )
        db_charity_project = db_charity_project.scalars().first()
        if db_charity_project:
            project_value = db_charity_project.full_amount - db_charity_project.invested_amount
            if value > project_value:
                db_charity_project.invested_amount += project_value
                db_charity_project.fully_invested = True
                db_charity_project.close_date = dt.datetime.now()
                new_donation.invested_amount += project_value
                # session.add(new_donation)
                # session.add(db_charity_project)
            if value < project_value:
                db_charity_project.invested_amount += value
                new_donation.invested_amount += value
                new_donation.fully_invested = True
                new_donation.close_date = dt.datetime.now()
                # session.add(new_donation)
                # session.add(db_charity_project)
            if value == project_value:
                db_charity_project.invested_amount += project_value
                new_donation.invested_amount += value
                db_charity_project.fully_invested = True
                new_donation.fully_invested = True
                db_charity_project.close_date = dt.datetime.now()
                new_donation.close_date = dt.datetime.now()
                # session.add(new_donation)
                # session.add(db_charity_project)
            session.add(new_donation)
            session.add(db_charity_project)
            await session.commit()
            await session.refresh(new_donation)
        else:
            break
    return new_donation


