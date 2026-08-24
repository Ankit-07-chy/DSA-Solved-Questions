from collections import deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []
        
        # Step 1: Map child -> parent using BFS
        parent_map = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)
        
        # Step 2: BFS starting from target going 3 directions (left, right, parent)
        visited = set([target])
        queue = deque([(target, 0)])  # (node, current_distance)
        result = []
        
        while queue:
            node, dist = queue.popleft()
            
            # If we reached distance k, collect node value
            if dist == k:
                result.append(node.val)
                continue  # Do not explore beyond distance k
            
            # Explore all 3 possible adjacent neighbors
            for neighbor in (node.left, node.right, parent_map.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
                    
        return result