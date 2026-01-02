class TravelAgent:
    def __init__(self, retrievers, llm):
        self.retrievers = retrievers
        self.llm = llm

    def plan_trip(self, user_query):
        context = []

        for retriever in self.retrievers:
            context.extend(retriever.search(user_query, top_k=3))

        context_text = "\n".join(
            [f"- {c['description']} (قیمت: {c.get('price', 'نامشخص')})" for c in context]
        )

        prompt = f"""
کاربر چنین درخواستی دارد:
{user_query}

اطلاعات موجود:
{context_text}

بر اساس اطلاعات بالا یک برنامه سفر پیشنهادی به زبان فارسی ارائه بده.
"""

        return self.llm.chat(prompt)
