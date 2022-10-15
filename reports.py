import pandas as pd
import numpy as np
import random
import seaborn as sns 
import matplotlib.pyplot as plt
from time import sleep

path = 'cota-parlamentar.csv'
usable_fields = [
    'numano',
    'nummes',
    'txnomeparlamentar',
    'sgpartido',
    'sguf',
    'txtdescricao',
    'txtfornecedor',
    'vlrliquido'
]


class ExtractData():
    def _extract_data(self):
        pass

    def _get_data_frame(self):
        df = pd.read_csv(path)
        print(f"\nInfos database Original (linhas, colunas): {df.shape}")

        df_object = df[usable_fields]
        df_object['vlrliquido'] = df_object['vlrliquido'].abs()

        print(f"database\n {df_object}")
        print(f"\nLinhas NaN:\n {df_object.notna()}")
        print(f"\nInfos database (linhas, colunas): {df_object.shape}")

        df_object = self._clean_data(df_object)

        print(f"\nInfos database (linhas, colunas) após limpar linhas NaN: {df_object.shape}")
        print(f"\nTipos de dados:\n {df_object.dtypes}")

        return df_object

    def _clean_data(self, df):
        return df.dropna()

    def get_reports(self, df):

        party = random.choice(df.sgpartido.unique())
        year = int(random.choice(df.numano.unique()))
        state = random.choice(df.sguf.unique())

        spent_in_all_period = df.groupby('sgpartido')['vlrliquido'].mean()

        # Spent per political party in all periodo
        spent_per_political_party = df.loc[
            df['sgpartido'] == party
        ]

        # Spent per political party X in year X
        spent_per_political_party_year = df.loc[
            (df['sgpartido'] == party) &
            (df['numano'] == year)
        ]

        # Spent per political party X in year X and state X
        spent_per_political_party_year_state = df.loc[
            (df['sgpartido'] == party) &
            (df['numano'] == year) &
            (df['sguf'] == state)
        ]

        print(
            f"\n\nMédia de gastos por parlamentar: R${str(round(spent_per_political_party_year_state['vlrliquido'].mean(), 2))}"
            f"\nPartido: {party}"
            f"\nPeríodo: {year}"
            f"\nN° Parlamentares: {spent_per_political_party_year_state['txnomeparlamentar'].nunique()}"
            f"\nEstado:{state}")

        print(
            f"\n\nMédia de gastos por parlamentar: R${str(round(spent_per_political_party_year['vlrliquido'].mean(), 2))}"
            f"\nPartido: {party}"
            f"\nPeríodo: {year}"
            f"\nN° Parlamentares: {spent_per_political_party_year['txnomeparlamentar'].nunique()}"
            f"\nem todos os estados e Distrito Federal")

        print(
            f"\n\nMédia de gastos por parlamentar: R${str(round(spent_per_political_party['vlrliquido'].mean(), 2))}"
            f"\nPartido: {party}"
            f"\nN° Parlamentares: {spent_per_political_party['txnomeparlamentar'].nunique()}"
            f"\nPeríodo (2009-2020)")

        print(
            f"\n\nMédia de gastos por parlamentar:\n {spent_in_all_period}"
            f"\nN° Parlamentares: {df['txnomeparlamentar'].nunique()}"
            f"\nPeríodo (2009-2020)")


extractor = ExtractData()
df = extractor._get_data_frame()
print(f"\n\nPartidos disponíveis\n {sorted(df.sgpartido.unique())}")
print(f"\nAnos disponíveis\n {sorted(df.numano.unique())}")
print(f"\nUFs disponíveis\n {sorted(df.sguf.unique())}")

extractor.get_reports(df)

print(f"\n\n################## 14/10 ##########################")
# xf = df.loc[0:100]
# print(xf)
#anscombe = sns.df('anscombe')
# dataset_1 = df[df['sgpartido' == 'PSDB']]
#plt.scatter(xf['txnomeparlamentar'], xf['vlrliquido'])
plt.scatter(df['vlrliquido'], df['txnomeparlamentar'])
# plt.set_title("Governo")
# plt.set_xlabel("Nome")
# plt.set_xlabel("valor")
plt.show()
# fig = plt.figure()
# fig.show()
#sleep(60000)