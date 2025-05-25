from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    set_seed,
)
from transformers import set_seed
from torch.utils.data import Dataset
import torch
from sklearn.model_selection import train_test_split

from entailment_training_dataset import grc_training_data

# Seed
set_seed(42)

# Label mapping
label2id = {"contradiction": 0, "entailment": 1, "neutral": 2}
id2label = {v: k for k, v in label2id.items()}


# Prepare dataset
class GRCDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        encoded = self.tokenizer(
            item["control"],
            item["audit_statement"],
            truncation=True,
            padding="max_length",
            max_length=128,
            return_tensors="pt",
        )
        return {
            "input_ids": encoded["input_ids"].squeeze(),
            "attention_mask": encoded["attention_mask"].squeeze(),
            "labels": torch.tensor(label2id[item["expected_label"]], dtype=torch.long),
        }


# Load tokenizer and model
model_id = "cross-encoder/nli-deberta-v3-large"
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_id, num_labels=3)

# Dataset


# Split dataset into 90% train, 10% validation
train_data, val_data = train_test_split(
    grc_training_data, test_size=0.1, random_state=42
)
train_dataset = GRCDataset(train_data, tokenizer)
eval_dataset = GRCDataset(val_data, tokenizer)

# Training args
training_args = TrainingArguments(
    output_dir="./finetuned_nli-deberta-v3-large",
    fp16=True,
    per_device_train_batch_size=8,
    num_train_epochs=10,
    learning_rate=2e-5,
    logging_dir="./logs",
    logging_steps=1,
    save_strategy="no",
    disable_tqdm=False,
    # evaluation_strategy="epoch",
    save_total_limit=1,
    # load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
)


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = logits.argmax(axis=1)
    accuracy = (preds == labels).astype(float).mean().item()
    return {"accuracy": accuracy}


# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

# Show training device info
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(
    f"Training using device: {device} -",
    torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU",
)


# Train
trainer.train()

# Save model
model.save_pretrained("./finetuned_nli-deberta-v3-large")
tokenizer.save_pretrained("./finetuned_nli-deberta-v3-large")
