# Hugging-Face-Uploader

# 🟢 Hugging Face Model Management Scripts

This guide explains how to use two scripts, `push.py` and `deletemodels.py`, to manage your Hugging Face repositories. You can use these scripts to create repositories, upload fine-tuned models, or delete repositories.

---

## Requirements

1. **Install Python**: Ensure Python is installed on your system.
2. **Install Required Libraries**:
   Run this command in your terminal:
   ```bash
   pip install huggingface_hub
   ```
3. **Set Your Hugging Face Token**:
   Replace `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` in the scripts with your own Hugging Face token. You can generate a token from [Hugging Face's token page](https://huggingface.co/settings/tokens).

---

## Scripts Overview

### 1. **`push.py`** - Create Repositories and Upload Models

This script lets you:

- Create repositories in your Hugging Face account.
- Upload fine-tuned models to the repositories.

#### ⚡️ Steps to Use:

1. **Fork This Repository**:
   Click the **Fork** button at the top-right corner of this repository to create your own copy.

2. **Prepare Your Directory**:
   - Navigate to where your models are stored.
   - Organize your models under a folder named `fine_tuned_model`.
   - Example directory structure:
     ```
     /Users/your_username/Documents/test/
       ├── EXP1/
       │   ├── finetuning-exp1numberone/fine_tuned_model/
       │   ├── finetuning-exp1numbertwo/fine_tuned_model/
       │   └── finetuning-exp1numberthree/fine_tuned_model/
     ```

3. **Run the Script**:
   Use the terminal to call the script with the folder name (e.g., `EXP1`):

   ```bash
   python push.py EXP1
   ```

4. **What Happens**:
   - Creates repositories in your Hugging Face account, named like `finetuning-exp1-numberone`.
   - Uploads all files from the `fine_tuned_model` folders to their respective repositories.

#### 🟢 Demo:
For instance, if your folder name is `EXP2`, run:

```bash
python push.py EXP2
```

This will:
- Create `raminguyen/finetuning-exp2-numberone`, `raminguyen/finetuning-exp2-numbertwo`, and `raminguyen/finetuning-exp2-numberthree` repositories.
- Upload files from:
  - `/Users/your_username/Documents/test/EXP2/finetuning-exp2numberone/fine_tuned_model`
  - `/Users/your_username/Documents/test/EXP2/finetuning-exp2numbertwo/fine_tuned_model`
  - `/Users/your_username/Documents/test/EXP2/finetuning-exp2numberthree/fine_tuned_model`

---

### 2. **`deletemodels.py`** - Delete Repositories

This script deletes repositories from your Hugging Face account. Be careful as this cannot be undone.

#### 🟢 Steps to Use:

1. **Run the Script to Delete All Repositories**:
   ```bash
   python deletemodels.py
   ```
   This will list and delete all repositories owned by your Hugging Face account.

2. **Run the Script to Delete a Specific Repository**:
   Uncomment and use the second block of code in `deletemodels.py`:
   ```python
   model_to_delete = "raminguyen/repo_name"  # Replace with your specific repo name
   print(f"Deleting: {model_to_delete}")
   api.delete_repo(repo_id=model_to_delete, token=hf_token, repo_type="model")
   print(f"Model '{model_to_delete}' deleted successfully!")
   ```

#### ✨ Demo:
To delete all models:
```bash
python deletemodels.py
```
To delete a specific model, update the code to specify the repository name and run:
```bash
python deletemodels.py
```

---

## Code Customization

### Define Your Directory
To ensure the scripts work correctly for you:
- Update the `base_path` in `push.py` to reflect your local directory where model files are stored.
- Example:
  ```python
  base_path = f"/Users/your_username/Documents/test/{folder_name}"
  ```
- Ensure your folder names match what you provide when running the script (e.g., `EXP1`, `EXP2`).

### Replacing Hugging Face Token
Update `hf_token` in both scripts with your Hugging Face token to authenticate your requests.

### Adding More Models
In `push.py`, update the `models` list to include new models:
```python
models = [
    "numberone",
    "numbertwo",
    "numberthree",
    "numberfour"  # Add more as needed
]
```

---

## 🟢 Example Workflow

1. **Fork the Repository**:
   Fork this repository to create your own copy.

2. **Define Your Directory and Token**:
   Update `base_path` in `push.py` to reflect your directory and replace `hf_token` with your Hugging Face token.

3. **Run Push Script**:
   Run the following command to create repositories and upload models:
   ```bash
   python push.py EXP1
   ```

4. **Delete All Repositories (Optional)**:
   Run this command to delete all repositories:
   ```bash
   python deletemodels.py
   ```

---
# 🔧 Hugging Face Model Management Scripts

This guide explains how to use two scripts, `push.py` and `deletemodels.py`, to manage your Hugging Face repositories. You can use these scripts to create repositories, upload fine-tuned models, or delete repositories.

---

## 🔎 Requirements

1. **Install Python**: Ensure Python is installed on your system.
2. **Install Required Libraries**:
   Run this command in your terminal:
   ```bash
   pip install huggingface_hub
   ```
3. **Set Your Hugging Face Token**:
   Replace `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` in the scripts with your own Hugging Face token. You can generate a token from [Hugging Face's token page](https://huggingface.co/settings/tokens).

---
Feel free to connect with me for any questions or assistance:

**LinkedIn**: [http://www.linkedin.com/in/rami-huu-nguyen/](http://www.linkedin.com/in/rami-huu-nguyen/) | **Email**: [rami.nguyen12@gmail.com](mailto:rami.nguyen12@gmail.com) | OR Learn More about Me **Resume**: [https://docs.google.com/document/d/17-sjbPCVa1Z0SxOfZr4kHi3VOdJCSIz9GOS6SBeSgUg/edit?usp=sharing](https://docs.google.com/document/d/17-sjbPCVa1Z0SxOfZr4kHi3VOdJCSIz9GOS6SBeSgUg/edit?usp=sharing) 



