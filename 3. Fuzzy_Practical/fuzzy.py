# Fuzzy Set Class
class FuzzySet:

    def __init__(self, elements):
        self.elements = elements

    # Union Operation
    def union(self, other):
        result = {}

        for key in sorted(set(self.elements) | set(other.elements)):
            result[key] = round(
                max(self.elements.get(key, 0),
                    other.elements.get(key, 0)), 2
            )

        return result

    # Intersection Operation
    def intersection(self, other):
        result = {}

        for key in sorted(set(self.elements) & set(other.elements)):
            result[key] = round(
                min(self.elements[key],
                    other.elements[key]), 2
            )

        return result

    # Complement Operation
    def complement(self):
        result = {}

        for key, value in self.elements.items():
            result[key] = round(1 - value, 2)

        return result

    # Difference Operation
    def difference(self, other):
        result = {}

        for key in sorted(self.elements):
            result[key] = round(
                min(self.elements[key],
                    1 - other.elements.get(key, 0)), 2
            )

        return result


# Fuzzy Relation Class
class FuzzyRelation:

    # Cartesian Product
    @staticmethod
    def cartesian_product(set1, set2):
        relation = {}

        for k1, v1 in set1.elements.items():
            for k2, v2 in set2.elements.items():
                relation[(k1, k2)] = round(min(v1, v2), 2)

        return relation

    # Max-Min Composition
    @staticmethod
    def max_min_composition(r1, r2):
        result = {}

        for (x, y1) in r1:
            for (y2, z) in r2:

                if y1 == y2:

                    value = min(r1[(x, y1)],
                                r2[(y2, z)])

                    if (x, z) in result:
                        result[(x, z)] = round(
                            max(result[(x, z)], value), 2
                        )

                    else:
                        result[(x, z)] = round(value, 2)

        return result


# Main Program

# Define fuzzy sets
A = FuzzySet({
    'a': 0.5,
    'b': 0.7,
    'c': 0.2
})

B = FuzzySet({
    'a': 0.6,
    'b': 0.3,
    'c': 0.8
})


# Operations
print("Union:")
print(A.union(B))

print("\nIntersection:")
print(A.intersection(B))

print("\nComplement of A:")
print(A.complement())

print("\nDifference A-B:")
print(A.difference(B))


# Fuzzy Relations
R1 = FuzzyRelation.cartesian_product(A, B)
R2 = FuzzyRelation.cartesian_product(B, A)

print("\nCartesian Product Relation:")
print(R1)

print("\nMax-Min Composition:")
print(FuzzyRelation.max_min_composition(R1, R2))