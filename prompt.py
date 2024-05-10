import pandas as pd
import numpy as np

from ciphers import caesar, permute_words

def build_prompt(
    encryptions: list[str],
    data: pd.DataFrame,
    examples: int,
    encryption_kwargs: list[dict],
    test_with_dataset = True, # try random strings for output because LLM may be cheating with knowledge of the training corpus
) -> str:
    permuted: np.ndarray = np.random.permutation(len(data))[:examples + 1]
    train: pd.DataFrame = data[permuted[:len(permuted) - 1]].tolist()
    train_enc = train.copy()
    test: pd.DataFrame = data[permuted[-1].item()]
    test_enc = test
    for i, enc in enumerate(encryptions):
        if enc == 'caesar':
            train_enc = [caesar(sample, **encryption_kwargs[i]) for sample in train_enc]
            test_enc = caesar(test_enc, **encryption_kwargs[i])
        elif enc == 'permute':
            train_enc = [permute_words(sample) for sample in train_enc]
            test_enc = permute_words(test_enc)
    
    prompt: str = "The following are examples of encrypted and decrypted ciphertext using a scheme that I want you to replicate.\n\n"
    for i in range(len(train_enc)):
        prompt += f"Encrypted: {train_enc[i]}\n"
        prompt += f"Decrypted: {train[i]}\n"
    prompt += "\nNow that you've seen some examples of the scheme, decrypt this prompt with the same scheme.\n\n"
    prompt += f"Encrypted: {test_enc}\n"
    prompt += "\nPrint out your answer and nothing else. Do not print out the word Decrypted."
    return prompt, test