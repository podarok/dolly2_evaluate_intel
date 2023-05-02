import torch
from instruct_pipeline import InstructionTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-12b", padding_side="left")
torch.set_num_interop_threads(56)
torch.set_num_threads(56)
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-12b", device_map="cpu", torch_dtype=torch.bfloat16)

generate_text = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)

res = generate_text("Tell me why Ukraine is winning a war with Russia")
print(res[0]["generated_text"])
