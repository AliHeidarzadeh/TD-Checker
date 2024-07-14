import requests
import pandas as pd



class DDn():
    def DDn_F(Ddn_file):
        Ddf_Df = pd.read_excel(Ddn_file)
        Ddf_Df['نماد'] = Ddf_Df['نماد'].str.replace("ك","ک")
        Ddf_Df['نماد'] = Ddf_Df['نماد'].str.replace("ي","ی")
        Ddf_Df['نماد'] = Ddf_Df['نماد'].str.replace("ذ","")
        Ddf_Df['نماد'] = Ddf_Df['نماد'].str.replace("ژ","")
        Ddf_Df['نماد'] = Ddf_Df['نماد'].str.replace("گ","")
        global Ddn_Df
        Ddn_Df = Ddf_Df
class Rayan:
    def Rayan_F(Rayan_file):
        Df = pd.read_excel(Rayan_file)
        Df.columns = Df.iloc[4]
        Df.drop(Df.iloc[0:5].index,inplace=True)
        Df = Df[['نماد','مانده قابل فروش','قيمت روز']]
        Df['نماد'] = Df['نماد'].str.replace("ك","ک")
        Df['نماد'] = Df['نماد'].str.replace("ي","ی")
        Df['نماد'] = Df['نماد'].str.replace("ذ","")
        Df['قیمت Tse'] = 0
        Df['تعداد DDN'] = 0
        Df.to_excel("Df.xlsx")
        
class Tadbir:
    def tadbir_F(Tadbir_file):
        Df = pd.read_excel(Tadbir_file)
        Df.columns = Df.iloc[1]
        Df.drop(Df.iloc[0:2].index,inplace=True)
        Df = Df[['نام سهام','تعداد','قیمت روز']]
        Df.rename(columns={'نام سهام':'نماد','تعداد':'مانده قابل فروش','قیمت روز':'قيمت روز'},inplace=True)
        Df['نماد'] = Df['نماد'].str.replace("ك","ک")
        Df['نماد'] = Df['نماد'].str.replace("1","")
        Df['نماد'] = Df['نماد'].str.replace("ي","ی")
        Df['نماد'] = Df['نماد'].str.replace("ذ","")
        Df['قیمت Tse'] = 0
        Df['تعداد DDN'] = 0
        Df.to_excel("Df.xlsx")
        
class RequestsToTse:
    def requests():
        import requests
        Df = pd.read_excel("Df.xlsx")
        for i in range(len(Df.index) - 1):
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                Respons = requests.get(f"http://cdn.tsetmc.com/api/Instrument/GetInstrumentSearch/{Df['نماد'].iloc[i]}",headers=headers)
                print(Df['نماد'].iloc[i])
                Data = Respons.json()
                name = Data['instrumentSearch'][0]['insCode']
                Respons2 = requests.get(f'http://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceDailyList/{name}/0', headers=headers)
                df_history = pd.DataFrame(Respons2.json()['closingPriceDaily'])
                df_history = df_history[['dEven','priceMax','priceMin','pClosing','pDrCotVal','priceFirst','priceYesterday','qTotCap','qTotTran5J','zTotTran']]
                df_history.columns = ['Date','High','Low','Final','Close','Open','Y-Final','Value','Volume','No']
                df_history['Date'] = df_history['Date'].apply(lambda x: str(x))
                df_history['Date'] = df_history['Date'].apply(lambda x: f'{x[:4]}-{x[4:6]}-{x[-2:]}')
                df_history['Date']=pd.to_datetime(df_history['Date'])
                Close_Prise = df_history.iloc[0]['Close']
                Df['قیمت Tse'].iloc[i] = Close_Prise
            except:
                continue
        for i in range(len(Df.index) - 1):
                Data2 = Ddn_Df[Ddn_Df['نماد'] == Df['نماد'].iloc[i]]
                if Data2['نماد'].all() == Data2['نماد'].empty:
                    continue
                else:
                    Df['تعداد DDN'].iloc[i] = Data2['میزان دارایی قابل معامله'].iloc[0]
        Df.to_excel("result.xlsx")

