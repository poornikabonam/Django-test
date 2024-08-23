import json
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

# Load pre-trained model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Load and preprocess the dataset
def preprocess_dataset(file_path, tokenizer, block_size, subset_size):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Take only a subset of the data
    data = data[:subset_size]  # Adjust this value to limit the dataset size
    
    # Save this subset to a new file
    subset_file_path = "subset_data.json"
    with open(subset_file_path, 'w') as f:
        json.dump(data, f)
    
    return TextDataset(
        tokenizer=tokenizer,
        file_path=subset_file_path,
        block_size=block_size
    )

# Adjust the subset size here
subset_size = 1000
train_dataset = preprocess_dataset("alpaca_data.json", tokenizer, block_size=128, subset_size=subset_size)

# Data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Training arguments
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=3,  # Adjust as needed
    per_device_train_batch_size=4,  # Adjust as needed
    save_steps=10_000,
    save_total_limit=2,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Fine-tune the model
trainer.train()

# Save the model
model.save_pretrained("./gpt2-finetuned")
