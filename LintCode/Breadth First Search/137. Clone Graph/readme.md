Clone an undirected graph. Each node in the graph contains a `label` and a list of its `neighbors`. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

Example1
```
Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   
```
### Clarification
How we serialize an undirected graph: http://www.lintcode.com/help/graph/

### Notice
You need return the node with the same label as the input node.