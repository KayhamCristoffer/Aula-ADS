import requests

def main():
    print("Cliente de API - Arquitetura Distribuída (FastAPI)")
    while True:
        text = input("Digite um texto (ou 'sair'): ")
        if text.lower() == "sair":
            break

        try:
            response = requests.post(
                "http://localhost:5001/process",
                json={"text": text},
                timeout=5
            )
            if response.status_code == 200:
                print("Resposta:", response.json())
            else:
                print(f"Erro {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            print("Erro de conexão com o servidor:", e)

if __name__ == "__main__":
    main()

#execução 
#python B.py --- servidor
#python A.py --- cliente
#http://localhost:5001/docs