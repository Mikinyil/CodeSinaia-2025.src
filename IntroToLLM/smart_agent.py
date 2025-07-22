import ollama

class SmartAgent:
    # Private constants
    __context_file = 'IntroToLLM/context_prompt.txt'
    __ollama_model = 'llama3.2'

    def __init__(self):
            # Read the content of 'context_prompt.txt' into a string variable
        with open(self.__context_file, 'r', encoding='utf-8') as file:
            self.__context = file.read()
        self.__chat = [{'role': 'user', 'content': self.__context}]

    def __str__(self):
        return f"SmartAgent(context_file='{self.__context_file}', ollama_model='{self.__ollama_model}')"

    def chat(self, prompt):
        self.__chat.append({'role': 'user', 'content': prompt})
        response = ollama.chat(
            model=self.__ollama_model,
            messages=self.__chat
        )
        agent_response = response['message']['content']
        self.__chat.append({'role': 'agent', 'content': agent_response})
        return agent_response

