import pandas as pd
import numpy as np
import random
import string

from ciphers import caesar

def remove_punc(inp: str) -> str:
    """
    Removes all characters from the input string that are not spaces or ascii letters.

    Parameters:
        inp:    The string to be sanitized of punctuation

    Returns:
        The input string sanitized to have only ascii letters and spaces.
    """
    return ''.join([
        c for c in inp
        if c == ' ' or c in string.ascii_letters
    ])

def erase_letters(inp: str, p: float = 0.1) -> str:
    """
    Randomly erases non-space letters from the input string with a given probability.

    Parameters:
        inp:    The input string to be perturbed
        p:      The probability to remove any individual characters
    
    Returns:
        The string with random letters erased.
    """
    rng: np.ndarray = np.random.uniform(size=(len(inp)))
    return ''.join([c for i, c in enumerate(inp) if c == ' ' or rng[i] > p])

def gen_random_words(n: int = 10) -> str:
    """
    Generates n words composed of random characters.

    Parameters:
        n:  The number of words to be generated
    
    Returns:
        A sentence with n random words.
    """
    words: list[str] = []
    for _ in range(n):
        k = random.randint(3, 7)
        words.append(''.join(random.choices(string.ascii_letters, k=k)))
    return ' '.join(words)

def build_prompt(
    encryptions: list[str],
    data: pd.DataFrame,
    examples: int,
    encryption_kwargs: list[dict],
    test_with_dataset: bool = True,
    perturb_prob: int = 0,
    train_augment: bool = True,
) -> str:
    """
    Builds a prompt based on the provided encryptions, dataset, and setting commands.

    Parameters:
        encryptions:        List of encryption strategies to be used on the input in order
        data:               The dataset from which to retrieve the train and test examples
        examples:           The number of examples to use for training
        encryption_kwargs:  Arguments to the encryption algorithms, indexed the
                            same as encryptions
        test_with_dataset:  Whether or not to operate on the dataset or just on words
                            made from random letters
        perturb_prob:       The perturbation probability for individual non-space
                            characters in the string
        train_augment:      Whether or not to augment the train data in the same way
                            as the test data
    
    Returns:
        The prompt to be passed for the LLM.
    """
    permuted: np.ndarray = np.random.permutation(len(data))[:examples + 1]
    train: list[str] = data[permuted[:len(permuted) - 1]].tolist()
    train = [remove_punc(s) for s in train]
    n_words: int = 10
    if train_augment:
        if perturb_prob != 0:
            train = [erase_letters(s, p=perturb_prob) for s in train]
        if not test_with_dataset:
            train = [gen_random_words(n_words) for _ in range(examples)]
    train_enc = train.copy()
    if test_with_dataset:
        test: str = data[permuted[-1].item()]
        if perturb_prob != 0:
            test = erase_letters(test, p=perturb_prob)
        test = remove_punc(test)
    else:
        test = gen_random_words(n_words)
    test_enc = test
    for i, enc in enumerate(encryptions):
        if enc == 'caesar':
            train_enc = [caesar(sample, **encryption_kwargs[i]) for sample in train_enc]
            test_enc = caesar(test_enc, **encryption_kwargs[i])

    prompt: str = "The following are examples of encrypted and decrypted ciphertext using a scheme that I want you to replicate.\n\n"
    for i in range(len(train_enc)):
        prompt += f"Encrypted: {train_enc[i]}\n"
        prompt += f"Decrypted: {train[i]}\n"
    prompt += "\nNow that you've seen some examples of the scheme, decrypt this prompt with the same scheme.\n\n"
    prompt += f"Encrypted: {test_enc}\n"
    prompt += "\nPrint out your answer and nothing else. Do not print out the word Decrypted."
    return prompt, test