from src.chatbot import ask_question

def test_ask_question():
    prompt = "Quantos registros o usuário 158490 fez?"
    response = ask_question(prompt)
    assert "O usuário 158490 realizou" in response
