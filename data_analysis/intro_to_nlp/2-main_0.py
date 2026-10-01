#!/usr/bin/env python3

import pandas as pd
clean_text    = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text


# tweet vs word vs split
msg = clean_text("Don't call me!!! Visit <URL> for FREE prizes... u won :)")
print(f"input : {msg}\n")

for method in ['tweet', 'word', 'split']:
    tokens = tokenize_text(msg, method=method)
    print(f"[{method}] ({len(tokens)}) {tokens}\n")


$ ./2-main_0.py
input : don't call me! visit <URL> for free prizes... u won :)

[tweet] (13) ["don't", 'call', 'me', '!', 'visit', '<URL>', 'for', 'free', 'prizes', '...', 'u', 'won', ':)']

[word] (17) ['do', "n't", 'call', 'me', '!', 'visit', '<', 'URL', '>', 'for', 'free', 'prizes', '...', 'u', 'won', ':', ')']

[split] (11) ["don't", 'call', 'me!', 'visit', '<URL>', 'for', 'free', 'prizes...', 'u', 'won', ':)']
