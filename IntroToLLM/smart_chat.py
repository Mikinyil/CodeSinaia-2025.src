from smart_agent import SmartAgent

if __name__ == "__main__":
    agent = SmartAgent()
    prompt = ''
    while prompt != '/bye':
        if prompt != '':
            print(agent.chat(prompt))
        prompt = input("smart chat > ")
