from huggingface_hub import HfApi

hf_token = "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"

api = HfApi()

user_models = api.list_models(author="raminguyen", token=hf_token)

for model in user_models:
    model_id = model.modelId
    print(f"Deleting: {model_id}")
    api.delete_repo(repo_id=model_id, token=hf_token, repo_type="model")

print("All models deleted!")


"""
from huggingface_hub import HfApi

# Replace 'your_hf_token' with your actual token
hf_token = "your_hf_token"
api = HfApi()

# Specify the model you want to delete
model_to_delete = "raminguyen/llava-1.5-7b-hf-ft-mix-vsft"  # Replace with your model's ID

print(f"Deleting: {model_to_delete}")
api.delete_repo(repo_id=model_to_delete, token=hf_token, repo_type="model")
print(f"Model '{model_to_delete}' deleted successfully!")
"""
