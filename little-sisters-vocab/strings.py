"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un"+word
    
def make_word_groups(vocab_words):
    pre = vocab_words[0]
    return pre + " :: " + " :: ".join([pre + i for i in vocab_words[1:]])
    
def remove_suffix_ness(word):
    if word[-5]=='i':
        return word[:-4].replace('i','y')
    else:
        return word[:-4]
        
def adjective_to_verb(sentence, index):
    return sentence.split()[index].replace(".","")+"en"