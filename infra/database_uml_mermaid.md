classDiagram
direction BT
class applicant_responsibilities {
   varchar description
   uuid job_opening_id
   uuid id
}
class bonus {
   varchar description
   uuid id
}
class contract {
   varchar name
   uuid id
}
class job_opening {
   varchar name
   varchar activity_field
   varchar description
   experienceduration work_experience
   educationlevel education
   integer min_salary
   integer max_salary
   workarrangements arrangement
   boolean insurance
   varchar location
   varchar additional_info
   uuid employer_id
   uuid id
}
class job_opening_bonus {
   uuid job_opening_id
   uuid bonus_id
   uuid id
}
class job_opening_contract {
   uuid job_opening_id
   uuid contract_id
   uuid id
}
class job_opening_file {
   json file
   uuid job_opening_id
   uuid id
}
class job_opening_job_type {
   uuid job_opening_id
   uuid job_type_id
   uuid id
}
class job_opening_skill {
   uuid job_opening_id
   uuid skill_id
   uuid id
}
class job_type {
   varchar description
   uuid id
}
class legal_form {
   varchar name
   uuid id
}
class lookup_order {
   uuid employer_id
   uuid job_opening_id
   tariffoption tariff
   integer bounty
   integer urgency_bounty
   timestamp awaited_employee_date
   timestamp first_cv_await_date
   integer recruiter_quantity
   experienceoption recruiter_experience
   legalformoption legal_form
   varchar additional_info
   uuid id
}
class lookup_order_file {
   json file
   uuid lookup_order_id
   uuid id
}
class lookup_order_legal_form {
   uuid lookup_order_id
   uuid legal_form_id
   uuid id
}
class lookup_order_recruiter {
   uuid lookup_order_id
   uuid recruiter_id
   uuid id
}
class lookup_order_recruiter_resp {
   uuid lookup_order_id
   uuid recruiter_resp_id
   uuid id
}
class recruiter_requirement {
   varchar description
   uuid lookup_order_id
   uuid id
}
class recruiter_responsibility {
   varchar description
   uuid id
}
class skill {
   varchar name
   uuid id
}
class stop_list {
   varchar description
   uuid job_opening_id
   uuid id
}
class user {
   varchar name
   varchar surname
   role role
   varchar(20) phone_number
   varchar(320) email
   varchar(1024) hashed_password
   boolean is_active
   boolean is_superuser
   boolean is_verified
   uuid id
}

applicant_responsibilities  -->  job_opening : job_opening_id:id
job_opening  -->  user : employer_id:id
job_opening_bonus  -->  bonus : bonus_id:id
job_opening_bonus  -->  job_opening : job_opening_id:id
job_opening_contract  -->  contract : contract_id:id
job_opening_contract  -->  job_opening : job_opening_id:id
job_opening_file  -->  job_opening : job_opening_id:id
job_opening_job_type  -->  job_opening : job_opening_id:id
job_opening_job_type  -->  job_type : job_type_id:id
job_opening_skill  -->  job_opening : job_opening_id:id
job_opening_skill  -->  skill : skill_id:id
lookup_order  -->  job_opening : job_opening_id:id
lookup_order_file  -->  lookup_order : lookup_order_id:id
lookup_order_legal_form  -->  legal_form : legal_form_id:id
lookup_order_legal_form  -->  lookup_order : lookup_order_id:id
lookup_order_recruiter  -->  lookup_order : lookup_order_id:id
lookup_order_recruiter  -->  user : recruiter_id:id
lookup_order_recruiter_resp  -->  lookup_order : lookup_order_id:id
lookup_order_recruiter_resp  -->  recruiter_responsibility : recruiter_resp_id:id
recruiter_requirement  -->  lookup_order : lookup_order_id:id
stop_list  -->  job_opening : job_opening_id:id
