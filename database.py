from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://umnnimetuxp59phbz9v8:pscale_pw_eWchJ41ZVbU3pCyV4xUQ1alIinALYEpOcVJWEk2BWtA@us-east.connect.psdb.cloud/juocareers?charset=utf8mb4"


engine = create_engine( db_connection_string,
    connect_args = {  
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"}

} )

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
        jobs.append.__dict__(row)
    return jobs