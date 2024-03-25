"""Pass."""

import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import crud_bonus, crud_contract, crud_job_type, crud_skill
from app.models import (
    ApplicantResponsibility,
    JobOpening,
    Skill,
    StopList,
    User,
)


class CRUDJobOpening:
    """Pass."""

    def __init__(self, model):
        """Initialize the CRUDBase object."""
        self.model = model

    async def create_job_opening(
        self,
        obj_schema,
        session: AsyncSession,
        user: User,
    ):
        """Create a new object."""
        obj_data = obj_schema.model_dump()

        obj_data["employer_id"] = user.id
        obj_data["id"] = uuid.uuid4()
        responsibilities = obj_data.pop("responsibilities")
        job_types = obj_data.pop("job_types")
        skills = obj_data.pop("skills")
        bonuses = obj_data.pop("bonuses")
        contracts = obj_data.pop("contracts")
        stop_list = obj_data.pop("stop_list")

        db_obj = self.model(**obj_data)
        session.add(db_obj)

        db_obj = await session.get(self.model, db_obj.id)

        for resp in responsibilities:
            session.add(
                ApplicantResponsibility(
                    job_opening_id=db_obj.id,
                    description=resp["description"],
                ),
            )

        for job_type in job_types:
            job_type_obj = await crud_job_type.get_by_description(
                session,
                job_type["description"],
            )
            if job_type_obj:
                db_obj.job_types.append(job_type_obj)

        for skill in skills:
            skill_obj = await crud_skill.get_by_name(session, skill["name"])
            if not skill_obj:
                skill_obj = Skill(name=skill["name"])
                session.add(skill_obj)
            db_obj.skills.append(skill_obj)

        for bonus in bonuses:
            bonus_obj = await crud_bonus.get_by_description(
                session,
                bonus["description"],
            )
            if bonus_obj:
                db_obj.bonuses.append(bonus_obj)

        for contract in contracts:
            contract_obj = await crud_contract.get_by_name(
                session,
                contract["name"],
            )
            if contract_obj:
                db_obj.contracts.append(contract_obj)

        for stop in stop_list:
            session.add(
                StopList(
                    job_opening_id=db_obj.id,
                    description=stop["description"],
                ),
            )

        # await session.commit()
        # await session.refresh(db_obj)
        return db_obj


crud_job_opening = CRUDJobOpening(JobOpening)
