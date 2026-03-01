class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ""
        suggestions_final = []
        for ch in searchWord:
            prefix += ch
            sugg=[]
            for product in products:
                if product.startswith(prefix):
                    sugg.append(product)
                if len(sugg)>=3:
                    break 
            suggestions_final.append(sugg)
        return suggestions_final