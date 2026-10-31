import requests
import csv
import time

cnpjs = [
    "06990590000123", 
    "00000000000191", 
    "02449992000164"  
]

leads = []
print("Iniciando extração de dados B2B...")

for cnpj in cnpjs:
    print(f"A processar CNPJ: {cnpj}...")
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    
    try:
        # Cabeçalho adicionado para evitar bloqueio da API
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            dados = response.json()
            leads.append([
                dados.get("razao_social", "N/A"),
                dados.get("ddd_telefone_1", "N/A"),
                dados.get("email", "N/A"),
                dados.get("municipio", "N/A")
            ])
        else:
            print(f"Erro ao consultar CNPJ {cnpj} - Código: {response.status_code}")
    except Exception as e:
        print(f"Erro de conexão: {e}")
        
    time.sleep(1)

with open("leads_gerados.csv", mode="w", newline="", encoding="utf-8-sig") as ficheiro:
    writer = csv.writer(ficheiro, delimiter=";")
    writer.writerow(["Empresa", "Telefone", "Email", "Cidade"])
    writer.writerows(leads)

print("\n✓ Sucesso! O ficheiro 'leads_gerados.csv' foi atualizado.")