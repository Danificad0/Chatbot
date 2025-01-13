from chatbot import ask_question

def main():
    print("Bem-vindo ao Chatbot Checkmob!")
    while True:
        prompt = input("Digite sua pergunta (ou 'sair' para encerrar): ")
        if prompt.lower() == "sair":
            break
        response = ask_question(prompt)
        print(response)

if __name__ == "__main__":
    main()
