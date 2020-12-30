
### Estatística ###

## numpy ##
#doc https://numpy.org/doc/stable/reference/routines.statistics.html?highlight=statistics
import numpy as np
average_age = np.average(author_ages) # média
median_age = np.median(sorted_author_ages) # mediana
teacher_one_variance = np.var(teacher_one_grades) # variância
standard_deviation = np.std() # Desvio Padrão
songs_q1 = np.quantile(songs,0.25) # primeiro quartil
songs_q2 = np.quantile(songs,0.5) # mediana
songs_q3 = np.quantile(songs,0.75) # terceiro quartil

## Outra opcao é usar array:
quartiles = np.quantile(songs,[0.25,0.5,0.75])
deciles = np.quantile(songs,[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])

min_time = np.amin(times) # <-- min calc
max_time = np.amax(times) # <-- max calc
range_time = max_time - min_time # <-- Replace max - min

## scipy ##
from scipy import stats
example_mode = stats.mode(example_array) # moda


### Histograma ###

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
df = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
DATA = df['coluna']

# Use plt.hist() below
plt.hist(DATA, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Authors at Publication")
plt.xlabel("Age")
plt.ylabel("Count")
plt.axvline(x=q1, c = 'r') # quartil 1
plt.axvline(x=q2, c = 'r') # quartil 2 == Mediana
plt.axvline(x=q3, c = 'r') # quartil 3
for i in range(1, 10):
  plt.axvline(x=np.quantile(songs, i/10), c = 'r') # botar decil no mapa (termina em 9)
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.axvline(median_age, color='y', linestyle='dotted', linewidth=3, label="median")
plt.axvline(mode_age, color='orange', linestyle='dashed', linewidth=3, label="Mode")

plt.legend()
plt.tight_layout() # ajuda a nao encavalar as palavras e o gráfico
plt.show()

### BOXPLOT ###

Quadrado = Quartil
1(0.25)
até
o
Quartil
3(0.75)  # No meio é a mediana que é o quartil 0.5
Os
whiskers
são:
quartile_one = np.quantile(dataset, 0.25)
quartile_three = np.quantile(dataset, 0.75)

iqr = quartile_three - quartile_one
distance = iqr * 1.5

left_whisker = quartile_one - distance
right_whisker = quartile_three + distance

plt.boxplot([two_thousand, two_thousand_one, two_thousand_two], labels=["2000 Songs", "2001 Songs", "2002 Songs"])
plt.show()


### REGEX ###

#Limpar string de todas, no caso todos "%"
students.score = students.score.replace('[\%,]','', regex=True)

#De "11th Grade" -> Como tirar só o numero e ja retornar (index é 1)
students.grade = students.grade.str.split('(\d+)',expand=True)[1]

# Como separar por espaço ' '
df.coluna.str.split(' ')

## Como falar com {}.format
sample_1_mean = np.mean(sample_1)
print "Sample 1 Mean: {}".format(sample_1_mean)


### TYPES ###

#Descobrir o type de todas colunas
print(students.dtypes)

#Transformar em numerico (usando o panda as pd)
students["score"] = pd.to_numeric(students.score)


### GARBAGE COLLECTOR ###

#limpar linhas com NaN
bill_df = bill_df.dropna()
#Limpar linhas com NaN na coluna "X"
bill_df = bill_df.dropna(subset=['X'])
#Completar linhas com Nan
bill_df = bill_df.fillna(15)
#Completar linhas de Nan na coluna "X" e "Y"
bill_df = bill_df.fillna(value={"X":bill_df.bill.mean(), "Y":15})

#dropar duplicadas
df = df.drop_duplicates(subset=['reps'])

### DATA FINDING ###

#Pegar só a coluna "TemperatureC" com uma condição (coluna month == 6)
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
