const API_URL = "/api";

async function carregarProjetos() {
    const gridProjetos = document.querySelector("#projetos .grid");
    
    if (!gridProjetos) return;

    try {
        const response = await fetch(`${API_URL}/projetos`);
        const projetos = await response.json();
        gridProjetos.innerHTML = "";

        // Card 1: SaaS de Produtividade com IA
        projetos.forEach(projeto => {
            gridProjetos.innerHTML += `
                <div class="card">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: start;">
                            <span class="card-status disponivel">Disponível</span>
                            <span style="font-size: 0.75rem; color: #6b7280;">💻 Full Stack</span>
                        </div>
                        <h3>${projeto.titulo}</h3>
                        <p>${projeto.descricao}</p>
                    </div>
                    <div>
                        <div class="tags">
                            <span class="tag">FastAPI</span>
                            <span class="tag">SQLModel</span>
                            <span class="tag">PostgreSQL</span>
                            <span class="tag">OpenAI</span>
                        </div>
                        <a href="/login" class="btn-primary" style="display: block; text-align: center; margin-top: 1rem; padding: 0.5rem; text-decoration: none; font-size: 0.875rem;">Acessar Sistema</a>
                    </div>
                </div>
            `;
        });

        // Card 2: Marketplace E-commerce
        gridProjetos.innerHTML += `
            <div class="card" style="border-color: rgba(16, 185, 129, 0.4);">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <span class="card-status" style="color: #34d399; background-color: rgba(52, 211, 153, 0.1); border-color: rgba(52, 211, 153, 0.2);">Disponível</span>
                        <span style="font-size: 0.75rem; color: #6b7280;">🛒 E-commerce</span>
                    </div>
                    <h3>Marketplace Tech Shop</h3>
                    <p>Loja virtual completa com catálogo dinâmico, gerenciamento de estoque integrado ao banco e simulação de checkout transacional.</p>
                </div>
                <div>
                    <div class="tags">
                        <span class="tag">FastAPI</span>
                        <span class="tag">SQLModel</span>
                        <span class="tag">PostgreSQL</span>
                    </div>
                    <a href="/loja" class="btn-primary" style="display: block; text-align: center; margin-top: 1rem; padding: 0.5rem; text-decoration: none; font-size: 0.875rem; background-color: #10b981; box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.3);">Entrar na Loja</a>
                </div>
            </div>
        `;

        // --- MUDANÇA AQUI: Card 3 - Transforma o card cinza no Projeto 3 Real ---
        gridProjetos.innerHTML += `
            <div class="card" style="border-color: rgba(59, 130, 246, 0.4);">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <span class="card-status" style="color: #60a5fa; background-color: rgba(59, 130, 246, 0.1); border-color: rgba(59, 130, 246, 0.2);">Disponível</span>
                        <span style="font-size: 0.75rem; color: #6b7280;">📊 Analytics</span>
                    </div>
                    <h3>Automated Scraper & Analytics</h3>
                    <p>Robô de automação que realiza raspagem de dados (Web Scraping) em tempo real, trata os registros e exibe métricas completas em um painel interativo.</p>
                </div>
                <div>
                    <div class="tags">
                        <span class="tag">FastAPI</span>
                        <span class="tag">Web Scraping</span>
                        <span class="tag">Automation</span>
                    </div>
                    <a href="/analytics" class="btn-primary" style="display: block; text-align: center; margin-top: 1rem; padding: 0.5rem; text-decoration: none; font-size: 0.875rem; background-color: #3b82f6; box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);">Ver Analytics</a>
                </div>
            </div>
        `;

    } catch (error) {
        console.error("Erro na aplicação:", error);
        gridProjetos.innerHTML = `<p style="color: #f87171; text-align: center; grid-column: 1/-1;">Erro ao conectar com o backend.</p>`;
    }
}

document.addEventListener("DOMContentLoaded", carregarProjetos);


