print ("""
  /\    /\          __ __  |    |     ___
 /  \  /  \  |   | |  |  | |__  |    |___
/    \/    \ |___| |  |  | |__| |___ |___

Version 1.1.0
------------
""")

def askcommand():
    global input_str
    input_str = input("Enter command - ")

    if input_str.startswith("newscript "):
        text = newscript(input_str)
        global scriptname
        scriptname = text
        global is_in_script
        is_in_script = True
        print(" New script named " + text + " created")
        f = open(scriptname +".mumble", "w")

    if input_str.startswith("runscript "):
        text = runscript(input_str)
        f = open(text + ".mumble", "r")
        print(f.readline())
        for i in range(999999):
            global code_to_run
            code_to_run = f.readline()
            if code_to_run[12:16] == "say ":
                print(code_to_run[16:])
            if code_to_run[12:16] == "ask ":
                global ask_input_2
                ask_input_2 = input(code_to_run[16:])
            if "repeat answer" in code_to_run:
                print(ask_input_2)
                

    if input_str.startswith("say "):
        text = say(input_str)
        print(text)
        if is_in_script == True:
            f = open(scriptname +".mumble", "a")
            f.write("""
            say """ + text)
            f.close()

    if input_str.startswith("ask "):
        text = ask(input_str)
        global ask_input
        ask_input = input(text)
        if is_in_script == True:
            f = open(scriptname +".mumble", "a")
            f.write("""
            ask """ + text)
            f.close()

    if input_str == "repeat answer":
        print(ask_input)
        if is_in_script == True:
            f = open(scriptname +".mumble", "a")
            f.write("""
            repeat answer""")
            f.close()





def say(text):
    return text.split("say ")[1]

def ask(text):
    return text.split("ask ")[1]

def newscript(text):
    return text.split("newscript ")[1]

def runscript(text):
    return text.split("runscript ")[1]

def scriptlen(text):
    return text.split("scriptlength ")[1]


while True:
    askcommand()

