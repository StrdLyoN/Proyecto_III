import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

calls_df=pd.read_csv('./megaline_calls.csv')
internet_df=pd.read_csv('./megaline_internet.csv')
messages_df=pd.read_csv('./megaline_messages.csv')
plans_df=pd.read_csv('./megaline_plans.csv')
users_df=pd.read_csv('./megaline_users.csv')

print('Preparar los datos')
print()

print(plans_df.info())
print()

print(plans_df.describe())
print()

print('Corregir datos')
print()

print(plans_df.duplicated().sum())
print()
print(plans_df.isnull().sum())
print()

print('Enriquecer los datos')
plans_df.rename(columns = {'usd_monthly_pay' : 'usd_monthly_fee' , 'mb_per_month_included': 'gb_per_month_included'}, inplace=True)
plans_df['gb_per_month_included'] = plans_df['gb_per_month_included'] / 1024
print(plans_df.head())
print()

print(users_df.info())
print()

print(users_df.describe())
print()

print('Enriquecer los datos')
print(users_df.duplicated().sum())
print()
print(users_df.isnull().sum())
print()

users_df['reg_date'] = pd.to_datetime(users_df['reg_date'],format = '%Y-%m-%d')
users_df['churn_date'] = pd.to_datetime(users_df['churn_date'],format = '%Y-%m-%d')
users_df.rename(columns={'plan': 'plan_name'}, inplace=True)
print(users_df.head())
print()
print(users_df.info())
print()
print(users_df.describe())
print()

print('Lo que hicimos con este dataframe fue cambiar el Dtype de las columnas en donde se indicaba una fecha, ya que este no tenía el correcto, esto nos permitirá realizar operaciones mas adelante, así como un mejor manejo o análisis de estos datos con otros dataframes #Lo que podemos observar de los datos es que la media de edad están en los 40´s, tenemos personas que han terminado su plan y debemos de averiguar por qué, pero la mayoria de personas siguen contratando los planes')
print()

print(calls_df.info())
print()

print(calls_df.describe())
print()

print('Enriquecer los datos')
print(calls_df.duplicated().sum())
print()
print(calls_df.isnull().sum())
print()

calls_df['call_date'] = pd.to_datetime(calls_df['call_date'],format = '%Y-%m-%d')
calls_df.rename(columns  = {'id' : 'call_id'}, inplace=True)
calls_df['duration'] = np.ceil(calls_df['duration'])
calls_df['duration'] = calls_df['duration'].fillna(0).astype('int64')
print(calls_df.head(10))
print()
print(calls_df.info())
print()

print('Lo que apreciamos es al igual que en el apartado anterior las columnas en donde se indicaba una fecha, ya que este no tenía el correcto, esto nos permitirá realizar operaciones mas adelante, así como un mejor manejo o análisis de estos datos con otros dataframes, también redondeamos la duración de las llamadas #cambiamos el nombre de la columna id por call_id para una mejor comprensión. #El tipo de dtype de duration fuue modificado para lograr operacines en pasos posteriores. #Observamos que el promedio de la duración de las llamadas es de casi 7 min, las que mas duran son de casi 40 min y debemos de identificar de que clientes son porque son los que mas nos copnsumen y hay que darles una atención especial')
print()

print(messages_df.info())
print()

print(messages_df.describe())
print()

print('Enriquecer los datos')
print()

messages_df['message_date'] = pd.to_datetime(messages_df['message_date'],format = '%Y-%m-%d')
messages_df.rename(columns  = {'id' : 'messages_id'}, inplace=True)
print(messages_df.head())
print()
print(messages_df.info())
print()
print(messages_df.describe())
print()

print('Lo que apreciamos es al igual que en el apartado anterior las columnas en donde se indicaba una fecha, ya que este no tenía el correcto, esto nos permitirá realizar operaciones mas adelante, así como un mejor manejo o análisis de estos datos con otros dataframes. #Se cambió el nombre de la columna id a messages_id para un mejor entendimiento. #el promedio que se realizan en general por los usarios de mensajes tenemos que son casi 1300')
print()

print(internet_df.info())
print()

print(internet_df.describe())
print()

print(internet_df.duplicated().sum())
print()
print(internet_df.isnull().sum())
print()

print('Enriquecer los datos')
print()

internet_df['session_date'] = pd.to_datetime(internet_df['session_date'],format = '%Y-%m-%d')
internet_df['mb_used'] = np.ceil(internet_df['mb_used'])
internet_df.rename(columns = {'mb_used' : 'gb_used'}, inplace=True)
internet_df.rename(columns  = {'id' : 'internet_id'}, inplace=True)                
internet_df['gb_used'] = internet_df['gb_used'] / 1024
print(internet_df.head())
print()
print(internet_df.info())
print()
print(internet_df.describe())
print()

print('Lo que apreciamos es al igual que en el apartado anterior las columnas en donde se indicaba una fecha, ya que este no tenía el correcto, esto nos permitirá realizar operaciones mas adelante, así como un mejor manejo o análisis de estos datos con otros dataframe, también modificamos el nombre de la columna mb_used a gb_used y convertimos sus valores. #También se modificó la columna id por internet id para una mejor comprensión #tenemos que los usuarios que mas nos consumen llegan a gastar 1693 mb, lo cual debemos de tener en cuenta que usarios ya que son los mejores usuarios')
print()

print(plans_df.head())
print()

print('Agregar datos por usuario')
print()

print('Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.')
print()
calls_df['year_month'] = pd.DatetimeIndex(calls_df['call_date']).month
monthly_calls = calls_df.groupby(['user_id', 'year_month']).size().reset_index(name='call_count')
print(monthly_calls)
print(calls_df.info())
print()

print('Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.')
print()
calls_df['year_month'] = pd.DatetimeIndex(calls_df['call_date']).month
monthly_minutes = result = calls_df.groupby(['user_id', 'year_month'], as_index=False)['duration'].sum()
print(monthly_minutes)
print()

print('Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.')
print()
messages_df['month'] = pd.DatetimeIndex(messages_df['message_date']).month
messages_per_user = messages_df.groupby(['user_id', 'month']).size().reset_index(name='message_count')
print(messages_per_user)
print()

print('Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.')
print()
internet_df['year_month'] = pd.DatetimeIndex(internet_df['session_date']).month
internet_traffic = internet_df.groupby(['user_id', 'year_month'], as_index=False)['gb_used'].sum()
print(internet_traffic.head())
print()

print('Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month')
print()

merged_df = monthly_calls.merge(monthly_minutes, on=['user_id', 'year_month'], how='outer')
merged_df = merged_df.merge(messages_per_user, left_on=['user_id', 'year_month'], right_on=['user_id', 'month'], how='outer')
merged_df = merged_df.merge(internet_traffic, on=['user_id', 'year_month'], how='outer')
merged_df.fillna(0, inplace=True)
merged_df['call_count'] = merged_df['call_count'].astype(int)
merged_df['message_count'] = merged_df['message_count'].astype(int)
print(merged_df)
print()

print(plans_df)
print('Añade la información de la tarifa')
print()

mergedusers_df = merged_df.merge(users_df[['user_id', 'plan_name']], on='user_id', how='outer')
mergedusersplans_df = mergedusers_df.merge(plans_df, on='plan_name', how='left')

print('Calcula los ingresos mensuales por usuario (resta el límite del paquete gratuito del número total de llamadas, mensajes de texto y datos; multiplica el resultado por el valor del plan de llamadas; añade la tarifa mensual en función del plan de llamadas). Nota: Dadas las condiciones del plan, ¡esto podría no ser tan trivial como un par de líneas! Así que no pasa nada si dedicas algo de tiempo a ello.]')
print()

print('Calcula el ingreso mensual para cada usuario')
print()

mergedusersplans_df['gb_used'] = np.ceil(mergedusersplans_df['gb_used'])
mergedusersplans_df.fillna(0,inplace=True)
mergedusersplans_df['message_excedent'] = mergedusersplans_df['message_count'] - mergedusersplans_df['messages_included']
mergedusersplans_df.loc[mergedusersplans_df['message_excedent']<0,'message_excedent']= 0
mergedusersplans_df['minutes_excedent'] = mergedusersplans_df['duration'] - mergedusersplans_df['minutes_included']
mergedusersplans_df.loc[mergedusersplans_df['minutes_excedent']<0,'minutes_excedent']= 0
mergedusersplans_df['gb_excedent'] = mergedusersplans_df['gb_used'] - mergedusersplans_df['gb_per_month_included']
mergedusersplans_df.loc[mergedusersplans_df['gb_excedent']<0,'gb_excedent']= 0
mergedusersplans_df['total_fee'] = (mergedusersplans_df['usd_per_message'] * mergedusersplans_df['message_excedent']) + (mergedusersplans_df['usd_per_minute'] * mergedusersplans_df['minutes_excedent']) + (mergedusersplans_df['usd_per_gb'] * mergedusersplans_df['gb_excedent']) + mergedusersplans_df['usd_monthly_fee']
print(mergedusersplans_df)
print()

print('Estudia el comportamiento de usuario')
print()

print('Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.')
print()
avg_call_duration = mergedusersplans_df.groupby(['year_month', 'plan_name'])['duration'].mean().reset_index()
sns.barplot(data=avg_call_duration, x='year_month', y='duration', hue='plan_name')
plt.title('Average Call Duration per Plan by Month')
plt.xlabel('Month')
plt.ylabel('Average Duration (minutes)')
plt.legend(title='Plan Name')
plt.show()
print()

print('Lo que podemos observar es que la gente que tiene un plan surf, registra una duración promedio por mes mayor en 6 meses comparado con el ultimate, la mitad del año tiene un mayor proemdio y la otra mitad la tiene el otro plan, ahora, debemos de analizar por qué consumen mas, y en que nos beneficia o nos perjudica.')
print()

print('Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.')
print()
sns.histplot(mergedusersplans_df, x='duration', hue='plan_name', multiple='stack', bins=30)
plt.title('Distribution of Monthly Minutes by Plan')
plt.xlabel('Monthly Minutes')
plt.ylabel('Frequency')
plt.legend(title='Plan Name')
plt.show()
print()

print('Lo que podemos observar de esta gráfica es que se concentran al rededor que los usuarios requieren entre 250 y 600 minutos por mes por usuarios de cada plan.')
print()

print('Calcula la media y la varianza de la duración mensual de llamadas.')
print()
call_duration_stats = mergedusersplans_df.groupby('year_month')['duration'].agg(['mean', 'var','std']).reset_index()
print(call_duration_stats)
print()

print('Se observa de este estudio que los meses con mas llamadas son los cercanos a los meses con mas fiestas y celebraciones. por lo que se ve claramente que pasado la mitad de año la gente realiza mas llamadas que en el primer semestre.')
print()

print('Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas')
print()

sns.boxplot(data=mergedusersplans_df, x='year_month', y='duration', hue='plan_name')
plt.title('Box Plot of Monthly Call Duration by Plan')
plt.xlabel('Month')
plt.ylabel('Duration (minutes)')
plt.legend(title='Plan Name')
plt.show()
print()

print('Lo que observamos a travez de los meses, en diciembre la duración de los minutos que ocupan los usuairos suben, esto posiblemente a las festiviades del mes, así también vemos que el mes mas bajo es enero por ambos planes.')
print()

print('Comprara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan')
print()

print('Compara la cantidad de tráfico de Internet consumido por usuarios por plan')
print()
avg_messages_per_plan = mergedusersplans_df.groupby(['year_month', 'plan_name'])['message_count'].mean().reset_index()
sns.barplot(data=avg_messages_per_plan, x='year_month', y='message_count', hue='plan_name')
plt.title('Average Number of Messages Sent per Plan by Month')
plt.xlabel('Month')
plt.ylabel('Average Number of Messages')
plt.legend(title='Plan Name')
plt.show()

g = sns.histplot(data=avg_messages_per_plan, x='message_count', hue='plan_name', multiple="stack", kde=True, bins=10)
plt.title('Distribution of Average Number of Messages Sent per Plan')
plt.xlabel('Average Number of Messages')
plt.ylabel('Frequency')
plt.legend(title='Plan Name')
plt.show()

sns.boxplot(data=mergedusersplans_df, x='year_month', y='message_count', hue='plan_name')
plt.title('Distribución del número de mensajes enviados por mes y plan')
plt.xlabel('Mes')
plt.ylabel('Número de Mensajes')
plt.legend(title='Plan Nombre')
plt.xticks(rotation=45) 
plt.show()

print('Estos gráficos en conjunto ofrecen una visión integral sobre el uso de datos por parte de los usuarios según sus planes de Internet. Se puede concluir si ciertos planes son más efectivos en términos de uso promedio, cómo varía el uso en el tiempo y la importancia de considerar la variabilidad entre los usuarios y sus patrones de uso. Esta información es valiosa para la toma de decisiones en marketing, desarrollo de productos y atención al cliente.')
print()

print('Calcular el uso promedio de GB por cada plan')
print()

average_gb_used = mergedusersplans_df.groupby('plan_name').agg({'gb_used': 'mean'}).reset_index()
sns.barplot(x='plan_name', y='gb_used', data=average_gb_used, palette='viridis')
plt.title('Uso promedio de GB por cada Plan')
plt.xlabel('Plan')
plt.ylabel('GB Usados (Promedio)')
plt.xticks(rotation=45)
plt.show()

print('Puedes observar qué plan tiene un uso promedio de GB más alto en comparación con los demás. Esto te puede ayudar a identificar qué plan resulta más atractivo para los usuarios en términos de consumo de datos. a gráfica proporciona información valiosa sobre el uso de datos entre diferentes planes y puede servir como una herramienta para la toma de decisiones y estrategias de mejora dentro de la empresa. Lo que observamos es que no hay mucha diferencia entre consumos de gb por plan.')
print()

sns.histplot(mergedusersplans_df['gb_used'], bins=30, kde=True, color='skyblue')
plt.title('Distribución de GB Usados')
plt.xlabel('GB Usados')
plt.ylabel('Frecuencia')
plt.show()

print('Nuestro consumo de usuarios regulares se concentra entre 15 y 25 gb, es lo que mas se consume en nuestros planes.')
print()

sns.boxplot(x='plan_name', y='gb_used', data=mergedusersplans_df, palette='Set2')
plt.title('Distribución de GB Usados por Plan')
plt.xlabel('Plan')
plt.ylabel('GB Usados')
plt.xticks(rotation=45)
plt.show()

print('Lo que podemos observar aquí es que el plan surf nos refleja que tenemos un par de clientes a los cuales debemos centrarnos, ya que su consumo es elevado.')
print()

monthly_fees = mergedusersplans_df.groupby(['plan_name', 'year_month'])['total_fee'].sum().reset_index()
sns.barplot(data=monthly_fees, x='year_month', y='total_fee', hue='plan_name', ci=None)
plt.title('Tarifa total mensual por plan')
plt.xlabel('Mes')
plt.ylabel('Tarifa total ($)')
plt.legend(title='Plan')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

print('Lo que nos arroja esta tabla de información es que el plan surf tiene un pago mayor que la premium, por lo que debemos de observar que clientes son los que nos dan ese impulso en ese plan para un mejor trato y sigan consumiendo, ya que son nuestros mejores clientes.')
print()

sns.histplot(mergedusersplans_df['total_fee'], bins=30, kde=True)
plt.title('Distribución de tarifas totales')
plt.xlabel('Tarifa total ($)')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()

sns.boxplot(data=mergedusersplans_df, x='plan_name', y='total_fee')
plt.title('Boxplot de tarifas totales por plan')
plt.xlabel('Plan')
plt.ylabel('Tarifa total ($)')
plt.grid(axis='y')
plt.show()

print('El plan Surf ofrece una mayor versatibilidad en cuanto a datos arrojados, tenemos mucha mas gente que consume mas de lo que tiene contratado.')
print()

print('Prueba las hipótesis estadísticas')
print()

print('Prueba la hipótesis de que son diferentes los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf.')
print()

ultimate_revenue = mergedusersplans_df[mergedusersplans_df['plan_name'] == 'ultimate']['total_fee']
surf_revenue = mergedusersplans_df[mergedusersplans_df['plan_name'] == 'surf']['total_fee']

from scipy import stats

t_stat, p_value = stats.ttest_ind(ultimate_revenue, surf_revenue, equal_var=False) 

alpha = 0.05
print(f"T-statistic: {t_stat}, P-value: {p_value}")

if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
print()

print('Hipótesis nula, No hay diferencia en los ingresos totales entre los dos planes. Es decir, la media de los ingresos del plan ultimate es igual a la media de los ingresos del plan surf.')
print()
print('Hipotesis alternativa, Hay una diferencia en los ingresos totales entre los dos planes. Es decir, la media de los ingresos del plan ultimate no es igual a la media de los ingresos del plan surf.')
print()

subset_df = mergedusersplans_df[mergedusersplans_df['plan_name'].isin(['Ultimate', 'Surf'])]
ultimate_revenue = subset_df[subset_df['plan_name'] == 'Ultimate']['total_fee']
surf_revenue = subset_df[subset_df['plan_name'] == 'Surf']['total_fee']
t_stat, p_value = stats.ttest_ind(ultimate_revenue, surf_revenue, equal_var=False)
print(f'T-Statistic: {t_stat}')
print(f'P-Value: {p_value}')

if p_value < 0.05:
    print("Rechazamos la hipótesis nula: hay una diferencia significativa entre los ingresos promedio de los planes Ultimate y Surf.")
else:
    print("No rechazamos la hipótesis nula: no hay diferencia significativa entre los ingresos promedio de los planes Ultimate y Surf.")
print()

print('La hipótesis nula establece que no hay diferencia significativa en los ingresos promedio entre los dos grupos que estás comparando. Esto significa que los ingresos promedio de los planes Ultimate y Surf son iguales.')
print()
print('La hipótesis alternativa postula que sí hay una diferencia significativa en los ingresos promedio entre los dos grupos. Esto implica que los ingresos promedio de los planes Ultimate y Surf no son iguales.')
print()

print('Haciendo un analisis desde un princpio pudimos observar que debemos de examinar la informacion proporcionada para enriquecer los datos, esto se logra modificando columnas, datos, el tipo de estos para hacer operaciones, un mejor manejo y entendimiento de estos, una vez enriqueciendo los datos ya podemos hacer un analisis de estos, como ver mediante operaciones y graficos el comportamiento de los usuarios en cada uno de los planes, los meses en los que consumen mas y menos, que usuarios son nuestros mejores usuarios, en que se puede mejorar como empresa para justo retener a estos e invitar a mas a que lleguen a estos niveles que como')
