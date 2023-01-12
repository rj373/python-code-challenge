def is_pangram(sentence):
    sentence="".join(ch for ch in sentence if ch.isalnum()).lower()
    sentence=set(sentence)
    str=set('abcdefghijklmnopqrstuvwxyz')
    if sentence >= str:
        return True
    else:
        return False
    
            
            