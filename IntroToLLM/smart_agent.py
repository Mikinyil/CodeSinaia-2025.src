import ollama

class SmartAgent:
    # Private constants
    __context_file = 'IntroToLLM/context_prompt.txt'
    __ollama_model = 'gemma3:1b'

    def __init__(self):
            # Read the content of 'context_prompt.txt' into a string variable
        with open(self.__context_file, 'r', encoding='utf-8') as file:
            self.__context = file.read()
        self.__chat = [self.__context]

    def __str__(self):
        return f"SmartAgent(context_file='{self.__context_file}', ollama_model='{self.__ollama_model}')"

    def chat(self, prompt):
        self.__chat.append(prompt)
        full_prompt = "\n".join(self.__chat)
        response = ollama.chat(
            model=self.__ollama_model,
            messages=[
                {'role': 'user', 'content': full_prompt}
            ])
        return response['message']['content']
        
