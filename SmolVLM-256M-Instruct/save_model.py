from transformers import AutoModel, AutoTokenizer

model_name = "HuggingFaceTB/SmolVLM-256M-Instruct"

model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./modelo")
tokenizer.save_pretrained("./modelo")