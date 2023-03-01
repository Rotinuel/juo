from flask_sqlalchemy import SQLAlchemy, create_engine, text

db_connection_string = "mysql+pymysql://umnnimetuxp59phbz9v8:pscale_pw_eWchJ41ZVbU3pCyV4xUQ1alIinALYEpOcVJWEk2BWtA@us-east.connect.psdb.cloud/juocareers?charset=utf8mb4"


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
    return [ convert_to_dict(row) for row in result.all()]


def convert_to_dict(row):
    id, title, location, salary, currency, responsibilities, requirements = row
    data = dict(id=id, title=title, salary=salary, currency=currency, location=location, requirements=requirements, responsibilities=responsibilities)
    return data


print(load_jobs_from_db())
