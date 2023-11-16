from transformers import GPT2Tokenizer, AutoModelForCausalLM

def get_model(args):
    tokenizer = GPT2Tokenizer.from_pretrained(args.model_name_or_path)
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model = AutoModelForCausalLM.from_pretrained(args.model_name_or_path)
    print(f'model {args.model_name_or_path} loaded')

    return model,tokenizer
