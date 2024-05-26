from django.contrib.auth.models import User
from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_questions', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_questions', blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def toggle_like(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
        else:
            self.likes.add(user)
            self.dislikes.remove(user)  # Remove from dislikes if liked

    def toggle_dislike(self, user):
        if user in self.dislikes.all():
            self.dislikes.remove(user)
        else:
            self.dislikes.add(user)
            self.likes.remove(user)  # Remove from likes if disliked

    class Meta:
        verbose_name = 'события'
        verbose_name_plural = 'события'


class PhotoEvents(models.Model):
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/events/', null=True, blank=True)
    video = models.FileField(upload_to='videos/events/', null=True, blank=True)


class Relation(models.Model):
    RATE_CHOICES = (
        (1, 'жаман'),
        (2, 'жакшы'),
        (3, 'мыкты'),
    )


#class What_class(models.Model):
 #   title = models.CharField(max_length=5)


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middle_names = models.CharField(max_length=30)
    img = models.ImageField()
    teach = models.CharField(max_length=30)
    classroom_teacher = models.CharField(max_length=30)
    work_date = models.DateTimeField()


# for register
class UserProfile(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

#
# class Students(models.Model):
#     name = models.CharField(max_length=20)
#     surname = models.CharField(max_length=30)
#     middle_names = models.CharField(max_length=30)
#     img = models.ImageField()
#     what_class = models.ForeignKey(What_class, on_delete=models.CASCADE)
#     birth = models.DateTimeField()
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

