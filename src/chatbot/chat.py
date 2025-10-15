import google.generativeai as genai
from util import jsonltovector

class AIEngine:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def chat_with_ai(self, user_input):

        #jsonltovector.add_jsonl_to_chromadb("D:\Magesh Ai Workspace\RAGify\my-cli-app\input_article_details.jsonl","RAGify_Collection","chromadb_local")
        context=jsonltovector.generate_reply(user_input)
        # Step 2: Combine context + user query
        prompt = f"Use the following context to answer:\n{context}\n\nUser question: {user_input}"


        response = self.model.generate_content(
            user_input,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 2000
            }
        )
        return "Bot: " + response.text.strip() if hasattr(response, "text") else "No response generated."



