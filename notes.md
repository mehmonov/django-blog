mvt 
model-view-template


model - database strukturasi 

view - loyiha mantiq -> 

    url  - routing - yo'naltirish 

template - userga ko'rinadigan 

mvc - model - view - controller



product.objects.all
product.objects.filter


# Maqola
1. title -> maqola nomi? 
2. subtitle -> maqolani qisqacha ta'rifi
3. content -> maqola matni
4. created_at  -> qachon yaratilgan 
5. views  -> nechta odam ko'rdi?
6. category -> qaysi yo'nalishdagi maqola?

# Comment 
1. user -> kim?
2. maqola - qaysi maqolaga?
3. vaqti - > qachon? 
4. adminReply - > admin nima dedi?  
5. status - > saytga ko'rinadimi? 

# Like
1. user -> kim?
2. maqola - qaysi maqolaga?

# Category
1. name -> bu qanaqa kategoriya? dasturlash, video montaj



pip install django-ckeditor

Add ckeditor to your INSTALLED_APPS setting.

from ckeditor.fields import RichTextField


    content = RichTextField()


STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Add the compressor.storage.CompressorFileStorage for production use
STATICFILES_STORAGE = 'compressor.storage.CompressorFileStorage' # Use this for offline compression

# Add compressor to STATICFILES_FINDERS
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
