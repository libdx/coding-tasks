class Solution:
    def _isMatched(self, sub_query: str, sub_pattern: str) -> bool:
        try:
            start = None
            for index, char in enumerate(sub_pattern):
                start = sub_query.index(char, start + 1 if start else 0)
            return True
        except IndexError:
            return False
        except ValueError:
            return False

    def isMatched(self, split_query: List[str], split_pattern: List[str]) -> bool:
        if len(split_pattern) != len(split_query):
            return False

        acc = True
        for pair in zip(split_query, split_pattern):
            acc &= self._isMatched(pair[0], pair[1])

        return acc
        
    def camelSplit(self, string: str) -> List[str]:
        def isCapitalized(text):
            if len(text) > 0:
                return text[0].isupper()
            else:
                return False
        
        threshold = ord('a')
        splits = []
        sub = ''

        for char in string:
            if ord(char) < threshold and sub:
                splits.append(sub)
                sub = ''
            sub += char
        splits.append(sub)

        return [*filter(isCapitalized, splits)]

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        split_pattern = self.camelSplit(pattern)
        
        matches = []
        for query in queries:
            split_queries = self.camelSplit(query)
            matches.append(self.isMatched(split_queries, split_pattern))
        
        return matches
