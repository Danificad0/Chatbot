from transformers import LlamaTokenizer, LlamaForCausalLM
import torch
import os

def load_llama_model(model_name="meta-llama/Llama-2-7b-chat-hf"):
    # Configuração para evitar fragmentação de memória no CUDA
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    
    # Carregar tokenizer
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    
    # Carregar o modelo com suporte ao Accelerate (device_map="auto")
    print("Carregando modelo...")
    model = LlamaForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,  # Usa meia precisão para otimizar memória
        device_map="auto",         # Accelerate gerencia dispositivos automaticamente
    )

    print("Modelo e tokenizer baixados com sucesso!")
    return tokenizer, model
