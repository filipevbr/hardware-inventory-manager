import datetime
import json

# Taxa para o calculo do preco final
fixed_profit = 0.3

# Funcao que salva os dados do estoque
def save_data(inventory):
    with open("inventory.json", "w", encoding="utf-8") as data:
        json.dump(inventory, data, indent=4)

# Funcao que carrega os dados do estoque
def load_data():
    try:
        with open("inventory.json", "r", encoding="utf-8") as data:
            return json.load(data)
    except json.JSONDecodeError:
        print('ERRO: Não foi possível ler o arquivo.')
        return []
    except FileNotFoundError:
        return []
    
# Funcao que exibe o menu principal
def show_menu():
    print("=== MENU PRINCIPAL ===")
    print("1 - Adicionar Componentes")
    print("2 - Ver Estoque")
    print("3 - Remover Componente")
    print("4 - Sair")

# Funcao que trata os valores recebidos pelo usuario
def get_valid_float(prompt):
    while True:
        data = input(prompt).strip()  # Pede o dado usando a pergunta que veio no parametro "prompt"
        data = data.replace(",", ".")

        try:
            value = float(data)
            if value < 0:
                print("O valor não pode ser negativo.")
                continue  # Volta para o inicio do loop
            return value
        
        except ValueError:
            print("\nERRO: Digite apenas números válidos.")

# Funcao para notificar a necessidade de aprovacao da gerencia
def manager_approval():
    print("ATENÇÃO: Valor alto! Necessária a aprovação da gerencia.")

# Funcao para adicionar as pecas
def add_component(inventory):
    while True: 
        print("\n=== CADASTRAR PEÇAS ===")

        # Coleta de dados
        name = input("Digite o nome do componente: ").strip().upper()
        cost = get_valid_float(f"Digite o custo da compra de {name}: ")
        
        # Calculo
        final_value = cost * (1 + fixed_profit)

        # Pacote com os dados da peça
        item = {
            "name": name,
            "cost": cost,
            "sale": final_value,
            "registration_date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        # Adiciona o item a lista global
        inventory.append(item)
        save_data(inventory)
        
        # Feedback visual
        print(f"\n{name} cadastrado! Venda: R${final_value:.2f}")

        if final_value >= 500.00:
            manager_approval()

        # Menu de decisao
        print("\nO que deseja fazer?")
        print("1 - Cadastrar outro")
        print("2 - Voltar ao menu principal")

        option = input("Opção: ")
        if option == "2":
            break  # Quebra o loop e finaliza a funcao

# Funcao para listar pecas no estoque
def list_inventory(inventory):
    print("\n=== ESTOQUE ATUAL ===")
    if not inventory:
        print("Estoque vazio.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    for index, item in enumerate(inventory, start=1):  # Percorre a lista de estoque enumerando o indice
        print(f"{index} - Peça: {item['name']} | Custo: R${item['cost']:.2f} | Venda: R${item['sale']:.2f} - Data: {item['registration_date']}")

    input("\nPressione Enter para voltar ao menu...")

# Funcao para remover pecas do estoque
def remove_component(inventory):
    print("\n=== REMOVER COMPONENTE ===")
    if not inventory:
        print("Estoque vazio.")
        input("\nPressione Enter para voltar ao menu...")
        return

    for index, item in enumerate(inventory, start=1):  # Percorre a lista de estoque enumerando o indice
        print(f"{index} - {item['name']}")

    try:
        option = int(input("Opção: "))
        real_index = option - 1  # Ajusta o indice iniciado em 1

        if 0 <= real_index < len(inventory):
            removed_item = inventory.pop(real_index)  # Remove e guarda qual foi o indice/item removido
            save_data(inventory)
            print(f"\n{removed_item['name']} removido com sucesso!")
        else:
            print("Opção inválida.\n")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

    input("\nPressione Enter para voltar ao menu...")

# Funcao principal
def main():
    inventory = load_data()
    while True: 
        show_menu()
        option = input("Digite a opção desejada: ").strip()
        match option:
            case "1":
                add_component(inventory)
            case "2":
                list_inventory(inventory)
            case "3":
                remove_component(inventory)
            case "4":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida.\n")

if __name__ == "__main__":
    main()
