from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a research assistant.

Answer the question strictly using the context below.
If the answer is not present in the context, say:
"I could not find this information in the provided papers."

Context:
{context}

Question:
{question}

Answer:
"""
)


class RAGQuestionAnswering:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.llm = ChatOpenAI(model=model_name, temperature=0)

    def generate_answer(self, context_chunks, question):
        context_text = "\n\n".join(context_chunks)

        prompt = RAG_PROMPT.format(
            context=context_text,
            question=question
        )

        response = self.llm.invoke(prompt)
        return response.content
