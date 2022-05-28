from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.models.donation import Donation
from app.schemas.donation import DonationCreate


async def create_donation(
        new_donation: DonationCreate,
        session: AsyncSession,
) -> Donation:
    new_donation_data = new_donation.dict()
    db_donation = Donation(**new_donation_data)
    session.add(db_donation)
    await session.commit()
    await session.refresh(db_donation)
    return db_donation
