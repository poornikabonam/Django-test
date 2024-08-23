from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from transformers import TextDataset, DataCollatorForLanguageModeling

class LLMModel:

    def generate_text(self, question):
        print('question---------------------------------------------',question)
        model_name = "gpt2"
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)

        # Load the fine-tuned model
        model = GPT2LMHeadModel.from_pretrained("gpt2-finetuned",local_files_only=True)

        # Tokenize input text
        input_ids = tokenizer.encode(question, return_tensors="pt")

        # Generate text
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

        # Decode and print generated texta
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text

