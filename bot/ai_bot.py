import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config import (
    GROQ_API_KEY
)


class AIBot:

    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.3-70b-versatile')

    def invoke(self, question):
        prompt = PromptTemplate(
            input_variables=['texto'],
            template='''
            Responda as perguntas dos usuários com base no texto abaixo.
            Você é um assistente especializado em tirar dúvidas sobre o caju sendo um representante da empresa cardeal.
            Tire dúvidas dos possíveis alunos que entrarem em contato.
            Responda de forma natural, agradável e respeitosa. Seja objetivo nas respostas, com informações
            claras, suscinta e diretas. Foque em ser natural e humanizado, como um diálogo comum entre duas pessoas.
            Leve em consideração também o histórico de mensagens da conversa com o usuário.
            Responda sempre em português brasileiro.
            <texto>
            {texto}
            </texto>
            '''
        )
        chain = prompt | self.__chat | StrOutputParser()
        response = chain.invoke({
            'texto': question,
        })
        return response
