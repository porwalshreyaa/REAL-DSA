// Adjacency List

// const nodes = ['a', 'b', 'c', 'd']
// const edges = [['a', 'b'], ['a', 'd'], ['d', 'b'], ['c', 'd']]

// [[1, 3], [0, 3], [3], [0, 1, 2]]

function graphList(nodes, edges) {
    let nodeMap = new Map()
    let graph = []
    nodes.forEach((node, index) => {
        nodeMap.set(node, index);
        graph.push([]);
    });
    for (const [uNode, vNode] of edges) {
        let u = nodeMap.get(uNode);
        let v = nodeMap.get(vNode);
        graph[u].push(v);
        graph[v].push(u);
    }

    return graph
}

// console.log(graphList(nodes, edges))

//--------------------------------------------------------------------------------------

// Weighted

// const nodes = ['a', 'b', 'c', 'd']
// const edges = [['a', 'b', 2], ['a', 'd', 4], ['d', 'b', 1], ['c', 'd', 3]]

// [[(1,2), (3,4)], [(0,2),(3, 1)], [(3, 3)], [(0, 4), (1, 1), (2, 3)]]

function graphListWeighted(nodes, edges) {
    let nodeMap = new Map()
    let graph = []
    nodes.forEach((node, index)=>{
        nodeMap.set(node,index);
        graph.push([]);
    });
    for (const [uNode, vNode, weight] of edges) {
        let u = nodeMap.get(uNode);
        let v = nodeMap.get(vNode);
        graph[u].push([v, weight]);
        graph[v].push([u, weight]);
    }

    return graph
}

// console.log(graphListWeighted(nodes, edges))

//--------------------------------------------------------------------------------------

// Adjacency Matrix

// const nodes = ['a', 'b', 'c', 'd']
// const edges = [['a', 'b'], ['a', 'd'], ['d', 'b'], ['c', 'd']]

// [[0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 0]]

function graphMatrix(nodes, edges) {
    let nodeMap = new Map();
    let graph = []
    nodes.forEach((node,index)=>{
        nodeMap.set(node,index);
        graph.push(Array.from({ length: nodes.length }, () => 0));
    });
    for (const [uNode, vNode] of edges) {
        let u = nodeMap.get(uNode);
        let v = nodeMap.get(vNode);
        graph[u][v] = 1;
        graph[v][u] = 1;
    }

    return graph
}

// console.log(graphMatrix(nodes, edges))


//--------------------------------------------------------------------------------------

// Weighted

// const nodes = ['a', 'b', 'c', 'd']
// const edges = [['a', 'b', 2], ['a', 'd', 4], ['d', 'b', 1], ['c', 'd', 3]]

// [ [ 0, 2, 0, 4 ], [ 2, 0, 0, 1 ], [ 0, 0, 0, 3 ], [ 4, 1, 3, 0 ] ]


function graphMatrixWeighted(nodes, edges) {
    let nodeMap = new Map()
    let graph = []
    nodes.forEach((node, index)=>{
        nodeMap.set(node,index);
        graph.push(Array.from({ length: nodes.length }, () => 0));
    });
    for (const [uNode, vNode, weight] of edges) {
        let u = nodeMap.get(uNode);
        let v = nodeMap.get(vNode);
        graph[u][v] = weight;
        graph[v][u] = weight;
    }

    return graph
}

// console.log(graphMatrixWeighted(nodes, edges))