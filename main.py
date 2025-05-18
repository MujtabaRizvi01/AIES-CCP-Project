from agents.news_agent import news_search_agent
from agents.technical_agent import technical_analyzer_agent
from agents.fundamental_agent import fundamental_analyzer_agent
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
import os
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
phi_api_key = os.getenv("PHI_API_KEY")


news_agent = news_search_agent()
tech_agent = technical_analyzer_agent()
fundamental_agent = fundamental_analyzer_agent()


# Setup and serve the playground application
app = Playground(agents=[news_agent, tech_agent, fundamental_agent]).get_app()

if __name__ == "__main__":
    print("Starting the app...")
    serve_playground_app("main:app", reload=True)