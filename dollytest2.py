import torch
import os
from instruct_pipeline import InstructionTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

os.environ["CUDA_VISIBLE_DEVICES"]=""

tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b", padding_side="left")
torch.set_num_interop_threads(27)
torch.set_num_threads(27)
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b", device_map="balanced", torch_dtype=torch.bfloat16)

generate_text = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)

res = generate_text("Describe in 200 words what is Drupal?")
print(res[0]["generated_text"])
print(res)
