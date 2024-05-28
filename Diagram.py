import matplotlib.pyplot as plt
import networkx as nx

# Direction
Diagram = nx.DiGraph()

# Class, attributes and methods
Diagram.add_node("Padaria", label="Padaria\n\n- nome: (Padaria 7 Sonhos)\n- endereço: (Rua da Sorte, 7)\n+ contratar_Funcionario(): void")
Diagram.add_node("Cliente", label="Cliente\n\n- nome: (Gabriel de Almeida)\n- endereço: (Rua Irimirim, 04)\n- telefone: ((11) 95732-4839)\n+ realizar_Pedido(): void")
Diagram.add_node("Funcionário", label="Funcionário\n\n- nome: (Edgar dos Santos)\n- cargo: (Balconista)\n- salário: 1.240,43")
Diagram.add_node("Produto", label="Produto\n\n- nome: (Baguete 500g)\n- preço: 13,30\n+ quantidade: 17")
Diagram.add_node("Gerente", label="Gerente\n\n- area_Responsavel: (Vendas)\n+ gerenciar(): void")

# Layout of diagram
pos = {
    "Padaria": (0, 0),
    "Cliente": (1, 0),
    "Funcionário": (2, 0),
    "Produto": (3, 0),
    "Gerente": (2, -1)
}

# Relationships
Diagram.add_edge("Padaria", "Cliente")
Diagram.add_edge("Padaria", "Funcionário")
Diagram.add_edge("Padaria", "Produto")
Diagram.add_edge("Padaria", "Gerente")
Diagram.add_edge("Gerente", "Funcionário")

# Size off screen
plt.figure(figsize=(15, 7))

# Customs 
#nx.draw_networkx_nodes(Diagram, pos, node_size=5000, node_color='black') # Circle behind the box(if u prefer)
nx.draw_networkx_edges(Diagram, pos, edgelist=Diagram.edges(), arrows=True)
nx.draw_networkx_labels(Diagram, pos, labels=nx.get_node_attributes(Diagram, 'label'), font_size=8, font_color='black', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

# Title
plt.title("State Diagram UML")
plt.axis('off')
plt.show()