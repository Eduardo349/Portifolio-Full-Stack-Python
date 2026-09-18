import os
from openai import OpenAI

# Puxa a chave das variáveis de ambiente em produção ou deixa vazio para o teste local
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "chave_simulada_local")

def gerar_relatorio_com_ia(dados_brutos: str) -> str:
    # Se você colocar uma chave real, o código executa a chamada real na nuvem
    if OPENAI_API_KEY != "chave_simulada_local":
        try:
            client = OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Modelo moderno, rápido e econômico
                messages=[
                    {"role": "system", "content": "Você é um analista de negócios sênior. Receba os dados do usuário e gere um relatório corporativo focado em insights, pontos fortes e melhorias."},
                    {"role": "user", "content": dados_brutos}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao conectar com o servidor da OpenAI: {str(e)}"
            
    # MODO SIMULADO LOCAL: Cria uma resposta estruturada de IA excelente para testar o portfólio de graça
    return f"""
    ### 📊 RELATÓRIO ANALÍTICO CORPORATIVO (Gerado por IA)
    
    **1. Análise dos Dados Recebidos:**
    O sistema processou os seguintes insumos comerciais: "{dados_brutos}".
    
    **2. Insights Estratégicos Identificados:**
    *   **Ponto de Otimização:** Padrões indicam gargalos operacionais na distribuição de recursos descritos.
    *   **Oportunidade Comercial:** Demanda reprimida latente identificável através do volume informado.
    
    **3. Plano de Ação Recomendado:**
    *   Implementar validação assíncrona em etapas críticas do processo.
    *   Monitorar métricas de conversão nas próximas 72 horas corporativas.
    """
