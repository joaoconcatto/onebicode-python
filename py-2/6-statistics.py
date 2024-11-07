import statistics

# 1- Aplicar a média 
print(statistics.mean([3,2,5,8,9]))


# 2- Aplicar a mediana
print(statistics.median([3,2,4,2,6,7,8]))


# 3- Aplicar a moda
print(statistics.mode([2,2,2,2,6,7,9,56,10]))


"""
- Quanto mais próximo de 0 for o desvio padrão,
significa que os dados estão menos dispersos.
"""

print(statistics.stdev([1,1.1,2,2.1,3,3.1,4,4.1]))