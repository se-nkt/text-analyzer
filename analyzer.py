import math

MODES = {'general': 180, 'technical': 130, 'math': 50}

def get_read_time(text, mode='general'):
    words = text.split()
    return math.ceil(len(words) / MODES.get(mode, 180)) if words else 0

if __name__ == '__main__':
    print('Minutes:', get_read_time('hello world example text', 'general'))
