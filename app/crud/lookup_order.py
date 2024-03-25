"""Pass."""

import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import crud_legal_form, crud_recruiter_responsibility
from app.crud.job_opening import crud_job_opening
from app.models import LookupOrder, RecruiterRequirement, User


class CRUDLookupOrder:
    """Pass."""

    def __init__(self, model):
        """Initialize the CRUDBase object."""
        self.model = model

    async def create_lookup_order(
        self,
        obj_schema,
        session: AsyncSession,
        user: User,
    ):
        """Create a new object."""
        job_opening = await crud_job_opening.create_job_opening(
            obj_schema.job_opening,
            session,
            user,
        )

        obj_data = obj_schema.model_dump()
        obj_data.pop("job_opening")
        legal_forms = obj_data.pop("legal_form")
        responsibilities = obj_data.pop("responsibilities")
        recruiter_requirements = obj_data.pop("recruiter_requirements")
        obj_data["employer_id"] = user.id
        obj_data["job_opening_id"] = job_opening.id
        obj_data["id"] = uuid.uuid4()

        db_obj = self.model(**obj_data)

        for legal_form in legal_forms:
            legal_form_obj = await crud_legal_form.get_by_name(
                session,
                legal_form["name"],
            )
            if legal_form_obj:
                db_obj.legal_forms.append(legal_form_obj)

        for resp in responsibilities:
            resp_obj = await crud_recruiter_responsibility.get_by_description(
                session,
                resp["description"],
            )
            if resp_obj:
                db_obj.responsibilities.append(resp_obj)

        for req in recruiter_requirements:
            session.add(
                RecruiterRequirement(
                    lookup_order_id=db_obj.id,
                    description=req["description"],
                ),
            )

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


crud_lookup_order = CRUDLookupOrder(LookupOrder)
