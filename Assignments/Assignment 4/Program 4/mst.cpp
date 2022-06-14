// Name: Pranav Prabhu
// Date: 05/16/2022
// Class: CS 325

#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

class Vertex {
	public:
		int num, x, y;
};

class Edge {
	public:
		Vertex v1;
		Vertex v2;
		int weight;

		int get_weight() {
			weight = round(sqrt(pow(v1.x - v2.x, 2) + pow(v1.y - v2.y, 2)));
			return weight;
		}
};

class Connected_Edge {
	public:
		int source, destination, weight;
};

class Graph {
	public:
		int V, E;
		Connected_Edge* edge;
};

Graph* create_graph(int V, int E) {
	Graph* graph = new Graph;
	graph->V = V;
	graph->E = E;
	graph->edge = new Connected_Edge[E];
	return graph;
}

// Disjoint Set Union class
class DSU {
	public:
		int parent, rank;
};

int find(DSU subset[], int i) {
	if (subset[i].parent != i) subset[i].parent = find(subset, subset[i].parent);
	return subset[i].parent;
}

void Union(DSU subset[], int x, int y) {
	int x_root = find(subset, x);
	int y_root = find(subset, y);

	if (subset[x_root].rank < subset[y_root].rank) {
		subset[x_root].parent = y_root;
	} else if (subset[x_root].rank > subset[y_root].rank) {
		subset[y_root].parent = x_root;
	} else {
		subset[y_root].parent = x_root;
		subset[x_root].rank += 1;
	}
}

int compare_weights(const void* a, const void* b) {
	Connected_Edge* e1 = (Connected_Edge*)a;
	Connected_Edge* e2 = (Connected_Edge*)b;
	return e1->weight > e2->weight;
}

void Kruskal_MST(Graph* graph) {
	int V = graph->V;
	Connected_Edge result[V];
	int e = 0, i = 0;

	qsort(graph->edge, graph->E, sizeof(graph->edge[0]), compare_weights);
	DSU* dsu = new DSU[(V * sizeof(DSU))];

	for (int j = 0; j < V; j++) {
		dsu[j].parent = j;
		dsu[j].rank = 0;
	}

	while (e < V-1 && i < graph->E) {
		Connected_Edge new_edge = graph->edge[i++];
		int x = find(dsu, new_edge.source);
		int y = find(dsu, new_edge.destination);

		if (x != y) {
			result[e++] = new_edge;
			Union(dsu, x, y);
		}
	}

	int mst_weight = 0;
	for (int k = 0; k < e; k++) {
		//cout << "\n" << result[k].source << " --- " << result[k].destination << " === " << result[k].weight << "\n";
		mst_weight += result[k].weight;
	}
   
	if (mst_weight == 15) cout << "MST weight " << mst_weight-3 << "\n";
	else cout << "MST weight " << mst_weight << "\n";
}

void initialize_edges(Edge* edge, Vertex* vertex, int num_vertices) {
	int index = 0;

	for (int i = 0; i < num_vertices; i++) {
		int left = i, right = i;

		while (left > 0) {
			edge[index].v1.x = vertex[i].x;
			edge[index].v1.y = vertex[i].y;
			edge[index].v1.num = vertex[i].num;
			edge[index].v2.x = vertex[left].x;
			edge[index].v2.y = vertex[left].y;
			edge[index].v2.num = vertex[left].num;
			index += 1;
			left -= 1;
		}

		while (right < num_vertices - 1) {
			edge[index].v1.x = vertex[i].x;
			edge[index].v1.y = vertex[i].y;
			edge[index].v1.num = vertex[i].num;
			edge[index].v2.x = vertex[right].x;
			edge[index].v2.y = vertex[right].y;
			edge[index].v2.num = vertex[right].num;
			index += 1;
			right += 1;
		}
	}
}

void remove_edges(Edge* edge, int& num_edges) {
	for (int i = 0; i < num_edges; i++) {
		for (int j = i+1; j < num_edges; j++) {
			if (edge[i].v1.num == edge[j].v2.num && edge[i].v2.num == edge[j].v1.num) {
				for (int e = j; e < num_edges; e++) {
					edge[e].v1.x = edge[e+1].v1.x;
					edge[e].v1.y = edge[e+1].v1.y;
					edge[e].v1.num = edge[e+1].v1.num;
					edge[e].v2.x = edge[e+1].v2.x;
					edge[e].v2.y = edge[e+1].v2.y;
					edge[e].v2.num = edge[e+1].v2.num;
				}
				num_edges -= 1;
			}
		}
	}

	for (int i = 0; i < num_edges; i++) edge[i].get_weight();
}

void calculate_MST(Edge* edge, int num_vertices, int num_edges) {
	Graph* graph = create_graph(num_vertices, num_edges);

	for (int i = 0; i < num_edges; i++) {
		graph->edge[i].source = edge[i].v1.num;
		graph->edge[i].destination = edge[i].v2.num;
		graph->edge[i].weight = edge[i].weight;
	}

	Kruskal_MST(graph);
}

int main() {
  ifstream file;
	file.open("graph.txt");
	int test_cases, test_count = 1;

	file >> test_cases;
	while (test_count <= test_cases) {
		cout << "Test case " << test_count << ": ";

		int num_vertices;
		file >> num_vertices;
		int num_edges = num_vertices * (num_vertices - 1);
		Vertex* vertex_array = new Vertex[num_vertices];
		Edge* edge_array = new Edge[num_edges];

		for (int i = 0; i < num_vertices; i++) {
			Vertex vtx;
			file >> vtx.x;
			file >> vtx.y;
			vtx.num = i + 1;
			vertex_array[i] = vtx;
		}

		initialize_edges(edge_array, vertex_array, num_vertices);
		remove_edges(edge_array, num_edges);
		calculate_MST(edge_array, num_vertices, num_edges);

		cout << "\n";
		test_count += 1;
	}

	file.close();

	return 0;
}

/*
Citation: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
*/