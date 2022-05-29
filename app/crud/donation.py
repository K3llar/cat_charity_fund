from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.models.donation import Donation
from app.schemas.donation import DonationCreate
from app.schemas.user import UserDB


async def create_donation(
        new_donation: DonationCreate,
        session: AsyncSession,
        user: UserDB
) -> Donation:
    new_donation_data = new_donation.dict()
    if user:
        new_donation_data['user_id'] = user.id
    db_donation = Donation(**new_donation_data)
    session.add(db_donation)
    await session.commit()
    await session.refresh(db_donation)
    return db_donation


async def get_all_donations_from_db(
        session: AsyncSession
) -> list[Donation]:
    all_donations = await session.execute(select(Donation))
    all_donations = all_donations.scalars().all()
    return all_donations


async def get_all_donations_by_user(
        session: AsyncSession,
        user: UserDB,
):
    donations = await session.execute(
        select(Donation).where(
            Donation.user_id == user.id
        )
    )
    return donations.scalars().all()
