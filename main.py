import pyttsx3
import keyboard
import threading

lock = threading.Lock()

CAA = {
    '1': 'Preciso de ajuda',
    '3': 'Estou com dor',
    '5': 'Estou assustado',
    '7': 'Estou passando mal',
    's': 'Estou com sede',
    'f': 'Estou com fome',
    'h': 'Quero ir ao banheiro',
    'a': 'Quero descansar',
    '9': 'Estou feliz',
    '-': 'Estou triste',
    '=': 'Estou ansioso',
    'v': 'Olá',
    'x': 'Sim',
    '\\': 'Não',
    'm': 'Obrigado',
    'b': 'Você pode repetir por favor?',
    'ç': 'Quero brincar',
    '/': 'Quero assistir',
    '.': 'Quero ir para casa',
    ']': 'Quero meu objeto',
    'k': 'Quero silêncio',
    '0': 'Muito obrigado pela atenção de todos, tenham uma boa noite!'
}

def falar_texto(texto):
    def run():
        if lock.locked():
            return
            
        with lock:
            engine = pyttsx3.init()
            engine.setProperty('rate', 200)
            engine.say(texto)
            engine.runAndWait()
            engine.stop()
            del engine
    
    threading.Thread(target=run, daemon=True).start()

for tecla, frase in CAA.items():
    keyboard.add_hotkey(tecla, falar_texto, args=(frase,))

keyboard.wait('esc')
