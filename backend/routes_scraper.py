from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select, func
from .database import get_session
from .models import DadoColetado
from typing import List
import random

router = APIRouter(prefix="/api/analytics", tags=["Web Scraper & Analytics"])

# 1. Rota que simula o Web Scraper rodando em tempo real
@router.post("/rodar-scraper", status_code=status.HTTP_201_CREATED)
def executar_web_scraper(db: Session = Depends(get_session)):
    # Simulando dados reais que seriam raspados do mercado de Hardware/Tech hoje
    itens_mercado = [
        {"nome": "Placa de Vídeo RTX 4060", "base": 2100},
        {"nome": "Processador Ryzen 5 5600", "base": 850},
        {"nome": "Memória RAM 16GB DDR4", "base": 290},
        {"nome": "SSD NVMe 1TB", "base": 420}
    ]
    
    novos_dados = []
    for item in itens_mercado:
        # Adiciona uma variação aleatória para simular a flutuação real do mercado
        preco_oscilado = item["base"] + random.randint(-50, 120)
        
        dado = DadoColetado(
            categoria="Hardware",
            nome_item=item["nome"],
            valor_identificado=float(preco_oscilado),
            fonte_origem="TechShop Scraper"
        )
        db.add(dado)
        novos_dados.append(dado)
        
    db.commit()
    return {"mensagem": "Web Scraper executado! 4 novos registros inseridos no banco.", "dados": novos_dados}

# 2. Rota que puxa os dados e gera estatísticas analíticas
@router.get("/metricas")
def puxar_metricas_dashboard(db: Session = Depends(get_session)):
    dados = db.exec(select(DadoColetado).order_by(DadoColetado.coletado_em.desc()).limit(10)).all()
    
    # Calcula a média de preços gravada no banco para exibir no painel
    total_itens = db.exec(select(func.count(DadoColetado.id))).one()
    
    return {
        "total_registros_banco": total_itens,
        "historico_recente": list(dados)
    }
