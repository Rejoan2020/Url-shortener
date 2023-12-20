import string
import random
from django.conf import settings

SHORTCODE_MIN = getattr(settings,"MINSIZE",6)

def code_generator(size=SHORTCODE_MIN,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def short_url_generator(instance,size=6):
    new_code = code_generator(size=size)
    cls = instance.__class__
    does_exist_in_query_set = cls.objects.filter(short_url=new_code).exists()
    if does_exist_in_query_set:
        return short_url_generator(size=size)
    return new_code

def removewww(str):
    f = ""
    cnt = 0
    for i in str:
        if cnt>=7 or len(str)<=cnt:
            break
        f+=i
        cnt+=1
    cnt += 3
    for cnt in range(11,len(str)):
        f+=str[cnt]
    print(f)
    return f