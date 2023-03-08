from flask import request
from sqlalchemy import  create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION']


engine = create_engine( db_connection_string,
    connect_args = {  
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"}

} )


# def load_jobs_from_db2():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from jobs"))
#     jobs = []
#     for row in result.all():
#         data = convert_to_dict(row)
#         jobs.append(data)
#     return jobs

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
    return [ convert_to_dict(row) for row in result.all() ]


def convert_to_dict(row):
    id, title, location, salary, currency, responsibilities, requirements = row
    data = dict(id=id, title=title, salary=salary, currency=currency, location=location, requirements=requirements, responsibilities=responsibilities)
    return data


def load_job_from_db(id):
    with engine.connect() as conn:
        stmt = text("SELECT * FROM jobs WHERE id=:job_id")
        result = conn.execute(stmt, dict(job_id=id))
        r = result.first()
        if r:
            return convert_to_dict(r)
    