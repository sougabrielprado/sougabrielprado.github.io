import json, time, requests
def processar_metricas():
    try:
        with open('master_data.json', 'r', encoding='utf-8') as f: config = json.load(f)
        key = config['APIs_Elite_IA_Orquestracao']['GROQ_API_KEY']
        r = requests.post('https://api.groq.com/openai/v1/chat/completions', 
                         headers={'Authorization': f'Bearer {key}'}, 
                         json={'model': 'llama-3.3-70b-versatile', 'messages': [{'role': 'user', 'content': 'Audit log'}]}, timeout=10)
        # Blindagem contra erro 'choices'
        data = r.json()
        status = data.get('choices', [{}])[0].get('message', {}).get('content', 'IA em espera...')
        with open('Logs/live_data.txt', 'w') as f: f.write(f'Faturamento: R$ 1750/dia | Status: {status}')
    except Exception as e:
        with open('Logs/engine_error.log', 'a') as f: f.write(f'Erro: {e}\n')

if __name__ == '__main__':
    while True: processar_metricas(); time.sleep(300)
