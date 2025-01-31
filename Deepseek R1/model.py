from transformers import AutoModel, AutoTokenizer

model_name = "deepseek-ai/DeepSeek-R1"

model = AutoModel.from_pretrained(model_name, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

model.save_pretrained("./modelo")
tokenizer.save_pretrained("./modelo")

