const API_URL = "/api";

async function carregarProjetos() {
    const gridProjetos = document.querySelector("#projetos .grid");
    
    if (!gridProjetos) return;

    try {
        const response = await fetch(`${API_URL}/projetos`);
        const projetos = await response.json();
        gridProjetos.innerHTML = "";

        // Card 1: Dinâmico da API Python
        projetos.forEach(projeto => {
            gridProjetos.innerHTML += `
                <div class="glass-card">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="card-tag-status">Disponível</span>
                            <span style="font-size: 0.75rem; color: #64748b; font-family: monospace;">💻 Full Stack</span>
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
                        <a href="/login" class="btn-card-action">Acessar Sistema</a>
                    </div>
                </div>
            `;
        });

        // Card 2: Marketplace
        gridProjetos.innerHTML += `
            <div class="glass-card" style="border-color: rgba(16, 185, 129, 0.2);">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="card-tag-status" style="color: #34d399; background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.2);">Disponível</span>
                        <span style="font-size: 0.75rem; color: #64748b; font-family: monospace;">🛒 E-commerce</span>
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
                    <a href="/loja" class="btn-card-action" style="background: #10b981; color: white;">Entrar na Loja</a>
                </div>
            </div>
        `;

        // Card 3: Analytics
        gridProjetos.innerHTML += `
            <div class="glass-card" style="border-color: rgba(59, 130, 246, 0.2);">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="card-tag-status" style="color: #60a5fa; background: rgba(59, 130, 246, 0.1); border-color: rgba(59, 130, 246, 0.2);">Disponível</span>
                        <span style="font-size: 0.75rem; color: #64748b; font-family: monospace;">📊 Analytics</span>
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
                    <a href="/analytics" class="btn-card-action" style="background: #3b82f6; color: white;">Ver Analytics</a>
                </div>
            </div>
        `;

    } catch (error) {
        console.error("Erro na aplicação:", error);
        gridProjetos.innerHTML = `<p style="color: #f87171; text-align: center; grid-column: 1/-1;">Erro ao conectar com o backend.</p>`;
    }
}

document.addEventListener("DOMContentLoaded", carregarProjetos);



