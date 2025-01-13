from transformers import LlamaForCausalLM, LlamaTokenizer

def load_llama_model(model_name="meta-llama/Llama-2-7b-chat-hf"):
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    model = LlamaForCausalLM.from_pretrained(model_name)
    print("Modelo e tokenizer baixados com sucesso!")
    return tokenizer, model