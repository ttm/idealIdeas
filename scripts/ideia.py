#-*- coding: utf8 -*-
import networkx as x, pylab as p 

arestas=[(1,1)]

rc=x.Graph() # Rede complexa com arestas direcionadas.
for aresta in arestas:
    rc.add_edge(aresta[0],aresta[1])

pos=x.spring_layout(rc)

x.draw_networkx_nodes(rc,pos,
        node_color='r',
        node_size=500,
        alpha=0.8)

#x.draw_networkx_edges(rc,pos,width=1.0,alpha=0.5)


p.xticks(())
p.yticks(())
p.show()
