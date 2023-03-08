import pandas as pd

import os

filename = 'finanzas2020.csv'

def ingresos(): 
    mask = df > 0
    return df[mask].sum()
  
def gastos(): 
    mask = df < 0
    return df[mask].sum()

def ahorro():
    return gastos()+ingresos()

df_mensual = pd.DataFrame(columns=['Gasto','Ingreso','Ahorro'])

try:
    df = pd.read_csv(os.path.join('data',filename),sep='\t')
    assert len(df.columns) == 12, 'La tabla no tiene 12 columnas'
    for column in df.columns:
        assert df[column].empty == False, f'La columna {column} está vacía'
        if df[column].dtypes == 'object':
            try:
                df[column] = pd.to_numeric(df[column], downcast="float")
            except:
                df[column] = df[column].replace("'", value="", regex=True)
                try:
                    df[column] = pd.to_numeric(df[column], downcast="float")
                except:
                    df[column] = df[column].str.replace(r'[a-z]','0',regex=True)
                    df[column] = pd.to_numeric(df[column], downcast="float")

    df_mensual['Ingreso'] = ingresos().transpose()
    df_mensual['Gasto'] = gastos().transpose()
    df_mensual['Ahorro'] = ahorro().transpose()

    print('1. Mes con mayor gasto: ',df_mensual['Gasto'].idxmin())
    print('2. Mes con mayor ahorro: ',df_mensual['Ahorro'].idxmax())
    print('3. Media anual de gastos: ',df_mensual['Gasto'].mean())
    print('4. Gasto anual: ',df_mensual['Gasto'].sum())
    print('5. Ingreso anual: ',df_mensual['Ingreso'].sum())
    
    print(df_mensual)
    
    grafica = df_mensual['Ingreso'].plot(kind='line',figsize=(20, 16), fontsize=26).get_figure()
    grafica.savefig(os.path.join('data','plot.png'))



    

                    
except FileNotFoundError:
    print(f'Por favor, comprueba que el existe el archivo {filename} en la carpeta data')

