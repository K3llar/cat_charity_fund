import datetime as dt

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation
from app.models.base_model import BaseModel


async def check_charity_projects_for_investing(
        new_donation: Donation,
        session: AsyncSession,
):
    while new_donation.fully_invested is False:
        db_charity_project = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == False
            )
        )
        db_charity_project = db_charity_project.scalars().first()
        if db_charity_project:
            new_donation, db_charity_project = calculation(new_donation, db_charity_project)
            session.add(new_donation)
            session.add(db_charity_project)
            await session.commit()
            await session.refresh(new_donation)
        else:
            break
    return new_donation


async def check_donations_for_investing(
        new_project: CharityProject,
        session: AsyncSession,
):
    while new_project.fully_invested is False:
        db_donation = await session.execute(
            select(Donation).where(
                Donation.fully_invested == False
            )
        )
        db_donation = db_donation.scalars().first()
        if db_donation:
            new_project, db_donation = calculation(new_project, db_donation)
            session.add(new_project)
            session.add(db_donation)
            await session.commit()
            await session.refresh(new_project)
        else:
            break
    return new_project


def calculation(
        input_model: BaseModel,
        db_model: BaseModel,
):
    input_value = input_model.full_amount - input_model.invested_amount
    db_value = db_model.full_amount - db_model.invested_amount
    if input_value > db_value:
        db_model.invested_amount += db_value
        db_model.fully_invested = True
        db_model.close_date = dt.datetime.now()
        input_model.invested_amount += db_value
    elif input_value < db_value:
        db_model.invested_amount += input_value
        input_model.invested_amount += input_value
        input_model.fully_invested = True
        input_model.close_date = dt.datetime.now()
    elif input_value == db_value:
        input_model.invested_amount += db_value
        db_model.invested_amount += input_value
        input_model.fully_invested = db_model.fully_invested = True
        input_model.close_date = db_model.close_date = dt.datetime.now()
    return input_model, db_model
