from flask import Flask, jsonify, request
import os
import datetime

app = Flask(__name__)

# Banco de dados simulado em memória (Segregação lógica Multitenant)
pedidos_armazenados = []

@app.route('/', methods=['GET'])
def healthcheck():
    return jsonify({
        "status": "Online",
        "timestamp": datetime.datetime.now().isoformat(),
        "ambiente": "Container Linux (Docker)",
        "disciplina": "Computacao em Nuvem e SOA - IFPA",
        "api_endpoint": "/predict [POST]"
}), 200

# =====================================================================
# SELEÇÃO DA TRILHA DE CÓDIGO (Escolha e use APENAS UMA das duas abaixo)
# =====================================================================

# --- TRILHA INTEGRADA (Alunos de Tópicos Avançados I) ---
# Se você cursa as duas disciplinas, utilize esta lógica:
@app.route('/predict', methods=['POST'])
def predict_mock_ia():
    data = request.get_json() or {}
    user_prompt = data.get("prompt")
    tenant_id = data.get("tenant_id", "default_tenant")

    if not user_prompt:
        return jsonify({"erro": "Bad Request", "mensagem": "Prompt ausente"}), 400

    # Mock Simulado: Na sexta-feira você integrará o seu Agente RAG Real aqui!
    resposta_simulada = f"[AGENTE IA MOCK] Processando busca semantica para o prompt: '{user_prompt}'"

    nova_transacao = {
        "id": len(pedidos_armazenados) + 1,
        "tenant_id": tenant_id,
        "prompt": user_prompt,
        "resposta_agente": resposta_simulada,
        "status_execucao": "Sucesso",
        "data_registro": datetime.datetime.now().isoformat()
    }
    pedidos_armazenados.append(nova_transacao)

    return jsonify({
    "sucesso": True,
    "trilha": "Integrada - Inteligencia Artificial",
    "dados": nova_transacao
    }), 201

# --- TRILHA PADRÃO (Alunos apenas de Computaçao em Nuvem) ---
# Se você cursa APENAS a disciplina de Nuvem, apague o bloco da Trilha Integrada e use este:

@app.route('/predict', methods=['POST'])
def calcular_frete_elastico():
    data = request.get_json() or {}
    distancia = data.get("distancia_km")
    peso = data.get("peso_kg")
    tenant_id = data.get("tenant_id", "default_tenant")

    if distancia is None or peso is None:
        return jsonify({"erro": "Bad Request", "mensagem": "Campos obrigatorios ausentes"}), 400

    try:
        custo_base = 15.0
        custo_distancia = float(distancia) * 1.5
        custo_peso = float(peso) * 0.8
        valor_total = custo_base + custo_distancia + custo_peso

        nova_transacao = {
            "id": len(pedidos_armazenados) + 1,
            "tenant_id": tenant_id,
            "distancia_km": distancia,
            "peso_kg": peso,
            "valor_calculado": round(valor_total, 2),
            "data_registro": datetime.datetime.now().isoformat()
        }
        pedidos_armazenados.append(nova_transacao)

        return jsonify({
            "sucesso": True,
            "trilha": "Padrao - Computacao em Nuvem",
            "dados": nova_transacao
            }), 201
    except ValueError:
        return jsonify({"erro": "Valores numericos invalidos"}), 422

# =====================================================================

if __name__ == '__main__':
# O Gunicorn usarÃ¡ a porta 5000 do container
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)