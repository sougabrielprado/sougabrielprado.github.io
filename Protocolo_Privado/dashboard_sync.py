import json, requests, time
def sync_secure():
    try:
        with open('master_data.json', 'r', encoding='utf-8') as f: config = json.load(f)
        key = config['APIs_Elite_IA_Orquestracao']['GROQ_API_KEY']
        r = requests.post('https://api.groq.com/openai/v1/chat/completions', 
                         headers={'Authorization': f'Bearer {key}'}, 
                         json={'model': 'llama-3.3-70b-versatile', 'messages': [{'role': 'user', 'content': 'Report Status'}]}, timeout=15)
        res = r.json()
        # Tratamento do erro visto na imagem
        ia_msg = res.get('choices', [{}])[0].get('message', {}).get('content', 'Sincronizando Nexus...')
        print(ia_msg)
    except Exception as e: print(f'Erro de Pulso: {e}')

if __name__ == '__main__':
    while True: sync_secure(); time.sleep(300)
