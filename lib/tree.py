
class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, target_id):
    # Helper function to perform depth-first search
    def dfs(node, target_id):
      # Base case: if node is None, return None
      if node is None:
        return None
      
      # Check if the current code matches the target_id
      if node.get('id') == target_id:
        return node

      for child in node.get('children', []):
        result = dfs(child, target_id)
        if result is not None:
          return result
        
      return None
    
    # Call the dfs function starting from the root node
    return dfs(self.root, target_id)
