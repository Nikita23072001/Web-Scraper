import json, csv
import xml.etree.cElementTree as elem #elem - element

class Convertising():
    def __init__(self, path):
        file = open(path, 'r')
        jason = file.read() # jason - json
        self.jason = json.loads(jason)
        file.close()
        
    def __str__(self): # This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object.
        clear_data = ''
        for row in self.jason:
            clear_data += (f'{row["id"]}. {row["imie_nazwisko_pracownika"]} | Adres Email: {row["email"]} | Numer Telefonu: {row["numer_telefonu"]} | Czy zatrudniony: {row["zatrudniony"]} |  Data Aplikacji: {row["data_aplikacji"]}\n')
        return clear_data
    
    def convert_csv(self):
        
        file2 = open('plik.csv', 'w', newline='')
        output = csv.writer(file2)
        output.writerow(self.jason[0].keys())  # header row
        for row in self.jason:
            output.writerow(row.values())
        file2.close()
        
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
            
    def write_page(self):
        #html
        html = elem.Element('html')
        head = elem.Element('head')
        body = elem.Element('body')
        html.extend([head, body])

        #head
        elem.SubElement(head, 'title').text="Final Project"
        elem.SubElement(head, 'link', attrib={'rel':"preconnect", 'href':"https://fonts.gstatic.com"})
        elem.SubElement(head, 'link', attrib={'href':"https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap", 'rel':"stylesheet"})
        elem.SubElement(head, 'link', attrib={'href':"https://fonts.googleapis.com/css2?family=Aleo&display=swap", 'rel':"stylesheet"})
        elem.SubElement(head, 'link', attrib={'rel':"stylesheet", 'href':"css.css"})
        
        #body
        header = elem.Element('header')
        body.append(header)
        div = elem.Element('div', attrib={'id': 'menu'})
        header.append(div)
        elem.SubElement(header, 'h1', attrib={'class': 'title'}).text = 'Final Project'
        elem.SubElement(header, 'h2', attrib={'class': 'title'}).text = 'Computer Programming'

        #header -> div -> ul
        ul = elem.Element('ul')
        div.append(ul)
        li1 = elem.Element('li')
        li2 = elem.Element('li')
        li3 = elem.Element('li')
        li4 = elem.Element('li')
        ul.extend([li1, li2, li3, li4])
        elem.SubElement(li1, 'a', attrib={'href': '#o_nas'}).text = 'O NAS'
        elem.SubElement(li2, 'a', attrib={'href': '#szczegoly'}).text = 'SZCZEGÓŁY'
        elem.SubElement(li3, 'a', attrib={'href': '#informacje'}).text = 'INFORMACJE'
        elem.SubElement(li4, 'a', attrib={'href': '#pliki'}).text = 'PLIKI'

        #section
        section1 = elem.Element('section', attrib={'id': 'about'})
        body.append(section1)
        h1 = elem.Element('h1', attrib={'class': 'nagl'})
        elem.SubElement(h1, 'a', attrib={'id': 'o_nas'}).text = 'O NAS'

        #hr - deklaracja
        hr = elem.Element('hr')
        section1.extend([h1,hr])

        #br - deklaracja
        br = elem.Element('br')
        
        table = elem.Element('table', attrib={'id': 'pierwsza'})
        section1.append(table)
        td1 = elem.Element('td')
        td2 = elem.Element('td')
        td3 = elem.Element('td')
        table.extend([td1, td2, td3])

        elem.SubElement(td1, 'p').text = 'Nichita Gordinschii'
        elem.SubElement(td1, 'p').text = '218981'
        elem.SubElement(td2, 'p').text = 'Dominik Brożyna'
        elem.SubElement(td2, 'p').text = '219297'
        elem.SubElement(td2, 'p').text = 'TEAM LEADER'
        elem.SubElement(td3, 'p').text = 'Viktoriia Dolhova'
        elem.SubElement(td3, 'p').text = '218105'
        
        body.append(br) #zadaklarowane wyzej

        #section
        section2 = elem.Element('section', attrib={'id': 'details'})
        body.append(section2)

        h2 = elem.Element('h1', attrib={'class':'nagl'})
        elem.SubElement(h2, 'a', attrib={'id': 'szczegoly'}).text = "SZCZEGÓŁY PROJEKTU"

        section2.extend([h2, hr]) # hr zadaklarowane wyzej

        #ul
        ul5 = elem.Element('ul', attrib={'style': 'float:left; width:50%; padding-top:50px'})
        elem.SubElement(ul5, 'li').text = 'Projekt polega na pobraniu odpowiedniej bazy danych w postaci JSONa, pozniej przeformatowaniu pliku na format CSV oraz XML.'
        elem.SubElement(ul5, 'li').text = 'Zespół za każdym razem, gdy plik jest zmieniany na inny format, powinien wyświetlić go w czytelnej postaci.'
        elem.SubElement(ul5, 'li').text = 'Wszystkie działania muszą być wykonane za pomocą języka programowania Python.'

        #ul
        ul6 = elem.Element('ul', attrib={'style': 'float:right; width:50%; padding-top:20px'})
        elem.SubElement(ul6, 'li').text = 'Jedną z ostatnich czynności, które zespół ma wykonać, jest tworzenie pliku HTML, gdzie będą umieszczone informacje, dotyczące właśnie członków zespołu, projektu, danych oraz same dane w 3 postaciach.'
        elem.SubElement(ul6, 'li').text = 'Po zrobieniu wyżej wymienionych podpunktów, zespół projektowy ma za zadanie nagrać wideoprezentację, która potrwa od 9 do 10 minut i zaprezentować swój projekt.'
        
        section2.extend([ul5, ul6])

        #section
        section3 = elem.Element('section', attrib={'id': 'dane'})
        body.append(section3)

        table2 = elem.Element('table', attrib={'id':'druga'})

        td4 = elem.Element('td')
        mar = elem.Element('marquee', attrib={'direction':"right", 'width':"350px"})
        h3 = elem.Element('h1', attrib={'class':'nagl'})
        mar.append(h3)
        elem.SubElement(h3, 'a', attrib={'id':'informacje'}).text = 'Czego dotyczą dane?'
        td4.extend([mar, hr])

        td5 = elem.Element('td', attrib={'id':'ff'})
        elem.SubElement(td5, "p").text = 'Baza danych składa się ze 100 osób, którzy są zainteresowani ofertą pracy. W pliku możemy zobaczyć imie i nazwisko każdego z nich, e-mail oraz numer telefonu, który jest nam potrzebny do komunikacji z osobą, informacje o tym, czy zostali zatrudnieni i data aplikacji.'
        
        table2.extend([td4,td5])
        section3.append(table2)
        
        #dane z jsona
        table3 = elem.Element(str("table"), attrib={'id': 'data'})

        #naglowki
        heading = elem.SubElement(table3, str("tr"))
        elem.SubElement(heading,"th").text = "id"
        elem.SubElement(heading,"th").text = "imie_nazwisko_pracownika"
        elem.SubElement(heading,"th").text = "email"
        elem.SubElement(heading,"th").text = "numer_telefonu"
        elem.SubElement(heading,"th").text = "zatrudniony"
        elem.SubElement(heading,"th").text = "data_aplikacji"

        #wiersze
        for json_row in self.jason:

            table_row = elem.SubElement(table3, str("tr"))
        
            elem.SubElement(table_row,"td").text = str(json_row["id"])
            elem.SubElement(table_row,"td").text = str(json_row["imie_nazwisko_pracownika"])
            elem.SubElement(table_row,"td").text = str(json_row["email"])
            elem.SubElement(table_row,"td").text = str(json_row["numer_telefonu"])
            elem.SubElement(table_row,"td").text = str(json_row["zatrudniony"])
            elem.SubElement(table_row,"td").text = str(json_row["data_aplikacji"])
            
        section3.append(table3)
        
        #zapis do html
        elem.ElementTree(html).write('index.html', encoding='utf-8', method='html')
        
        #css
        css_code = """
                body {
                    margin: 0%;
                }

                header {
                    width: 100%;
                    height: 300px;
                }
                        
                #menu {
                    color: black;
                    font-family: 'Aleo', serif;
                    font-size: 20px;
                    text-decoration: none;
                }

                #menu ul {
                    display: table;
                    width: 100%;
                    margin: 0;
                    padding: 0;
                }

                #menu li {
                    display: table-cell;
                    background: #6b99a3;
                    color: white;
                    text-align: center;
                    text-decoration: none;
                    font-weight: bold;
                }

                #menu li :hover {
                    color: white;
                }

                #menu a {
                    line-height: 70px;
                    display: block;
                    text-decoration: none;
                    color: black;
                    border-radius: 3px;
                }

                #about {
                   text-align: center; 
                   font-family: 'Aleo', serif;
                }

                .nagl {
                    font-size: 30px;
                    text-align: center;
                }

                hr {
                    width: 50%;
                    background-color: #3c95a8;
                }

                #pierwsza {
                    width: 100%;
                    height: 300px;
                    margin: 0 auto;
                    font-size: 18px;
                    text-align: center;
                }

                #pierwsza td:hover {
                    background-color: #ffa46b;
                    transition: 0.7s;
                    color: white;
                    font-size: 23px;
                }

                #details {
                    width: 80%;
                    padding-left: 150px;
                    text-align: center;
                    font-family: 'Aleo', serif;
                }

                #druga {
                    width: 100%;
                    height: 300px;
                    margin: 0 auto;
                    padding-top: 100px;
                    font-size: 18px;
                    text-align: center;
                    font-family: 'Aleo', serif;
                }

                #druga td {
                    width: 50%;
                }

                #ff {
                    background-color: #3c95a8;
                }

                #dane {
                    width: 80%;
                    padding-left: 150px;
                    padding-top: 100px;
                    text-align: center;
                    font-family: 'Aleo', serif;
                }

                #trzecia {
                    width: 100%;
                    height: auto;
                    padding-top: 30px;
                    margin: 0 auto;
                    font-size: 18px;
                    border: 2px solid black;
                }
                
                #dane1 {
                    padding-right: 50px;
                }    
                h1.title {
                    margin-left:12%;
                    margin-bottom:0;
                    font-family: 'Roboto';
                    font-size:500%;
                }
                h2.title {
                    margin-left:23%;
                    font-family: 'Roboto';
                }
                #data {
                    margin: 30px auto;
                }
                """
        
        css = open('css.css', 'w', encoding='utf-8')
        css.write(css_code)
        css.close()