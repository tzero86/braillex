banner = '''
                                                                                                                      
bbbbbbbb                                                                                                              
b::::::b                                                  iiii  lllllll lllllll                                       
b::::::b                                                 i::::i l:::::l l:::::l                                       
b::::::b                                                  iiii  l:::::l l:::::l                                       
 b:::::b                                                        l:::::l l:::::l                                       
 b:::::bbbbbbbbb    rrrrr   rrrrrrrrr   aaaaaaaaaaaaa   iiiiiii  l::::l  l::::l     eeeeeeeeeeee  xxxxxxx      xxxxxxx
 b::::::::::::::bb  r::::rrr:::::::::r  a::::::::::::a  i:::::i  l::::l  l::::l   ee::::::::::::ee x:::::x    x:::::x 
 b::::::::::::::::b r:::::::::::::::::r aaaaaaaaa:::::a  i::::i  l::::l  l::::l  e::::::eeeee:::::eex:::::x  x:::::x  
 b:::::bbbbb:::::::brr::::::rrrrr::::::r         a::::a  i::::i  l::::l  l::::l e::::::e     e:::::e x:::::xx:::::x   
 b:::::b    b::::::b r:::::r     r:::::r  aaaaaaa:::::a  i::::i  l::::l  l::::l e:::::::eeeee::::::e  x::::::::::x    
 b:::::b     b:::::b r:::::r     rrrrrrraa::::::::::::a  i::::i  l::::l  l::::l e:::::::::::::::::e    x::::::::x     
 b:::::b     b:::::b r:::::r           a::::aaaa::::::a  i::::i  l::::l  l::::l e::::::eeeeeeeeeee     x::::::::x     
 b:::::b     b:::::b r:::::r          a::::a    a:::::a  i::::i  l::::l  l::::l e:::::::e             x::::::::::x    
 b:::::bbbbbb::::::b r:::::r          a::::a    a:::::a i::::::il::::::ll::::::le::::::::e           x:::::xx:::::x   
 b::::::::::::::::b  r:::::r          a:::::aaaa::::::a i::::::il::::::ll::::::l e::::::::eeeeeeee  x:::::x  x:::::x  
 b:::::::::::::::b   r:::::r           a::::::::::aa:::ai::::::il::::::ll::::::l  ee:::::::::::::e x:::::x    x:::::x 
 bbbbbbbbbbbbbbbb    rrrrrrr            aaaaaaaaaa  aaaaiiiiiiiillllllllllllllll    eeeeeeeeeeeeeexxxxxxx      xxxxxxx
                                                            A super simple, text to braille converter. By @tzero86
'''


braille_alphabet = {' ': '⠀', '!': '⠮', '"': '⠐', '#': '⠼', '$': '⠫', '%': '⠩', '&': '⠯', '': '⠄', '(': '⠷', ')': '⠾',
                    '*': '⠡', '+': '⠬', ',': '⠠', '-': '⠤', '.': '⠨', '/': '⠌', '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒',
                    '4': '⠲', '5': '⠢', '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', ':': '⠱', ';': '⠰', '<': '⠣', '=': '⠿',
                    '>': '⠜', '?': '⠹', '@': '⠈', 'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛',
                    'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟',
                    'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', '[': '⠪',
                    '\\': '⠳', ']': '⠻', '^': '⠘', '_': '⠸'}

# we generate a dictionary with the reverse values, meaning braille to their corresponding character
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}


# This function receives a string of braille chars and returns the resulting text back
def braille_to_text(braille_text):
    braille_value = braille_text.lower()  # convert Braille to lowercase
    text_result = ''
    i = 0
    while i < len(braille_value):
        # Check if the next two characters form a Braille symbol
        if braille_value[i:i+2] in reverse_braille_alphabet:
            text_result += reverse_braille_alphabet[braille_value[i:i+2]]
            i += 2
        # Otherwise, treat the next character as a single-character Braille symbol
        else:
            text_result += reverse_braille_alphabet[braille_value[i]]
            i += 1
    return text_result


# This function takes the text and returns the resulting braille sequence of characters
def text_to_braille(text):
    result = ''
    for char in text.lower():
        result += braille_alphabet[char]
    return result


# we print the banner when the script starts.
print(banner)


try:
    # We listen for user input until the word exit is
    while True:  # loop indefinitely
        # Prompt the user for input
        user_text = input('[!] Enter some text to convert to Braille (Press Ctrl+C to quit): ')
        braille = text_to_braille(user_text)  # convert text to Braille
        user_text = braille_to_text(braille)  # convert Braille back to text
        print(f'    [Original Text]: {user_text}')
        print(f'    [Braille Translation]: {braille}')

except KeyboardInterrupt:  # handle the KeyboardInterrupt exception
    print('\n[*] Exiting Braillex Script.')

