from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_description = models.TextField()
    article_published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.article_published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.article_title

class Quest(models.Model):
	quest_title = models.CharField(max_length=200)
	spb = 'SP'
	quest_city_choices = ((spb, 'Санкт-Петербург'),)
	quest_city = models.CharField(max_length=2, choices=quest_city_choices, default=spb,)
	classical_quest = 'Классический квест'
	quest_excursion = 'Квест-экскурсия'
	auto_quest = 'Авто-квест'
	quest_type_choices = (
		(classical_quest, 'Классический квест'),
		(quest_excursion, 'Квест-экскурсия'),
		(auto_quest, 'Авто-квест'),
	)
	quest_type = models.CharField(max_length=200, choices=quest_type_choices, default=quest_excursion,)
	easy = 'Легко'
	medium = 'Средне'
	hard = 'Сложно'
	complexity_choices = (
		(easy, 'Легко'),
		(medium, 'Средне'),
		(hard, 'Сложно'),
	)
	complexity = models.CharField(max_length=200, choices=complexity_choices, default=easy,)
	min_players = models.IntegerField()
	max_players = models.IntegerField()
	quest_text = models.TextField(blank=True, null=True)
	quest_description = models.TextField(blank=True, null=True)
	votes = models.IntegerField(default=0)
	quest_cover = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')
	quest_author = models.CharField(max_length=200, default='admin')

	def vote(self):
		self.votes = self.votes + 1
		self.save()

	def __str__(self):
		return self.quest_title

class Stage(models.Model):
	stage_quest = models.ForeignKey('questscreed.Quest', related_name='stages')
	stage_title = models.CharField(max_length=200)
	question_with_choice = 'QWC'
	question_with_answer = 'QWA'
	question_with_picture = 'QWP'
	question_with_location = 'QWE'
	question_type_choices = (
		(question_with_choice, 'Задание с выбором ответа'),
		(question_with_answer, 'Задание со свободным вводом ответа'),
		(question_with_picture, 'Задание с отправлением изображения'),
		(question_with_location, 'Задание на определение соответствия'),
	)
	question_type = models.CharField(max_length=3, choices=question_type_choices, default=question_with_choice,)
	stage_question = models.TextField()
	answer_choice_1 = models.CharField(max_length=200, null=True, blank=True)
	answer_choice_2 = models.CharField(max_length=200, null=True, blank=True)
	answer_choice_3 = models.CharField(max_length=200, null=True, blank=True)
	answer_choice_4 = models.CharField(max_length=200, null=True, blank=True)
	answer_variant_1 = models.CharField(max_length=200, null=True, blank=True)
	answer_variant_2 = models.CharField(max_length=200, null=True, blank=True)
	answer_variant_3 = models.CharField(max_length=200, null=True, blank=True)
	answer_variant_4 = models.CharField(max_length=200, null=True, blank=True)
	answer_text = models.TextField(null=True, blank=True)
	answer_right_choice = models.CharField(max_length=200, null=True, blank=True)
	hint = models.TextField()
	stage_number = models.IntegerField(default=1)
	stage_cover = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')

	def __str__(self):
		return self.stage_title

class Commoncomment(models.Model):
    common_comment_author = models.CharField(max_length=200)
    common_comment_text = models.TextField()
    common_comment_created_date = models.DateTimeField(default=timezone.now)
    common_comment_approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.common_comment_approved_comment = True
        self.save()

    def __str__(self):
        return self.common_comment_text

class Comment(models.Model):
	comment_quest = models.ForeignKey('questscreed.Quest', related_name='comments', blank=True, null=True)
	comment_author = models.CharField(max_length=200)
	comment_text = models.TextField()
	comment_created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.comment_approved_comment = True
		self.save()

	def __str__(self):
		return self.comment_text

class Answer(models.Model):
	answer_stage = models.ForeignKey('questscreed.Stage', related_name='answers')
	answer = models.TextField()
	answer_picture = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')
	answer_choice = models.CharField(max_length=200, blank=True, null=True)
	answer_1 = models.CharField(max_length=200, blank=True, null=True)
	answer_2 = models.CharField(max_length=200, blank=True, null=True)
	answer_3 = models.CharField(max_length=200, blank=True, null=True)
	answer_4 = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.answer

class Statistic(models.Model):
	stat_quest = models.ForeignKey('questscreed.Quest', related_name='statistics')
	stat_login = models.CharField(max_length=200)
	start_time = models.DateTimeField(blank=True, null=True)
	end_time = models.DateTimeField(blank=True, null=True)
	time = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.stat_login

class Universary(models.Model):
	universary_login = models.CharField(max_length=200)
	balloon = models.BooleanField(default=False)
	text = models.BooleanField(default=False)
	mask = models.BooleanField(default=False)
	send = models.BooleanField(default=False)
	photo = models.BooleanField(default=False)

	def __str__(self):
		return self.universary_login