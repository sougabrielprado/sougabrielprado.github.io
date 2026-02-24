import json, requests, time, os
def sync_dashboard():
    try:
        with open('master_data.json', 'r', encoding='utf-8') as f: config = json.load(f)
        key = config['APIs_Elite_IA_Orquestracao']['GROQ_API_KEY']
        # Resiliência: Verificação de segurança antes de acessar 'choices'
        r = requests.post('https://api.groq.com/openai/v1/chat/completions', 
                         headers={'Authorization': f'Bearer {key}'}, 
                         json={'model': 'llama-3.3-70b-versatile', 'messages': [{'role': 'user', 'content': 'Resumo C-Level'}]}, timeout=15)
        res = r.json()
        ia_msg = res.get('choices', [{}])[0].get('message', {}).get('content', 'Nexus em Processamento...')
        
        # Gera o HTML purificado
        html = f"<html><body style='background:#001f3f;color:#FFD700;font-family:sans-serif;'><h1># Status do Império</h1><p>{ia_msg}</p></body></html>"
        with open('5_Interface_CLevel/dashboard.html', 'w', encoding='utf-8') as f: f.write(html)
    except Exception as e:
        with open('Logs/sync_error.log', 'a') as f: f.write(f'[{time.ctime()}] {e}\n')

if __name__ == '__main__':
    while True:
        sync_dashboard()
        time.sleep(300)
