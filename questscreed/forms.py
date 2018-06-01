from django import forms

from .models import Commoncomment, Comment, Article, Quest, Stage, Answer

class QuestForm(forms.ModelForm):

	class Meta:
		model = Quest
		fields = ('quest_title', 'quest_city', 'quest_type', 'complexity', 'min_players', 'max_players', 'quest_text', 'quest_description', 'quest_cover',)
		labels = {'quest_title': ('Название квеста'), 'quest_city': ('Город'), 'quest_type': ('Тип квеста'), 'complexity': ('Сложность'),
		 'min_players': ('Минимальное число игроков'), 'max_players': ('Максимальное число игроков'), 'quest_description': ('Описание квеста'),
		 'quest_text': ('Краткое описание квеста'), 'quest_cover': ('Обложка для квеста')}
		widgets = {
			'min_players': forms.NumberInput(attrs={'placeholder': '2', 'step': '1', 'min': '1', 'max': '3'}),
			'max_players': forms.NumberInput(attrs={'placeholder': '6', 'step': '1', 'min': '4', 'max': '8'}),
			'quest_text': forms.Textarea(attrs={'placeholder': 'Введите, пожалуйста, текст, который будет отображаться на странице со всеми квестами'})
		}

class StageForm(forms.ModelForm):

	class Meta:
		model = Stage
		fields = ('stage_title', 'question_type', 'stage_question', 'answer_text', 'hint', 'answer_choice_1', 'answer_choice_2', 'answer_choice_3', 
			'answer_choice_4', 'answer_right_choice', 'answer_variant_1', 'answer_variant_2', 'answer_variant_3', 'answer_variant_4',)
		labels = {'stage_title': ('Название этапа'), 'question_type': ('Тип задания'), 'stage_question': ('Текст вопроса'), 'answer_text': ('Верный ответ'), 
		'hint': ('Подсказка'), 'answer_choice_1': ('Введите вариант ответа'), 'answer_choice_2': ('Введите вариант ответа'), 'answer_choice_3': ('Введите вариант ответа'), 
			'answer_choice_4': ('Введите вариант ответа'), 'answer_variant_1': ('Введите соответствие первому варианту'), 'answer_variant_2': 
			('Введите соответствие второму варианту'), 'answer_variant_3': ('Введите соответствие третьему варианту'), 'answer_variant_4': 
			('Введите соответствие четвертому варианту'), 'answer_right_choice': ('Введите верный ответ')}

class AnswerForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ('answer',)
		labels = {'answer': ('Введите ответ')}
		widgets = {
			'answer': forms.Textarea(attrs={'placeholder': 'Ответ введите с большой буквы без знаков препинания'}),
		}

class AnswerPicForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ('answer_picture',)
		labels = {'answer_picture': ('Загрузите изображение')}

class CommoncommentForm(forms.ModelForm):

    class Meta:
        model = Commoncomment
        fields = ('common_comment_author', 'common_comment_text',)
        labels = {'common_comment_author': ('Автор'), 'common_comment_text': ('Текст'),}
        widgets = {
            'common_comment_author': forms.TextInput(attrs={'placeholder': 'Введите, пожалуйста, имя или логин'}),
            'common_comment_text': forms.Textarea(
                attrs={'placeholder': 'Введите, пожалуйста, свой отзыв'}),
        }

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('comment_author', 'comment_text',)
		labels = {'comment_author': ('Автор'), 'comment_text': ('Текст'),}
		widgets = {
            'comment_author': forms.TextInput(attrs={'placeholder': 'Введите, пожалуйста, имя или логин'}),
            'comment_text': forms.Textarea(
                attrs={'placeholder': 'Введите, пожалуйста, свой отзыв'}),
        }

class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = ('article_title', 'article_text', 'article_description',)
		labels = {'article_title': ('Заголовок новости'), 'article_text': ('Текст новости'), 'article_description': ('Краткое описание новости'),}
		widgets = {
			'article_description': forms.Textarea(attrs={'placeholder': 'Введите, пожалуйста, текст, который будет отображаться на странице со всеми новостями'}),
		}