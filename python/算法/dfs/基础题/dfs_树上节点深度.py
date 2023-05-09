
#! 核心思想 当前点的深度一定是他的父节点的深度加1 特判根节点
#! 注意到根节点的选择不同 各个点的深度也不一样
#! 核心代码 
G=[[]]
depth={}#! 用一个字典来存储 每个点的深度
depth[1]=0
def dfs(u,fa):#! 经过分析这个题是无向图 所以我们默认根节点为1
    if u!=1:
        depth[u]=depth[fa]+1
    for x in G[u]:
        if x!=fa:
            dfs(x,u)
            
                