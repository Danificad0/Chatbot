from transformers import LlamaForCausalLM, LlamaTokenizer

# Nome do modelo
model_name = "meta-llama/Llama-2-7b-chat-hf"

# Baixar o modelo e o tokenizer
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

print("Modelo e tokenizer baixados com sucesso!")
