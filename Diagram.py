import matplotlib.pyplot as plt
import networkx as nx

#
Diagram = nx.DiGraph()

#
Diagram.add_node("Padaria", label="Padaria\n- nome: Padaria 7 Sonhos\n- endereço: Rua da Sorte, 7\n+ contratar_Funcionario(): void")
Diagram.add_node("Cliente", label="Cliente\n- nome: Gabriel de Almeida\n- endereço: Rua Irimirim, 04\n- telefone: (11) 95732-4839\n+ realizar_Pedido(): void")
Diagram.add_node("Funcionário", label="Funcionário\n- nome: Edgar dos Santos\n- cargo: Balconista\n- salário: 1.240,43")
Diagram.add_node("Produto", label="Produto\n- nome: Baguete 500g\n- preço: 13,30\n+ quantidade: int")
Diagram.add_node("Gerente", label="Gerente\n- area_Responsavel: Vendas\n+ gerenciar(): void")

#
pos = {
    "Padaria": (0, 0),
    "Cliente": (1, 0),
    "Funcionário": (2, 0),
    "Produto": (3, 0),
    "Gerente": (2, -1)
}

#
Diagram.add_edge("Padaria", "Cliente")
Diagram.add_edge("Padaria", "Funcionário")
Diagram.add_edge("Padaria", "Produto")
Diagram.add_edge("Padaria", "Gerente")
Diagram.add_edge("Gerente", "Funcionário")

#
plt.figure(figsize=(15, 8))

#
nx.draw_networkx_nodes(Diagram, pos, node_size=5000, node_color='black')
nx.draw_networkx_edges(Diagram, pos, edgelist=Diagram.edges(), arrows=True)
nx.draw_networkx_labels(Diagram, pos, labels=nx.get_node_attributes(Diagram, 'label'), font_size=8, font_color='black', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

#
plt.title("State Diagram UML")
plt.axis('off')
plt.show()