async function drawNetwork() {
    const response = await fetch("/api/network");
    const graph = await response.json();

    // ノードの設定
    const nodes = new vis.DataSet(
        graph.nodes.map(node => ({
            id: node.id,
            label: node.label,
            color:
                node.type === "self" ? "red" :
                node.type === "gateway" ? "orange" :
                "skyblue"
        }))
    );

    // エッジの設定
    const edges = new vis.DataSet(
        graph.edges.map(edge => ({
            from: edge.source,
            to: edge.target
        }))
    );

    const container = document.getElementById("network");

    const data = { nodes, edges };

    const options = {
        nodes: {
            shape: "dot",
            size: 25,
            font: { size: 16 }
        },
        edges: {
            width: 2
        },
        physics: {
            enabled: true
        }
    };

    new vis.Network(container, data, options);
}

drawNetwork();