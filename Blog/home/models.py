from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


# we make a abstract base model whose table is not made in database
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True


class BlogModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blogmodel')
    title=models.CharField(max_length=500)
    blog_text=models.TextField()
    main_images=models.ImageField(upload_to='blogs')