from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI ()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get ("/")
def index ():
    return {
        "messsage": "Welcome to the FastAPI application!",
    }

@app.get ("/api/params")
def search (request: Request):
    parameters = list ()
    parameter_values = list ()

    for parameter_name in request.query_params.keys ():
        
        parameter_values = request.query_params.getlist (parameter_name)
        for value in parameter_values:
            parameters.append ({
                "name": parameter_name,
                "value": value
            })


    print (parameters)

    return {
        "parameters": parameters,
    }

from pydantic import BaseModel


class Job (BaseModel):
    name: str
    cost: int

jobs = list ()

@app.post ("/api/create")
def create (job: Job):
    jobs.append (job)

    return {
        "job": job
    }

@app.get ("/api/jobs")
def get_jobs ():
    return {
        "jobs": jobs
    }

@app.delete ("/api/delete/{job_no}")
def delelte_job (job_no: int):
    if job_no < 0 or job_no >= len (jobs):
        return {
            "error": "Job not found"
        }

    job = jobs.pop (job_no)

    return {
        "job": job
    }


