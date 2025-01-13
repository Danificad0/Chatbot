from llama_loader import load_llama_model
from db_connector import connect_to_db, execute_query
import os
import re
import time

# Carregar modelo e banco
tokenizer, model = load_llama_model()

# Caminho absoluto para o banco de dados
db_path = os.path.join(os.path.dirname(__file__), "../data/158490.sqlite")

conn = connect_to_db(db_path)

# Lógica do chatbot
def ask_question(prompt):
    # Contexto do chatbot
    context = """
    Você é um assistente que responde a perguntas baseadas em um banco de dados.
    O banco contém informações sobre:
    - Registros do usuário (tabela `t_service`).
    - Clientes visitados (tabela `t_visitas`).

    Perguntas comuns:
    - Quantos registros o usuário possui?
    - Quantos clientes foram visitados?
    - Quais clientes foram visitados?
    """

    # Tokenizar entrada
    inputs = tokenizer(f"{context}\nUsuário: {prompt}", return_tensors="pt")

    # Mover os inputs para o dispositivo correto (GPU)
    device = model.device  # Obtém o dispositivo do modelo
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Gerar saída do modelo
    outputs = model.generate(**inputs, max_length=200)
    interpreted_question = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Decidir a ação com base na interpretação
    if "quantos registros" in interpreted_question.lower():
        query = "SELECT COUNT(*) FROM t_service;"
        result = execute_query(conn, query)
        return f"O usuário realizou {result[0][0]} registros."
    elif "quantos clientes" in interpreted_question.lower():
        query = "SELECT DISTINCT cliente_id FROM t_visitas;"
        result = execute_query(conn, query)
        return f"O usuário visitou {len(result)} clientes."
    else:
        return f"Desculpe, não consegui entender sua pergunta. Aqui está o que o modelo interpretou: {interpreted_question}"




