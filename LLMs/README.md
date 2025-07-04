# Fine-Tuning Mistral-7B with PEFT and QLoRA 🚀

Ce projet montre comment fine-tuner le modèle **Mistral-7B-Instruct** en utilisant la méthode **QLoRA** (Quantized LoRA) et la bibliothèque **PEFT (Parameter-Efficient Fine-Tuning)**. Il utilise le dataset `iamtarun/python_code_instructions_18k_alpaca` et le framework `transformers` de Hugging Face avec `trl`.

---


## 🧩 Technologies utilisées

- `transformers`
- `datasets`
- `peft`
- `trl` (pour `SFTTrainer`)
- `bitsandbytes` (quantization)
- `accelerate` (multi-GPU support)

---

## ⚙️ Installation des dépendances

```bash
pip install --upgrade peft accelerate bitsandbytes datasets trl
