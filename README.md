# 🛠️ CLI Hardware Inventory Manager

**Um software de console em Python para gerenciar estoque de peças de manutenção (Hardware & Mobile).**

---

## 🚧 STATUS DO PROJETO
**🚀 Em Desenvolvimento (v1.1)**

O projeto já conta com o ciclo completo de CRUD (Create, Read, Update, Delete), sistema de validação monetária e persistência automática de dados em JSON.
> **Destaque:** O sistema conta com **persistência de dados automática**, **validação de inputs** e recálculo inteligente de margem de lucro ao atualizar custos.

---

## ⚙️ Funcionalidades

### Funcionalidades Implementadas
* [X] **Menu Principal:** Interface de console limpa e navegável.
* [X] **Persistência de Dados:** Salva automaticamente em `inventory.json`.
* [X] **Input Validation:** Blinda o sistema contra erros de digitação (aceita `10,50` ou `10.50`).
* [X] **Comando `ADD`:** Cadastro de componentes com data/hora e cálculo de margem (30%).
* [X] **Alerta Gerencial:** Notifica quando o preço de venda ultrapassa R$ 500,00.
* [X] **Comando `LIST`:** Visualização tabular das peças.
* [X] **Comando `UPDATE`:** Edição de Nome e Custo (com recálculo automático do preço de venda).
* [X] **Comando `DELETE`:** Remoção segura de itens.

### Funcionalidades Pendentes
* [ ] **Comando `SEARCH`:** Busca de peças pelo nome.
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
* **Biblioteca `json`** (Persistência de dados)
* **Biblioteca `datetime`** (Registro temporal)

---

## 👨‍💻 Autor

* **Filipe Vaz**
      *(Estudante de Análise e Desenvolvimento de Sistemas - PUCPR)*

---

##  Declaração de Uso de IA

> Durante a preparação deste projeto e documentação, o autor utilizou o Gemini (Google) como ferramenta de apoio para auxiliar na estruturação do código e revisão de texto. O autor revisou, testou e editou o conteúdo, assumindo total responsabilidade pelo código final.

---