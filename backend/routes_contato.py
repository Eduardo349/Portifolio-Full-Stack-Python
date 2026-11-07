from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlmodel import Session, SQLModel, Field
from .database import get_session
import os

# Importações do ReportLab para o Currículo Padrão EBAC
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

router = APIRouter(prefix="/api/contato", tags=["Módulo de Contato & CV"])

class MensagemContato(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    email: str
    mensagem: str

@router.post("/enviar", status_code=status.HTTP_201_CREATED)
def receber_mensagem(dados: dict, db: Session = Depends(get_session)):
    nome = dados.get("nome")
    email = dados.get("email")
    mensagem = dados.get("mensagem")
    
    if not nome or not email or not mensagem:
        raise HTTPException(status_code=400, detail="Campos obrigatórios ausentes.")
        
    # Salva no Banco de Dados de forma limpa e profissional
    nova_msg = MensagemContato(nome=str(nome), email=str(email), mensagem=str(mensagem))
    db.add(nova_msg)
    db.commit()
    
    return {"status": "sucesso", "mensagem": "Mensagem armazenada com sucesso no banco relacional!"}

@router.get("/download-cv")
def baixar_cv_profissional():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_js = os.path.join(BASE_DIR, "frontend", "js")
    arquivo_pdf = os.path.join(pasta_js, "Curriculo_Python.pdf")
    
    os.makedirs(pasta_js, exist_ok=True)
    
    # Documento PDF estruturado de acordo com o checklist de empregabilidade da EBAC
    doc = SimpleDocTemplate(
        arquivo_pdf, 
        pagesize=letter, 
        rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45
    )
    story = []
    
    styles = getSampleStyleSheet()
    style_nome = ParagraphStyle('CVNome', parent=styles['Heading1'], fontSize=22, leading=26, textColor='#111827', alignment=1, spaceAfter=4)
    style_dados = ParagraphStyle('CVDados', parent=styles['Normal'], fontSize=9.5, leading=14, textColor='#4b5563', alignment=1, spaceAfter=15)
    style_secao = ParagraphStyle('CVSecao', parent=styles['Heading2'], fontSize=13, leading=17, textColor='#1f2937', spaceBefore=12, spaceAfter=4)
    style_corpo = ParagraphStyle('CVCorpo', parent=styles['Normal'], fontSize=10, leading=14.5, textColor='#374151', spaceAfter=5)
    style_item = ParagraphStyle('CVItem', parent=styles['Normal'], fontSize=9.5, leading=13.5, textColor='#4b5563', leftIndent=15, spaceAfter=3)

    # Dados de Jonas Eduardo extraídos dos certificados e contatos reais fornecidos
    story.append(Paragraph("<b>JONAS EDUARDO FONTELA MACHADO</b>", style_nome))
    story.append(Paragraph("Estância Velha, RS, Brazil | +55 (51) 99423-8039 | jonaseduardo879@gmail.com | LinkedIn: //linkedin.com/in/jonas-eduardo-3780412b6 | GitHub: ://github.com/Eduardo349", style_dados))
    
    story.append(Paragraph("<b>OBJETIVO</b>", style_secao))
    story.append(HRFlowable(width="100%", thickness=1, color="#d1d5db", spaceAfter=6))
    story.append(Paragraph("Desenvolvedor Full Stack Python Júnior", style_corpo))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>RESUMO DE QUALIFICAÇÕES</b>", style_secao))
    story.append(HRFlowable(width="100%", thickness=1, color="#d1d5db", spaceAfter=6))
    story.append(Paragraph("• Desenvolvedor Full Stack Python Júnior graduado com sólida experiência prática em modelagem de dados, arquiteturas corporativas e automação de processos.", style_corpo))
    story.append(Paragraph("• Especialista na construção de ecossistemas web e APIs síncronas e assíncronas utilizando <b>FastAPI</b> e <b>Django</b>, com persistência relacional via <b>PostgreSQL</b> e <b>SQLite</b>.", style_corpo))
    story.append(Paragraph("• Vivência no desenvolvimento de interfaces front-end dinâmicas e responsivas em conformidade com o ecossistema moderno usando <b>JavaScript (ES6+)</b> e o framework utilitário <b>Tailwind CSS</b>.", style_corpo))
    story.append(Paragraph("• Domínio completo de versionamento profissional com <b>Git/GitHub</b>, gerência de dependências operacionais e empacotamento isolado via containers <b>Docker</b>.", style_corpo))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>COMPETÊNCIAS TÉCNICAS</b>", style_secao))
    story.append(HRFlowable(width="100%", thickness=1, color="#d1d5db", spaceAfter=6))
    story.append(Paragraph("<b>• Back-End:</b> Python, FastAPI, Django, Django Rest Framework (DRF), Programação Assíncrona (Asyncio/HTTPX).", style_corpo))
    story.append(Paragraph("<b>• Front-End:</b> HTML5, CSS3, JavaScript (ES6+), TypeScript, React, Tailwind CSS, Bootstrap.", style_corpo))
    story.append(Paragraph("<b>• Bancos de Dados & Ferramentas:</b> PostgreSQL, SQLite, SQL (DDL/DML), SQLModel ORM, Mapeamento Relacional.", style_corpo))
    story.append(Paragraph("<b>• DevOps & Automação:</b> Docker, Docker Compose, Linux CLI, Web Scraping Automation, Uvicorn Deployment.", style_corpo))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>PROJETOS DE DESTAQUE (Portfólio Full Stack)</b>", style_secao))
    story.append(HRFlowable(width="100%", thickness=1, color="#d1d5db", spaceAfter=6))
    
    story.append(Paragraph("<b>Projeto 1: SaaS de Produtividade com Inteligência Artificial</b>", style_corpo))
    story.append(Paragraph("• Desenvolvimento de uma aplicação web fim a fim utilizando <b>FastAPI</b> e <b>SQLModel</b>, integrando modelos de linguagem avançados (LLMs via OpenAI API).", style_item))
    story.append(Paragraph("• Implementação de segurança e controle de sessão através de autenticação por tokens <b>JWT (Json Web Tokens)</b> e criptografia de senhas com <i>bcrypt</i>.", style_item))
    story.append(Paragraph("• Construção de microsserviço assíncrono para geração dinâmica de relatórios corporativos estruturados exportáveis no formato <b>PDF nativo</b> via biblioteca ReportLab.", style_item))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>Projeto 2: Marketplace / Loja Virtual Transacional</b>", style_corpo))
    story.append(Paragraph("• Construção de uma plataforma de e-commerce com catálogo de serviços dinâmico populado por meio de <i>seeds</i> estruturados integrados ao banco de dados.", style_item))
    story.append(Paragraph("• Arquitetura de dados relacionais mapeando entidades de Usuários, Produtos e Pedidos usando <b>SQLite/PostgreSQL</b>.", style_item))
    story.append(Paragraph("• Desenvolvimento de carrinho de compras responsivo em JavaScript puro e simulação transacional de rotas de checkout com retornos assíncronos.", style_item))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>Projeto 3: Automated Scraper & Analytics Dashboard</b>", style_corpo))
    story.append(Paragraph("• Construção de um robô de automação para raspagem de dados (<i>Web Scraping</i>) em Python focado em inteligência e oscilações de mercado.", style_item))
    story.append(Paragraph("• Desenvolvimento de uma interface analítica interativa (Dashboard) utilizando renderização de gráficos em CSS e HTML5 nativos para plotagem de métricas agregadas.", style_item))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>EDUCAÇÃO E CERTIFICAÇÕES</b>", style_secao))
    story.append(HRFlowable(width="100%", thickness=1, color="#d1d5db", spaceAfter=6))
    
    story.append(Paragraph("<b>• Formação Profissional: Profissão: Desenvolvedor Full Stack Python</b> – EBAC", style_corpo))
    story.append(Paragraph("Conclusão: 05/07/2026 | Carga Horária: 77+ Horas | Registro Verificador: 79274-40500-32013-36115", style_item))
    story.append(Paragraph("<b>• Extensão Profissional: Desenvolvedor Back-End Python</b> – EBAC", style_corpo))
    story.append(Paragraph("Conclusão: 05/07/2026 | Carga Horária: 41 Horas | Registro Verificador: 62429-40500-90129-22054", style_item))
    story.append(Paragraph("<b>• Extensão Profissional: Desenvolvedor Front-End</b> – EBAC", style_corpo))
    story.append(Paragraph("Conclusão: 03/03/2026 | Carga Horária: 37 Horas | Registro Verificador: 09969-40500-82267-45142", style_item))
    story.append(Paragraph("<b>• Curso de Extensão: TI do Zero ao Pro</b> – EBAC", style_corpo))
    story.append(Paragraph("Conclusão: 14/07/2025 | Carga Horária: 10 Horas | Registro Verificador: 33266-40500-44611-22408", style_item))
    
    doc.build(story)
    return FileResponse(arquivo_pdf, media_type="application/pdf", filename="Curriculo_Jonas_Machado.pdf")
