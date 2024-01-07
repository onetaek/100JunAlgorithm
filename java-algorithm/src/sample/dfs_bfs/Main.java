package sample.dfs_bfs;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Graph g = new Graph(9);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
        g.addEdge(3, 5);
        g.addEdge(5, 6);
        g.addEdge(5, 7);
        g.addEdge(6, 8);
        g.bfs();
    }
}

class Graph {
    Node[] nodes;
    Graph(int size) {
        nodes = new Node[size];
        for (int i = 0 ; i < size; i++ ){
            nodes[i] = new Node(i);
        }
    }
    class Node {
        int data;
        LinkedList<Node> adjacentNode;//인접한 노드
        boolean marked;//순회한 요소인지 아닌지 확인하는 값
        Node(int data) {
            this.data = data;
            this.marked = false;
            adjacentNode = new LinkedList<Node>();
        }
    }

    void addEdge(int i1, int i2) {
        Node n1 = nodes[i1];
        Node n2 = nodes[i2];
        if (!n1.adjacentNode.contains(n2)) {
            n1.adjacentNode.add(n2);
        }

        if (!n2.adjacentNode.contains(n1)) {
            n2.adjacentNode.add(n1);
        }
    }
    void dfs() {
        dfs(0);
    }
    void dfs(int index) {
        Node root = nodes[index];
        Stack<Node> stack = new Stack<Node>();
        stack.push(root);
        root.marked = true;
        while (!stack.isEmpty()) {
            Node r = stack.pop();
            for (Node n : r.adjacentNode) {
                if (n.marked == false) {
                    n.marked = true;
                    stack.push(n);
                }
            }
            System.out.print(r.data + " ");
        }
    }

    void bfs() {
        bfs(0);
    }

    void bfs(int index) {
        Node root = nodes[index];
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);
        root.marked = true;
        while(!queue.isEmpty()) {
            Node r = queue.poll();
            for (Node n : r.adjacentNode) {
                if (n.marked == false) {
                    n.marked = true;
                    queue.add(n);
                }
            }
            System.out.print(r.data + " ");
        }
    }
}
