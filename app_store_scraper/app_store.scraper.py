from app_store import AppStore
from pprint import pprint
import sys
import locale

print(sys.getfilesystemencoding())
print(locale.getpreferredencoding())

minecraft = AppStore(country="cn", app_name="小米商城-买齐全家智能好物",app_id="1024958046")
minecraft.review(how_many=10000)
with open('app.txt',mode='a+',encoding='utf8') as json_file:
    for string in minecraft.reviews:
        json_file.write(string['review'])
        json_file.write("\n")
# pprint(minecraft.reviews)
pprint(minecraft.reviews_count)