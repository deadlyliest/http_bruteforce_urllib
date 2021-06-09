import requests

with open("wordlist.txt", "r") as file:
    wordlist = file.read().splitlines()

    for word in wordlist:
        data = {"user": "admin", "password": word}
        response = requests.post("", data=data)
        if "logout" in response.text:
            print("Senha {} correta!".format(word))
        else:
            print("Senha {} incorreta!".format(word))
