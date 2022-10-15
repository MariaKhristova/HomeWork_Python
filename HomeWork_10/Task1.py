#Программа получает данные о курсе доллара из ЦБ РФ и стоит график от начала текущего года
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import requests
import xml.etree.ElementTree as ET

# today = datetime.today()
# url = f'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/{today.year}&date_req2={today.day:02d}/{today.month:02d}/{today.year}&VAL_NM_RQ=R01235'
#
# res = requests.get(url)
# res_xml = res.text

res_xml = '<?xml version="1.0" encoding="windows-1251"?><ValCurs ID="R01235" DateRange1="01.01.2022" DateRange2="15.10.2022" name="Foreign Currency Market Dynamic"><Record Date="11.01.2022" Id="R01235"><Nominal>1</Nominal><Value>75,1315</Value></Record><Record Date="12.01.2022" Id="R01235"><Nominal>1</Nominal><Value>74,8355</Value></Record><Record Date="13.01.2022" Id="R01235"><Nominal>1</Nominal><Value>74,5277</Value></Record><Record Date="14.01.2022" Id="R01235"><Nominal>1</Nominal><Value>74,5686</Value></Record><Record Date="15.01.2022" Id="R01235"><Nominal>1</Nominal><Value>75,7668</Value></Record><Record Date="18.01.2022" Id="R01235"><Nominal>1</Nominal><Value>76,0404</Value></Record><Record Date="19.01.2022" Id="R01235"><Nominal>1</Nominal><Value>76,3347</Value></Record><Record Date="20.01.2022" Id="R01235"><Nominal>1</Nominal><Value>76,8697</Value></Record><Record Date="21.01.2022" Id="R01235"><Nominal>1</Nominal><Value>76,4408</Value></Record><Record Date="22.01.2022" Id="R01235"><Nominal>1</Nominal><Value>76,6903</Value></Record><Record Date="25.01.2022" Id="R01235"><Nominal>1</Nominal><Value>77,3649</Value></Record><Record Date="26.01.2022" Id="R01235"><Nominal>1</Nominal><Value>78,6422</Value></Record><Record Date="27.01.2022" Id="R01235"><Nominal>1</Nominal><Value>78,9437</Value></Record><Record Date="28.01.2022" Id="R01235"><Nominal>1</Nominal><Value>78,9470</Value></Record><Record Date="29.01.2022" Id="R01235"><Nominal>1</Nominal><Value>77,8174</Value></Record><Record Date="01.02.2022" Id="R01235"><Nominal>1</Nominal><Value>77,4702</Value></Record><Record Date="02.02.2022" Id="R01235"><Nominal>1</Nominal><Value>77,1302</Value></Record><Record Date="03.02.2022" Id="R01235"><Nominal>1</Nominal><Value>76,4849</Value></Record><Record Date="04.02.2022" Id="R01235"><Nominal>1</Nominal><Value>76,6501</Value></Record><Record Date="05.02.2022" Id="R01235"><Nominal>1</Nominal><Value>76,0509</Value></Record><Record Date="08.02.2022" Id="R01235"><Nominal>1</Nominal><Value>75,6806</Value></Record><Record Date="09.02.2022" Id="R01235"><Nominal>1</Nominal><Value>75,3042</Value></Record><Record Date="10.02.2022" Id="R01235"><Nominal>1</Nominal><Value>74,8015</Value></Record><Record Date="11.02.2022" Id="R01235"><Nominal>1</Nominal><Value>74,7241</Value></Record><Record Date="12.02.2022" Id="R01235"><Nominal>1</Nominal><Value>74,9867</Value></Record><Record Date="15.02.2022" Id="R01235"><Nominal>1</Nominal><Value>76,5762</Value></Record><Record Date="16.02.2022" Id="R01235"><Nominal>1</Nominal><Value>76,1660</Value></Record><Record Date="17.02.2022" Id="R01235"><Nominal>1</Nominal><Value>75,0141</Value></Record><Record Date="18.02.2022" Id="R01235"><Nominal>1</Nominal><Value>75,7527</Value></Record><Record Date="19.02.2022" Id="R01235"><Nominal>1</Nominal><Value>75,7619</Value></Record><Record Date="22.02.2022" Id="R01235"><Nominal>1</Nominal><Value>76,7671</Value></Record><Record Date="23.02.2022" Id="R01235"><Nominal>1</Nominal><Value>80,4194</Value></Record><Record Date="25.02.2022" Id="R01235"><Nominal>1</Nominal><Value>86,9288</Value></Record><Record Date="26.02.2022" Id="R01235"><Nominal>1</Nominal><Value>83,5485</Value></Record><Record Date="01.03.2022" Id="R01235"><Nominal>1</Nominal><Value>93,5589</Value></Record><Record Date="02.03.2022" Id="R01235"><Nominal>1</Nominal><Value>91,7457</Value></Record><Record Date="03.03.2022" Id="R01235"><Nominal>1</Nominal><Value>103,2487</Value></Record><Record Date="04.03.2022" Id="R01235"><Nominal>1</Nominal><Value>111,7564</Value></Record><Record Date="05.03.2022" Id="R01235"><Nominal>1</Nominal><Value>105,8124</Value></Record><Record Date="06.03.2022" Id="R01235"><Nominal>1</Nominal><Value>105,8124</Value></Record><Record Date="10.03.2022" Id="R01235"><Nominal>1</Nominal><Value>116,0847</Value></Record><Record Date="11.03.2022" Id="R01235"><Nominal>1</Nominal><Value>120,3785</Value></Record><Record Date="12.03.2022" Id="R01235"><Nominal>1</Nominal><Value>116,7517</Value></Record><Record Date="15.03.2022" Id="R01235"><Nominal>1</Nominal><Value>115,1963</Value></Record><Record Date="16.03.2022" Id="R01235"><Nominal>1</Nominal><Value>111,4823</Value></Record><Record Date="17.03.2022" Id="R01235"><Nominal>1</Nominal><Value>108,0521</Value></Record><Record Date="18.03.2022" Id="R01235"><Nominal>1</Nominal><Value>104,8012</Value></Record><Record Date="19.03.2022" Id="R01235"><Nominal>1</Nominal><Value>103,9524</Value></Record><Record Date="22.03.2022" Id="R01235"><Nominal>1</Nominal><Value>104,6819</Value></Record><Record Date="23.03.2022" Id="R01235"><Nominal>1</Nominal><Value>104,0741</Value></Record><Record Date="24.03.2022" Id="R01235"><Nominal>1</Nominal><Value>103,1618</Value></Record><Record Date="25.03.2022" Id="R01235"><Nominal>1</Nominal><Value>96,0458</Value></Record><Record Date="26.03.2022" Id="R01235"><Nominal>1</Nominal><Value>95,6618</Value></Record><Record Date="29.03.2022" Id="R01235"><Nominal>1</Nominal><Value>93,7125</Value></Record><Record Date="30.03.2022" Id="R01235"><Nominal>1</Nominal><Value>86,2843</Value></Record><Record Date="31.03.2022" Id="R01235"><Nominal>1</Nominal><Value>84,0851</Value></Record><Record Date="01.04.2022" Id="R01235"><Nominal>1</Nominal><Value>83,4097</Value></Record><Record Date="02.04.2022" Id="R01235"><Nominal>1</Nominal><Value>83,4285</Value></Record><Record Date="05.04.2022" Id="R01235"><Nominal>1</Nominal><Value>83,5932</Value></Record><Record Date="06.04.2022" Id="R01235"><Nominal>1</Nominal><Value>83,3520</Value></Record><Record Date="07.04.2022" Id="R01235"><Nominal>1</Nominal><Value>82,5962</Value></Record><Record Date="08.04.2022" Id="R01235"><Nominal>1</Nominal><Value>76,2547</Value></Record><Record Date="09.04.2022" Id="R01235"><Nominal>1</Nominal><Value>74,8501</Value></Record><Record Date="12.04.2022" Id="R01235"><Nominal>1</Nominal><Value>79,1596</Value></Record><Record Date="13.04.2022" Id="R01235"><Nominal>1</Nominal><Value>79,6274</Value></Record><Record Date="14.04.2022" Id="R01235"><Nominal>1</Nominal><Value>79,8471</Value></Record><Record Date="15.04.2022" Id="R01235"><Nominal>1</Nominal><Value>81,2880</Value></Record><Record Date="16.04.2022" Id="R01235"><Nominal>1</Nominal><Value>80,0437</Value></Record><Record Date="19.04.2022" Id="R01235"><Nominal>1</Nominal><Value>79,4529</Value></Record><Record Date="20.04.2022" Id="R01235"><Nominal>1</Nominal><Value>79,0287</Value></Record><Record Date="21.04.2022" Id="R01235"><Nominal>1</Nominal><Value>77,0809</Value></Record><Record Date="22.04.2022" Id="R01235"><Nominal>1</Nominal><Value>74,9990</Value></Record><Record Date="23.04.2022" Id="R01235"><Nominal>1</Nominal><Value>73,5050</Value></Record><Record Date="26.04.2022" Id="R01235"><Nominal>1</Nominal><Value>73,3611</Value></Record><Record Date="27.04.2022" Id="R01235"><Nominal>1</Nominal><Value>72,7089</Value></Record><Record Date="28.04.2022" Id="R01235"><Nominal>1</Nominal><Value>72,8764</Value></Record><Record Date="29.04.2022" Id="R01235"><Nominal>1</Nominal><Value>72,2953</Value></Record><Record Date="30.04.2022" Id="R01235"><Nominal>1</Nominal><Value>71,0237</Value></Record><Record Date="05.05.2022" Id="R01235"><Nominal>1</Nominal><Value>69,4160</Value></Record><Record Date="06.05.2022" Id="R01235"><Nominal>1</Nominal><Value>66,2378</Value></Record><Record Date="07.05.2022" Id="R01235"><Nominal>1</Nominal><Value>67,3843</Value></Record><Record Date="12.05.2022" Id="R01235"><Nominal>1</Nominal><Value>68,8389</Value></Record><Record Date="13.05.2022" Id="R01235"><Nominal>1</Nominal><Value>65,7916</Value></Record><Record Date="14.05.2022" Id="R01235"><Nominal>1</Nominal><Value>63,7799</Value></Record><Record Date="17.05.2022" Id="R01235"><Nominal>1</Nominal><Value>63,4445</Value></Record><Record Date="18.05.2022" Id="R01235"><Nominal>1</Nominal><Value>63,5428</Value></Record><Record Date="19.05.2022" Id="R01235"><Nominal>1</Nominal><Value>63,5643</Value></Record><Record Date="20.05.2022" Id="R01235"><Nominal>1</Nominal><Value>62,4031</Value></Record><Record Date="21.05.2022" Id="R01235"><Nominal>1</Nominal><Value>58,8862</Value></Record><Record Date="24.05.2022" Id="R01235"><Nominal>1</Nominal><Value>58,2087</Value></Record><Record Date="25.05.2022" Id="R01235"><Nominal>1</Nominal><Value>56,9690</Value></Record><Record Date="26.05.2022" Id="R01235"><Nominal>1</Nominal><Value>56,2996</Value></Record><Record Date="27.05.2022" Id="R01235"><Nominal>1</Nominal><Value>62,0495</Value></Record><Record Date="28.05.2022" Id="R01235"><Nominal>1</Nominal><Value>66,4029</Value></Record><Record Date="31.05.2022" Id="R01235"><Nominal>1</Nominal><Value>63,0975</Value></Record><Record Date="01.06.2022" Id="R01235"><Nominal>1</Nominal><Value>61,6069</Value></Record><Record Date="02.06.2022" Id="R01235"><Nominal>1</Nominal><Value>61,4733</Value></Record><Record Date="03.06.2022" Id="R01235"><Nominal>1</Nominal><Value>61,5750</Value></Record><Record Date="04.06.2022" Id="R01235"><Nominal>1</Nominal><Value>61,9659</Value></Record><Record Date="07.06.2022" Id="R01235"><Nominal>1</Nominal><Value>61,1094</Value></Record><Record Date="08.06.2022" Id="R01235"><Nominal>1</Nominal><Value>60,9565</Value></Record><Record Date="09.06.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2282</Value></Record><Record Date="10.06.2022" Id="R01235"><Nominal>1</Nominal><Value>58,3895</Value></Record><Record Date="11.06.2022" Id="R01235"><Nominal>1</Nominal><Value>57,7780</Value></Record><Record Date="15.06.2022" Id="R01235"><Nominal>1</Nominal><Value>57,0926</Value></Record><Record Date="16.06.2022" Id="R01235"><Nominal>1</Nominal><Value>56,6624</Value></Record><Record Date="17.06.2022" Id="R01235"><Nominal>1</Nominal><Value>56,8691</Value></Record><Record Date="18.06.2022" Id="R01235"><Nominal>1</Nominal><Value>56,7101</Value></Record><Record Date="21.06.2022" Id="R01235"><Nominal>1</Nominal><Value>56,1727</Value></Record><Record Date="22.06.2022" Id="R01235"><Nominal>1</Nominal><Value>54,7081</Value></Record><Record Date="23.06.2022" Id="R01235"><Nominal>1</Nominal><Value>53,2788</Value></Record><Record Date="24.06.2022" Id="R01235"><Nominal>1</Nominal><Value>53,3578</Value></Record><Record Date="25.06.2022" Id="R01235"><Nominal>1</Nominal><Value>53,3234</Value></Record><Record Date="28.06.2022" Id="R01235"><Nominal>1</Nominal><Value>53,3641</Value></Record><Record Date="29.06.2022" Id="R01235"><Nominal>1</Nominal><Value>52,9699</Value></Record><Record Date="30.06.2022" Id="R01235"><Nominal>1</Nominal><Value>51,1580</Value></Record><Record Date="01.07.2022" Id="R01235"><Nominal>1</Nominal><Value>52,5123</Value></Record><Record Date="02.07.2022" Id="R01235"><Nominal>1</Nominal><Value>53,7676</Value></Record><Record Date="05.07.2022" Id="R01235"><Nominal>1</Nominal><Value>55,0858</Value></Record><Record Date="06.07.2022" Id="R01235"><Nominal>1</Nominal><Value>58,5118</Value></Record><Record Date="07.07.2022" Id="R01235"><Nominal>1</Nominal><Value>62,9110</Value></Record><Record Date="08.07.2022" Id="R01235"><Nominal>1</Nominal><Value>63,1427</Value></Record><Record Date="09.07.2022" Id="R01235"><Nominal>1</Nominal><Value>61,2664</Value></Record><Record Date="12.07.2022" Id="R01235"><Nominal>1</Nominal><Value>61,3045</Value></Record><Record Date="13.07.2022" Id="R01235"><Nominal>1</Nominal><Value>58,8541</Value></Record><Record Date="14.07.2022" Id="R01235"><Nominal>1</Nominal><Value>58,5322</Value></Record><Record Date="15.07.2022" Id="R01235"><Nominal>1</Nominal><Value>58,2568</Value></Record><Record Date="16.07.2022" Id="R01235"><Nominal>1</Nominal><Value>57,8323</Value></Record><Record Date="19.07.2022" Id="R01235"><Nominal>1</Nominal><Value>56,5616</Value></Record><Record Date="20.07.2022" Id="R01235"><Nominal>1</Nominal><Value>55,4370</Value></Record><Record Date="21.07.2022" Id="R01235"><Nominal>1</Nominal><Value>54,8491</Value></Record><Record Date="22.07.2022" Id="R01235"><Nominal>1</Nominal><Value>56,4783</Value></Record><Record Date="23.07.2022" Id="R01235"><Nominal>1</Nominal><Value>57,3917</Value></Record><Record Date="26.07.2022" Id="R01235"><Nominal>1</Nominal><Value>57,7821</Value></Record><Record Date="27.07.2022" Id="R01235"><Nominal>1</Nominal><Value>58,6605</Value></Record><Record Date="28.07.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2198</Value></Record><Record Date="29.07.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2031</Value></Record><Record Date="30.07.2022" Id="R01235"><Nominal>1</Nominal><Value>61,3101</Value></Record><Record Date="02.08.2022" Id="R01235"><Nominal>1</Nominal><Value>62,0506</Value></Record><Record Date="03.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,1595</Value></Record><Record Date="04.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2374</Value></Record><Record Date="05.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2580</Value></Record><Record Date="06.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,3696</Value></Record><Record Date="09.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,3164</Value></Record><Record Date="10.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,3814</Value></Record><Record Date="11.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,4542</Value></Record><Record Date="12.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,6229</Value></Record><Record Date="13.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,8993</Value></Record><Record Date="16.08.2022" Id="R01235"><Nominal>1</Nominal><Value>61,3747</Value></Record><Record Date="17.08.2022" Id="R01235"><Nominal>1</Nominal><Value>61,4247</Value></Record><Record Date="18.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,7552</Value></Record><Record Date="19.08.2022" Id="R01235"><Nominal>1</Nominal><Value>59,9570</Value></Record><Record Date="20.08.2022" Id="R01235"><Nominal>1</Nominal><Value>59,1321</Value></Record><Record Date="23.08.2022" Id="R01235"><Nominal>1</Nominal><Value>59,7419</Value></Record><Record Date="24.08.2022" Id="R01235"><Nominal>1</Nominal><Value>59,8963</Value></Record><Record Date="25.08.2022" Id="R01235"><Nominal>1</Nominal><Value>59,9974</Value></Record><Record Date="26.08.2022" Id="R01235"><Nominal>1</Nominal><Value>59,7699</Value></Record><Record Date="27.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,0924</Value></Record><Record Date="30.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,3636</Value></Record><Record Date="31.08.2022" Id="R01235"><Nominal>1</Nominal><Value>60,3677</Value></Record><Record Date="01.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2386</Value></Record><Record Date="02.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2370</Value></Record><Record Date="03.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,3713</Value></Record><Record Date="06.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,9033</Value></Record><Record Date="07.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,8544</Value></Record><Record Date="08.09.2022" Id="R01235"><Nominal>1</Nominal><Value>61,1814</Value></Record><Record Date="09.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,8010</Value></Record><Record Date="10.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,4696</Value></Record><Record Date="13.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,4568</Value></Record><Record Date="14.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,0676</Value></Record><Record Date="15.09.2022" Id="R01235"><Nominal>1</Nominal><Value>59,7751</Value></Record><Record Date="16.09.2022" Id="R01235"><Nominal>1</Nominal><Value>59,6663</Value></Record><Record Date="17.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,0316</Value></Record><Record Date="20.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,1662</Value></Record><Record Date="21.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,0158</Value></Record><Record Date="22.09.2022" Id="R01235"><Nominal>1</Nominal><Value>60,8685</Value></Record><Record Date="23.09.2022" Id="R01235"><Nominal>1</Nominal><Value>59,8318</Value></Record><Record Date="24.09.2022" Id="R01235"><Nominal>1</Nominal><Value>58,1006</Value></Record><Record Date="27.09.2022" Id="R01235"><Nominal>1</Nominal><Value>57,9990</Value></Record><Record Date="28.09.2022" Id="R01235"><Nominal>1</Nominal><Value>58,1756</Value></Record><Record Date="29.09.2022" Id="R01235"><Nominal>1</Nominal><Value>58,4485</Value></Record><Record Date="30.09.2022" Id="R01235"><Nominal>1</Nominal><Value>57,4130</Value></Record><Record Date="01.10.2022" Id="R01235"><Nominal>1</Nominal><Value>55,2987</Value></Record><Record Date="04.10.2022" Id="R01235"><Nominal>1</Nominal><Value>57,5664</Value></Record><Record Date="05.10.2022" Id="R01235"><Nominal>1</Nominal><Value>58,7913</Value></Record><Record Date="06.10.2022" Id="R01235"><Nominal>1</Nominal><Value>59,4043</Value></Record><Record Date="07.10.2022" Id="R01235"><Nominal>1</Nominal><Value>60,2534</Value></Record><Record Date="08.10.2022" Id="R01235"><Nominal>1</Nominal><Value>61,2475</Value></Record><Record Date="11.10.2022" Id="R01235"><Nominal>1</Nominal><Value>62,3126</Value></Record><Record Date="12.10.2022" Id="R01235"><Nominal>1</Nominal><Value>63,6840</Value></Record><Record Date="13.10.2022" Id="R01235"><Nominal>1</Nominal><Value>63,7559</Value></Record><Record Date="14.10.2022" Id="R01235"><Nominal>1</Nominal><Value>63,4917</Value></Record><Record Date="15.10.2022" Id="R01235"><Nominal>1</Nominal><Value>63,0558</Value></Record></ValCurs>'

arr = []
arr2 = []
tree = ET.fromstring(res_xml)
for element in tree:
    val = element[1]
    arr.append(float(val.text.replace(',', '.')))
    dat = datetime.strptime(element.attrib['Date'], '%d.%m.%Y')
    arr2.append(dat)


print(arr2)

y = np.array(arr)
x = np.array(arr2)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.title("Курс доллара от начала года")
plt.xlabel("Дата")
plt.ylabel("руб.")
plt.grid()

plt.show()
