# 🛠️ CLI Hardware Inventory

**Um software de console em Python para gerenciar estoque de peças de manutenção (Hardware & Mobile).**

---

## 🚧 STATUS DO PROJETO
**🚀 Em Desenvolvimento (v1.0)**

O projeto já conta com o ciclo de cadastro e visualização funcional, sistema de validação de dados monetários e remoção de itens. O foco atual é a robustez na entrada de dados e a persistência automática.
> **Destaque:** O sistema conta com **persistência de dados automática** (arquivo JSON), **validação de inputs** (tratamento de vírgula/ponto) e **alertas de custo** para valores elevados.

---

## ⚙️ Funcionalidades

### Funcionalidades Implementadas
* [X] **Menu Principal:** Interface de console limpa e navegável.
* [X] **Persistência de Dados:** Salva automaticamente (`Auto-Save`) as alterações em `inventory.json`.
* [X] **Input Validation:** Função auxiliar que blinda o sistema contra erros de digitação em valores numéricos (aceita `10,50` ou `10.50`).
* [X] **Comando `ADD`:** Cadastro de componentes com registro automático de data/hora.
* [X] **Alerta Gerencial:** Flag automática que notifica quando um custo ultrapassa R$ 500,00.
* [X] **Comando `LIST`:** Visualização tabular das peças, custos e preços de venda calculados (Margem de 30%).
* [X] **Comando `DELETE`:** Remoção segura de itens baseada no índice visual da lista.
* [X] **Tratamento de Erros:** Prevenção de *crashes* ao tentar remover índices inexistentes ou carregar arquivos corrompidos.

### Funcionalidades Pendentes (Roadmap)
* [ ] **Comando `UPDATE`:** Edição de itens já cadastrados (Nome ou Preço).
* [ ] **Comando `SEARCH`:** Busca de peças por nome.
* [ ] **Dashboard:** Relatório simples de valor total em estoque.

---

## 💻 Como Usar

1.  Certifique-se de ter o **Python 3.10** (ou superior) instalado.
2.  Clone este repositório (ou baixe os arquivos).
3.  Navegue até o diretório do projeto:
    ```bash
    cd hardware-inventory-manager-python
    ```
4.  Execute o script principal:
    ```bash
    python src/main.py
    ```
---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Biblioteca `json`** (para persistência de dados)
* **Biblioteca `datetime`** (para registro temporal de entrada de estoque)

---

## 👨‍💻 Autor

* **Filipe Vaz**
      *(Estudante de Análise e Desenvolvimento de Sistemas - PUCPR)*

---

##  Declaração de Uso de IA

> Durante a preparação deste **arquivo README.md**, o autor utilizou o **Gemini (Google)** como ferramenta de apoio para **auxiliar na estruturação e revisão do texto de documentação**. Após usar essa ferramenta, o autor revisou e editou o conteúdo conforme necessário e assume total responsabilidade pelo conteúdo.

---