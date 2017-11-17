from typing import List

from nltk import ToktokTokenizer

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class SynonymReplaceTransform(AbstractTransform):
    def __init__(self, synsets: List[List[str]], tokenizer=None):
        self.tokenizer = tokenizer or ToktokTokenizer()

        list_synsets = list()
        max_word_token_list_len = 0
        for synset in synsets:
            tokenized_synset = []
            for word in synset:
                tokenized_word = self.tokenizer.tokenize(word)
                max_word_token_list_len = max(max_word_token_list_len, len(tokenized_word))
                tokenized_synset.append(tokenized_word)
            list_synsets.append(tokenized_synset)

        dict_synsets = dict()
        for synset in list_synsets:
            tag = synset[0]
            for word in synset[1:]:
                dict_synsets[tuple(word)] = tuple(tag)

        self.synsets = dict_synsets
        self.max_word_token_list_len = max_word_token_list_len

    def transform(self, sent: List[str]) -> List[str]:
        for n in range(self.max_word_token_list_len, -1, -1):
            new_sent = list()

            i = 0
            while i < len(sent):
                n_gram = tuple(sent[i:i+n])
                if len(n_gram) == 0:
                    break
                if n_gram in self.synsets:
                    new_sent.extend(self.synsets[n_gram])
                    i += n
                else:
                    new_sent.append(n_gram[0])
                    i += 1

            if len(new_sent) == 0:
                new_sent = sent
            sent = new_sent

        return sent
