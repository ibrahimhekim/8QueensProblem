import random
import matplotlib.pyplot as plt
import numpy as np

# Fitness değerini hesapla

"""
8x8 boyutunda bir tahta üzerinde 8 vezirin konumlarının nasıl belirleneceğini gösteren bir Genetik Algoritma (GA) uygulamasıdır. Bu GA, vezirler arasındaki çakışmaları en aza indirmek için kullanılır. Özellikle, GA, rastgele oluşturulan başlangıç popülasyonu, seçilen elemanlar arasından çocuklar oluşturma, popülasyonun genetik özelliklerini değiştirme ve en iyi sonucu elde etmek için döngüler içerir.

Kod, "calculate_fitness" adlı bir fonksiyon kullanarak vezirler arasındaki çakışmaları hesaplar ve "generate_initial_population" adlı bir fonksiyon kullanarak rastgele oluşturulan başlangıç popülasyonunu oluşturur. "crossover" ve "mutate" adlı fonksiyonlar kullanılarak seçilen elemanlar arasından çocuklar oluşturulur ve popülasyonun genetik özellikleri değiştirilir.

Son olarak, "display_result" adlı bir fonksiyon kullanılarak en iyi sonuç görüntülenir. En iyi sonuç, en az çakışma olan kromozomdur.
"""

def calculate_fitness(chromosome):
    collisions = 0
    for i in range(len(chromosome)):
        for j in range(i+1, len(chromosome)):
            # Vezirler arasındaki çakışma kontrolü
            if abs(chromosome[i] - chromosome[j]) in (0, abs(i-j)):
                collisions += 1

    return 28 - collisions
"""28, tahtadaki maksimum olası çakışma sayısına karşılık gelir. çakışma sayısını bu değerden çıkartarak uygunluk skoru hesaplanır."""
"""Bu fonksiyon, her bir kromozom için bir "fitness" değeri hesaplar ve bu değer, kromozomun ne kadar uygun olduğunu gösterir."""

# İlk popülasyon oluşturma

def generate_initial_population(size):
    population = []
    for i in range(size):
        random_chromosome = list(range(8))
        random.shuffle(random_chromosome)
        population.append(random_chromosome)
    return population
"""Bu fonksiyon N-Vezir problemi için başlangıç popülasyonunu oluşturmak için kullanılır."""
"""Başlangıçta, bir dizi oluşturulur ve size parametresi kadar döngü içinde diziye eleman eklenir."""
"""Döngü içinde, her bir kromozom için 8 hücreli bir satranç tahtını temsil eden bir dizi oluşturulur."""
"""Bu dizi içindeki elemanlar rasgele şekilde karıştırılır. Bu, her kromozom için rasgele vezir yerleştirmelerini temsil eder."""

"""Son olarak, her bir rasgele kromozom diziye eklenir ve oluşan dizi popülasyon olarak geri döndürülür."""
"""Bu popülasyon, genetik algoritma için başlangıç noktası olarak kullanılır."""

# Seçilen elemanlar arasından çocuklar oluşturma

def crossover(parent1, parent2):
    child = []
    child_p1 = []
    child_p2 = []
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)
    for i in range(startGene, endGene):
        child_p1.append(parent1[i])
    child_p2 = [item for item in parent2 if item not in child_p1]
    child = child_p1 + child_p2
    return child
"""İki ebeveyn kromozomunu (listeler olarak temsil edilmiş) girdi olarak alır ve çocuk kromozomu çıktı olarak üretir."""
"""geneA ve geneB adında iki rastgele gen oluşturulur."""
"""startGene ve endGene, geneA ve geneB'nin minimum ve maksimumlarını alarak hesaplanır. """
"""for döngüsüyle, startGene ile endGene arasındaki elemanlar child_p1'e eklenir."""
"""child_p1 listesinde mevcut olan elemanları içermeyen child_p2 listesi oluşur"""
"""Son olarak, child_p1 ve child_p2 listeleri birleştirilerek son çocuk kromozomu oluşur ve geri döndürülür."""

# Popülasyonun genetik özelliklerini değiştirme

def mutate(chromosome):
    if random.random() > 0.1:
        return chromosome
    gene1 = int(random.random() * len(chromosome))
    gene2 = int(random.random() * len(chromosome))
    chromosome[gene1], chromosome[gene2] = chromosome[gene2], chromosome[gene1]
    return chromosome
"""Fonksiyon, random.random() ile 0 ile 1 arasında rastgele bir sayı üretir. """
"""Eğer bu sayı 0.1'den büyükse, fonksiyon girdi kromozomunu değiştirmeden geri döndürür."""
"""Bu, kromozomun mutasyona uğramama olasılığını simüle eder."""

"""Eğer sayı 0.1'den küçükse, fonksiyon iki gene1 ve gene2 değişkeni oluşturur."""
""""Bu değişkenleri kullanarak kromozomun rastgele iki noktasını seçer ve kromozomdaki bu iki noktayı yer değiştirir."""
""""Yeni kromozom en son geri döndürülür. Bu işlem kromozomun mutasyon olasılığını simüle eder."""

# Sonuçları görüntüleme

def display_result(chromosome):
    board = [['x' for x in range(8)] for y in range(8)]
    for col, row in enumerate(chromosome):
        board[row][col] = 'Q'
    for row in board:
        print(" ".join(row))
"""Verilen kromozomdaki verileri kullanarak 8x8 lik bir tahta oluşturur ve bu tahtada vezirlerin yerlerini gösterir."""
"""chromosome, 8 tane vezirin yerleşeceği sütunların sıralamasını içerir. Bu sıralama kullanılarak, her vezirin satır konumu hesaplanır."""

"""board değişkeni, 8x8 lik bir tahta oluşturur ve tüm hücreleri başlangıçta 'x' karakteri ile doldurulur."""

"""for col, row in enumerate(chromosome): döngüsü ile her vezirin sütun ve satır konumları belirlenir. enumerate fonksiyonu, dizi içindeki elemanların indekslerini ve değerlerini döndürür."""

"""board[row][col] = 'Q' satırı ile, belirlenen satır ve sütun konumunda 'Q' karakteri yerleştirilir."""

"""Son olarak, for row in board: döngüsü ile tahta satırları yazdırılır."""
"""join fonksiyonu ile, her satırdaki hücreler arasına boşluk konulur ve satır ekrana yazdırılır."""

# Algoritma için temel döngü

def genetic_algorithm():
    population = generate_initial_population(100)
    for i in range(100):
        population = sorted(
            population, key=lambda x: calculate_fitness(x), reverse=True)
        if calculate_fitness(population[0]) == 28:
            return population[0]
        new_generation = []
        new_generation.append(population[0])
        new_generation.append(population[1])
        for j in range(98):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_generation.append(child)
        population = new_generation
"""sorted() fonksiyonu bireyleri fitness değerlerine göre sıralamak için kullanılıyor."""
"""calculate_fitness(x) fonksiyonu kullanılarak her bireyin fitness değeri hesaplanır ve bu değerler kullanılarak bireyler sıralanır."""
"""reverse=True parametresi ile, en yüksek fitness değerine sahip bireyler en başta olur. Bu sayede, en iyi bireyler seçilip, yeni nesil için kullanılabilir."""

"""Eğer en iyi bireyin fitness değeri 28'e eşitse, bu birey geri döndürülür."""
"""Sonra, 98 adet daha birey oluşturulur."""
"""random.choice() satırları ile population dizisi içinden rastgele iki ebeveyn seçilir"""
"""Bu ebeveynlerden crossover fonksiyonu ile çocuk oluşturulur."""
"""Oluşan çocuk mutate fonksiyonu ile mutasyona uğratılır. Ve oluşan çocuk yeni nesil içine eklenir."""

"""Son olarak, population değişkeni yeni nesil ile güncellenir ve döngü tekrar başlar."""
"""Bu işlem, 100 nesil boyunca devam eder ve en iyi birey geri döndürülür. """

display_result(genetic_algorithm())
