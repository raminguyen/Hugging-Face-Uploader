from huggingface_hub import HfApi
import os
import sys

# Hugging Face token
hf_token = "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"
api = HfApi()

# Function to make repositories
def make_repos(folder_name):
    namespace = "raminguyen"

    models = [
        f"numberone",
        f"numbertwo",
        f"numberthree",
    ]

    for model in models:
        repo_name = f"finetuning-{folder_name.lower()}-{model}"
        print(f"Making repo: {namespace}/{repo_name}")
        api.create_repo(repo_id=f"{namespace}/{repo_name}", token=hf_token, repo_type="model", exist_ok=True)
        print(f"Done: {namespace}/{repo_name}")

# Function to upload files
def upload_files(folder_name):
    base_path = f"/Users/ramivy/Documents/test/{folder_name}"
    repos = {
        f"raminguyen/finetuning-{folder_name.lower()}-numberone": os.path.join(base_path, f"finetuning-{folder_name.lower()}numberone/fine_tuned_model"),
        f"raminguyen/finetuning-{folder_name.lower()}-numbertwo": os.path.join(base_path, f"finetuning-{folder_name.lower()}numbertwo/fine_tuned_model"),
        f"raminguyen/finetuning-{folder_name.lower()}-numberthree": os.path.join(base_path, f"finetuning-{folder_name.lower()}numberthree/fine_tuned_model"),
    }

    for repo, path in repos.items():
        print(f"Uploading from {path} to {repo}")

        # Check if the folder exists
        if not os.path.exists(path):
            print(f"Path {path} does not exist. Skipping...")
            continue

        # Upload files
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, path)  # Keep folder structure
                try:
                    api.upload_file(
                        path_or_fileobj=file_path,
                        path_in_repo=relative_path,
                        repo_id=repo,
                        token=hf_token,
                    )
                    print(f"Uploaded {relative_path} to {repo}")
                except Exception as e:
                    print(f"Error uploading {file_path} to {repo}: {e}")

# Main code
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a folder name as an argument.")
        sys.exit(1)

    folder_name = sys.argv[1]
    print(f"Working with folder: {folder_name}")
    make_repos(folder_name)
    upload_files(folder_name)
