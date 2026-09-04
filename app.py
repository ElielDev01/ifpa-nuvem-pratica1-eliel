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