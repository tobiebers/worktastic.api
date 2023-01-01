from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.job import job_list, Job


class JobListResource(Resource):

    def get(self):
        data = []
        for job in Job.get_all_published():
            if job.is_published is True:
                data.append(job.data)

        return{"data": data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        job = Job(
            title=data['title'],
            description=data['description'],
            salary=data['salary']
        )

        job.save()

        return job.data

class JobResource(Resource):

    def get(self, job_id):

        job = Job.get_by_id(job_id=job_id)

        if job is None:
            return {'message':'job not found'}, HTTPStatus.NOT_FOUND

        if job.is_published is False:
            return{'messege':'job not published'}

        return job.data, HTTPStatus.OK

    def put(self, job_id):
        data = request.get_json()

        job = next( (job for job in job_list
                     if job.id is job_id ), None)

        if job is None:
            return {'message':'job not found'}, HTTPStatus.NOT_FOUND

        job.title = data['title']
        job.description = data['description']
        job.salary = data['salary']

        return job.data, HTTPStatus.OK

    def delete(self, job_id):
        job = next((job for job in job_list
                    if job.id is job_id), None)

        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND

        job_list.remove(job)

        return{}, HTTPStatus.NO_CONTENT


class JobPublishResource(Resource):

    def put(self, job_id):
        job = next( (job for job in job_list
                     if job.id is job_id ), None)

        if job is None:
            return {'message':'job not found'}, HTTPStatus.NOT_FOUND

        job.is_published = True
        return{}, HTTPStatus.OK

    def delete(self, job_id):
        job = next((job for job in job_list
                    if job.id is job_id), None)

        if job is None:
            return {'message': 'job not found'}, HTTPStatus.NOT_FOUND

        job.is_published = False
        return {}, HTTPStatus.OK









