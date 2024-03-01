def separate_elements(input_string):

    reserved_words = ['automata', 'alfabeto', 'aceptacion']

    split_chars = "{:;,}"


    tokens = []
    current_token = ""
    for char in input_string:
        if char in split_chars or char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if char in split_chars:
                tokens.append(char)
        else:
            current_token += char

    
    if current_token:
        tokens.append(current_token)

    
    final_tokens = []
    for token in tokens:
        if token in reserved_words:
            final_tokens.append(token)
        else:
            buffer = ""
            for char in token:
                if char.isdigit() or char in split_chars:
                    if buffer:
                        final_tokens.append(buffer)
                        buffer = ""
                    final_tokens.append(char)
                else:
                    buffer += char
            if buffer:
                final_tokens.append(buffer)

    return final_tokens