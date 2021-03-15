import json, csv, io
import xml.etree.cElementTree as elem #elem - element
import pandas as pd

class Convertising():
    def __init__(self, path):
        self.path = path
        file = open(f'products/{path}.json', 'r', encoding='utf-8')
        jason = file.read() # jason - json
        self.jason = json.loads(jason)
        file.close()
        
    def __str__(self): # This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object.
        clear_data = ''
        for row in self.jason:
            clear_data += (f'{row["id"]}. {row["imie_nazwisko_pracownika"]} | Adres Email: {row["email"]} | Numer Telefonu: {row["numer_telefonu"]} | Czy zatrudniony: {row["zatrudniony"]} |  Data Aplikacji: {row["data_aplikacji"]}\n')
        return clear_data
    
    def convert_csv(self):
        try:
            file2 = open(f'products/{self.path}.csv', 'w', newline='')
            output = csv.writer(file2)
            output.writerow(self.jason[0].keys())  # header row
            for row in self.jason:
                output.writerow(row.values())
            file2.close()
        except:
            pass
        
    def convert_xml(self):
  
        empls = elem.Element(str("employees")) #empls - employees
        for json_row in self.jason:
            empl = elem.SubElement(empls, str("employee")) #empl - employee
            elem.SubElement(empl,"id").text = str(json_row["id"])
            elem.SubElement(empl,"imie_nazwisko_pracownika").text = str(json_row["imie_nazwisko_pracownika"])
            elem.SubElement(empl,"email").text = str(json_row["email"])
            elem.SubElement(empl,"numer_telefonu").text = str(json_row["numer_telefonu"])
            elem.SubElement(empl,"zatrudniony").text = str(json_row["zatrudniony"])
            elem.SubElement(empl,"data_aplikacji").text = str(json_row["data_aplikacji"])

            tree = elem.ElementTree(empls)
            tree.write("plik.xml")

    def convert_xlsx(self):
        df = pd.DataFrame(self.jason)
        df.to_excel(f'products/{self.path}.xlsx')