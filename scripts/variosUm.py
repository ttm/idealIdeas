#-*- coding: utf8 -*-
import networkx as x, pylab as p 

#G=x.cubical_graph()

#p.subplots_adjust(left=0,right=1,bottom=0,top=0.95,wspace=0.01,hspace=0.01)
#p.subplot(121)
G=x.erdos_renyi_graph(10,.3)

pos=x.spring_layout(G)

x.draw_networkx_nodes(G,pos,
        node_color='r',
        node_size=500,
        alpha=0.8)

x.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

#p.subplot(122)
#G=x.erdos_renyi_graph(1,.3)
#
#pos=x.spring_layout(G)
#x.draw_networkx_nodes(G,pos,
#        node_color='r',
#        node_size=500,
#        alpha=0.8)
#
#x.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
p.xticks(())
p.yticks(())
p.show()
