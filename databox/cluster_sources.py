import pandas as pd
import networkx as nx
from cdlib import algorithms

df = pd.read_csv('./databox/databox_data/query-20220118.csv', sep=';',
                 decimal=',')
G = nx.from_pandas_edgelist(df, 'space_id', 'key', )

def clusters(G, alg):
  """
  Find and print out standard statistics of clusters of undirected multigraph G.
  """
  tic = time()
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  comms = alg(G)
  print("{0:>15s} | '{1:s}'".format('Algorithm', comms.method_name.lower()))
  print("{0:>15s} | {1:,d}".format('Clusters', len(comms.communities)))
#  truth = {}
#  for node in G.nodes(data = True):
#    cluster = node[1]['cluster'] if 'cluster' in node[1] else 0
#    if cluster not in truth:
#      truth[cluster] = []
#    truth[cluster].append(node[0])
#  truth = NodeClustering(list(truth.values()), G, 'truth')
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))
  return comms

comms = clusters(G, lambda G: algorithms.louvain(G))
comms

