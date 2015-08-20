#-*- coding: utf8 -*-
import networkx as x, pylab as p, random as r

arestas=[(1,1)]
nodes=range(3000)

# 150 ideias de FP 2
rc=x.Graph() # Rede complexa com arestas direcionadas.

rc.add_nodes_from(nodes)

edges=[(r.choice(nodes),r.choice(nodes)) for i in xrange(150)]

for edge in edges:
    rc.add_edge(*edge)

edges3[(r.choice(nodes),r.choice(nodes),r.choice(nodes)) for i in xrange(4)]
for edge in edges3:
    rc.add_edge(edge[0],edge[1])
    rc.add_edge(edge[1],edge[2])

for i in xrange(3):
    n1=r.choice(nodes)
    n2=r.choice(nodes)
    n3=r.choice(nodes)
    n4=r.choice(nodes)
    rc.add_edge(n1,n2)
    rc.add_edge(n2,n3)
    rc.add_edge(n3,n4)


#
#pos=x.spring_layout(rc)
#
#x.draw_networkx_nodes(rc,pos,
#        node_color='r',
#        node_size=500,
#        alpha=0.8)
#
#x.draw_networkx_edges(rc,pos,width=1.0,alpha=0.5)
x.draw(rc)
#x.draw_graphviz(rc)

p.xticks(())
p.yticks(())
p.show()
