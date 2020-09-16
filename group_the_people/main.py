import math


class Solution:
    def make_chunks(self, items: List[int], size: int) -> List[List[int]]:
        chunks = []
        chunks_count = math.ceil(len(items) / size)

        for i in range(0, chunks_count):
            delta = size * i
            chunk = items[0 + delta : size + delta]
            chunks.append(chunk)

        return chunks

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        person_by_size = {}

        for person, size in enumerate(groupSizes):
            if size not in person_by_size:
                person_by_size[size] = []
            person_by_size[size].append(person)

        all_groups = []
        for size, persons in person_by_size.items():
            groups = self.make_chunks(persons, size)
            all_groups += groups

        return all_groups
