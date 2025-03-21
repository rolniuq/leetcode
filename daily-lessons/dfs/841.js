const dfs = (visited, graph, start) => {
  visited[start] = true;

  for (let i = 0; i < graph[start].length; i++) {
    if (!visited[graph[start][i]]) {
      dfs(visited, graph, graph[start][i]);
    }
  }
};

const canVisitAllRooms = (rooms) => {
  const visited = new Array(rooms.length).fill(false);

  const graph = {};
  for (let i = 0; i < rooms.length; i++) {
    graph[i] = rooms[i];
  }

  dfs(visited, graph, 0);

  return visited.every((room) => room);
};
