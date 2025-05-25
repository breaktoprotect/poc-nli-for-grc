from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from entailment_eval_dataset import (
    grc_eval_set_1,
    grc_eval_set_2,
    grc_eval_set_3,
    grc_eval_set_4,
)


def main():
    # Model #1: Pretrained cross-encoder/nli-deberta-v3-large
    original_deberta_model = "cross-encoder/nli-deberta-v3-large"

    # Model #2: Fine-tuned deberta known as finetuned_nli-deberta-v3-large
    finetuned_deberta_model = "./finetuned_nli-deberta-v3-large"

    infer(original_deberta_model, grc_eval_set_1)
    infer(finetuned_deberta_model, grc_eval_set_1)

    infer(original_deberta_model, grc_eval_set_2)
    infer(finetuned_deberta_model, grc_eval_set_2)

    infer(original_deberta_model, grc_eval_set_3)
    infer(finetuned_deberta_model, grc_eval_set_3)

    infer(original_deberta_model, grc_eval_set_4)
    infer(finetuned_deberta_model, grc_eval_set_4)


def infer(model_name: str, eval_dataset: dict) -> None:
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)

    # Extract premises (controls) and hypotheses (audit statements)
    premises = [item["control"] for item in eval_dataset["dataset"]]
    hypotheses = [item["audit_statement"] for item in eval_dataset["dataset"]]
    expected_labels = [item["expected_label"] for item in eval_dataset["dataset"]]

    # Tokenize in batch
    features = tokenizer(
        premises, hypotheses, padding=True, truncation=True, return_tensors="pt"
    )

    # Run model inference
    model.eval()
    with torch.no_grad():
        logits = model(**features).logits
        probs = F.softmax(logits, dim=1)
        label_mapping = ["contradiction", "entailment", "neutral"]
        predicted_labels = [label_mapping[idx] for idx in probs.argmax(dim=1)]

    # Display results with correctness
    print(f"[*] Model in use: {model_name}")
    print(f"[*] Evaluation set name: {eval_dataset['name']}")
    print(
        f"{'Control':<60} | {'Audit Statement':<60} | {'Predicted':<12} | {'Expected':<12} | {'Correct?':<8} | {'Conf':<6} | {'[Contradict, Entail, Neutral]'}"
    )
    print("-" * 200)

    correct_count = 0
    for item, pred, exp, conf, score_vec in zip(
        eval_dataset["dataset"],
        predicted_labels,
        expected_labels,
        probs.max(dim=1).values,
        probs,
    ):
        is_correct = pred == exp
        if is_correct:
            correct_count += 1
        scores_str = "[" + ", ".join(f"{s.item():.2f}" for s in score_vec) + "]"
        print(
            f"{item['control'][:58]:<60} | {item['audit_statement'][:58]:<60} | {pred:<12} | {exp:<12} | {str(is_correct):<8} | {conf.item():.2f} | {scores_str}"
        )

    # Show accuracy
    total = len(eval_dataset["dataset"])
    accuracy = (correct_count / total) * 100
    print(f"\nAccuracy: {correct_count} / {total} = {accuracy:.2f}%")
    print("---\n")


if __name__ == "__main__":
    main()
