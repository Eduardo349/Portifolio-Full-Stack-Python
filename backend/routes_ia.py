from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlmodel import Session, select
from .database import get_session
from .models import Relatorio, Usuario
from .service_ia import gerar_relatorio_com_ia
from .auth import obter_usuario_atual  # 1. Importa o validador de segurança
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

router = APIRouter(prefix="/api/ia", tags=["Inteligência Artificial"])

# --- ROTA ATUALIZADA E PROTEGIDA ---
@router.post("/gerar", status_code=status.HTTP_201_CREATED)
def criar_novo_relatorio(
    dados: dict, 
    db: Session = Depends(get_session),
    usuario_atual: Usuario = Depends(obter_usuario_atual) # 2. Exige o Token JWT ativo
):
    titulo = dados.get("titulo")
    dados_entrada = dados.get("dados_entrada")
    
    if not titulo or not dados_entrada:
        raise HTTPException(status_code=400, detail="Campos obrigatórios ausentes.")
        
    insight_gerado = gerar_relatorio_com_ia(dados_entrada)
    
    # Usa o ID extraído do Token de forma 100% segura
    novo_relatorio = Relatorio(
        titulo=titulo,
        dados_entrada=dados_entrada,
        insight_ia=insight_gerado,
        usuario_id=usuario_atual.id 
    )
    
    db.add(novo_relatorio)
    db.commit()
    db.refresh(novo_relatorio)
    
    return {
        "mensagem": "Relatório gerado com segurança corporativa JWT!",
        "relatorio": novo_relatorio
    }

# --- NOVA ROTA: GERADOR DE PDF PROFISSIONAL ---
@router.get("/pdf/{relatorio_id}")
def baixar_pdf_relatorio(relatorio_id: int, db: Session = Depends(get_session)):
    # Busca o relatório específico salvo no banco de dados
    relatorio = db.exec(select(Relatorio).where(Relatorio.id == relatorio_id)).first()
    if not relatorio:
        raise HTTPException(status_code=404, detail="Relatório não encontrado.")
        
    # Cria um fluxo de memória para segurar o arquivo antes do download
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    # Configuração de estilos do PDF corporativo
    styles = getSampleStyleSheet()
    style_titulo = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=22, textColor='#f59e0b', spaceAfter=15)
    style_sub = ParagraphStyle('SubStyle', parent=styles['Heading3'], fontSize=12, textColor='#4b5563', spaceAfter=20)
    style_corpo = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontSize=11, leading=16, spaceAfter=10)
    
    # Montando a estrutura do documento
    story.append(Paragraph(f"<b>{relatorio.titulo}</b>", style_titulo))
    story.append(Paragraph(f"Data de Emissão: {relatorio.criado_em} | ID: #{relatorio.id}", style_sub))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("<b>1. Dados Brutos Fornecidos:</b>", styles['Heading2']))
    story.append(Paragraph(relatorio.dados_entrada, style_corpo))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<b>2. Análise e Insights de Inteligência Artificial:</b>", styles['Heading2']))
    
    # Divide o texto por quebras de linha para o PDF interpretar corretamente os parágrafos
    linhas_insight = relatorio.insight_ia.split("\n")
    for linha in linhas_insight:
        if linha.strip():
            story.append(Paragraph(linha, style_corpo))
            
    doc.build(story)
    buffer.seek(0)
    
    # Entrega o arquivo PDF limpo direto para o navegador iniciar o download
    return StreamingResponse(buffer, media_type="application/pdf", headers={
        "Content-Disposition": f"attachment; filename=Relatorio_IA_{relatorio_id}.pdf"
    })
