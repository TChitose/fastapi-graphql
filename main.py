import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from schema import Query, Mutation

app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))


@app.get('/ping')
def ping():
    return {'ping': 'pong'}

@app.get('/pika')
def pika():
    return {'pika': 'pong'}