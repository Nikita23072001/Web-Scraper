from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.ceneo.pl/96961305/opinie-1')
bs = BeautifulSoup(html.read(), 'html.parser')
naglowki = bs.find_all('h1')
opinie = bs.find_all(class_='js_product-reviews')
file = open('scrapped.json', 'a', encoding='utf-8')

for x in opinie:
    file.write(x.get_text())

file.close()

print(naglowki[0].get_text())




# <div class="product-top-2020__product-info__name-container">
#                     <h1 class="product-top-2020__product-info__name js_product-h1-link js_product-force-scroll js_searchInGoogleTooltip default-cursor" data-onselect="true" data-tooltip-autowidth="true" productlink="#"> Xiaomi Redmi Note 9 Pro 6/128GB Szary</h1>
#                     <div class="product-top-2020__product-info__icons">
#         <div class="price-history">
#                 <span class="link link--dark js_show-price-history-popup" data-google-action="GoTo_PrcHis" data-google-label="Button_scroll_PrcHis" data-hint="Historia cen">
#                     <span data-icon=""></span>
#                 </span>
#             <span class="context-help scoreHint" data-offset-x="0" data-offset-y="25" data-dtr="true">?<span class="hidden js_context-datahint">Historia cen dostępna jest po zalogowaniu się. Dzięki niej możesz sprawdzić aktualny trend cenowy, wzrost lub spadek ceny oraz sezonowe obniżki cen produktów.</span></span>
#         </div>
#         <span id="clipboard-toggle-93700228" data-category="Product - Add to Wishlist" data-action="Click Add Favorite - product" data-label="Smartfony" data-pid="93700228" data-cid="471" data-hint="Ulubione" class="add-to-favorite js_no-conv js_wishlist-toggle js_sa-wishlist-item js_gtm_wishlist-toggle "></span>
#     </div>
# </div>