import streamlit as st

st.set_page_config(
    page_title="دستیار هوشمند سفر",
    layout="wide"
)

from dotenv import load_dotenv
from utils.loader import load_json
from core.retriever import Retriever
from core.llm_client import AvalAILLM
from core.agent import TravelAgent

load_dotenv()

st.title("✈️ دستیار هوشمند برنامه‌ریزی سفر")

query = st.text_input("برنامه سفر خود را توضیح دهید:")

if query:
    trains = load_json("data/trains.json")
    flights = load_json("data/flights.json")
    hotels = load_json("data/hotels.json")

    retrievers = [
        Retriever(trains),
        Retriever(flights),
        Retriever(hotels)
    ]

    agent = TravelAgent(retrievers, AvalAILLM())

    with st.spinner("در حال برنامه‌ریزی سفر..."):
        response = agent.plan_trip(query)

    st.success("برنامه پیشنهادی:")
    st.write(response)
