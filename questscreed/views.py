from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Quest, Article, Commoncomment, Comment, Stage, Answer, Statistic, Universary
from .forms import CommoncommentForm, CommentForm, ArticleForm, QuestForm, StageForm, AnswerForm, AnswerPicForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return redirect('index')
	else:
		form = UserCreationForm()
		return render(request, 'registration/register.html', {'form': form})

def index(request):
	quests = Quest.objects.order_by('-votes')
	commoncomments = Commoncomment.objects.order_by('-common_comment_created_date')
	return render(request, 'questscreed/index.html', {'quests': quests, 'commoncomments': commoncomments})

def main_page(request):
	user = request.user.username
	quests = Quest.objects.filter(quest_author=user).order_by('-votes')
	statistics = Statistic.objects.filter(stat_login=user).order_by('time')
	return render(request, 'questscreed/main_page.html', {'quests': quests, 'statistics': statistics})

@login_required
def universary(request):
	universary = Universary.objects.get(universary_login=request.user.username)
	return render(request, 'questscreed/universary.html', {'universary': universary})

def get_all_logged_in_users():
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=uid_list)

def moderation(request):
	users = get_all_logged_in_users()
	counter = 0
	for user in users:
		if not Universary.objects.filter(universary_login=user).exists():
			Universary(universary_login=user).save()
	if request.method == "POST":
		for user in users:
			counter = counter + 1
			number_balloon = 'checkBox1_'+str(counter)
			balloon = request.POST.get(number_balloon)
			if balloon:
				query = Universary.objects.get(universary_login=user)
				pk = query.pk
				user = query.universary_login
				if query.text == True:
					Universary(pk=pk, universary_login=user, balloon=True, text=True).save()
					if query.mask == True:
						Universary(pk=pk, universary_login=user, balloon=True, text=True, mask=True).save()
				else:
					if query.mask == True:
						Universary(pk=pk, universary_login=user, balloon=True, mask=True).save()
					else:
						Universary(pk=pk, universary_login=user, balloon=True).save()
			number_text = 'checkBox2_'+str(counter)
			text = request.POST.get(number_text)
			if text:
				query = Universary.objects.get(universary_login=user)
				pk = query.pk
				user = query.universary_login
				if query.balloon == True:
					Universary(pk=pk, universary_login=user, balloon=True, text=True).save()
					if query.mask == True:
						Universary(pk=pk, universary_login=user, balloon=True, text=True, mask=True).save()
				else:
					if query.mask == True:
						Universary(pk=pk, universary_login=user, text=True, mask=True).save()
					else:
						Universary(pk=pk, universary_login=user, text=True).save()
			number_mask = 'checkBox3_'+str(counter)
			mask = request.POST.get(number_mask)
			if mask:
				query = Universary.objects.get(universary_login=user)
				pk = query.pk
				user = query.universary_login
				if query.balloon == True:
					Universary(pk=pk, universary_login=user, balloon=True, mask=True).save()
					if query.text == True:
						if query.send == True:
							Universary(pk=pk, universary_login=user, balloon=True, text=True, mask=True, send=True).save()
						else:
							Universary(pk=pk, universary_login=user, balloon=True, text=True, mask=True).save()
				else:
					if query.text == True:
						Universary(pk=pk, universary_login=user, text=True, mask=True).save()
					else:
						Universary(pk=pk, universary_login=user, mask=True).save()
			number_send = 'checkBox4_'+str(counter)
			send = request.POST.get(number_send)
			if send:
				query = Universary.objects.get(universary_login=user)
				pk = query.pk
				user = query.universary_login
				if query.balloon == True:
					if query.text == True:
						if query.mask == True:
							Universary(pk=pk, universary_login=user, balloon=True, text=True, mask=True, send=True).save()
						else:
							if query.balloon == True:
								if query.text == True:
									Universary(pk=pk, universary_login=user, balloon=True, text=True, send=True).save()
			number_photo = 'checkBox5_'+str(counter)
			photo = request.POST.get(number_photo)
			if photo:
				query = Universary.objects.get(universary_login=user)
				pk = query.pk
				user = query.universary_login
				if query.balloon == True:
					if query.text == True:
						if query.mask == True:
							if query.send == True:
								Universary(pk=pk, universary_login=user, balloon=True, text=True, mask=True, send=True, photo=True).save()
	universarys = Universary.objects.all()
	return render(request, 'questscreed/moderation.html', {'users': users, 'universarys': universarys})

def news(request):
	articles = Article.objects.filter(article_published_date__lte=timezone.now()).order_by('-article_published_date')
	paginator = Paginator(articles, 2)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render(request, 'questscreed/news.html', {'articles': articles})

def quests(request):
	quests = Quest.objects.order_by('-pk')
	paginator = Paginator(quests, 6)
	page = request.GET.get('page')
	try:
		quests = paginator.page(page)
	except PageNotAnInteger:
		quests = paginator.page(1)
	except EmptyPage:
		quests = paginator.page(paginator.num_pages)
	return render(request, 'questscreed/quests.html', {'quests': quests})

def quests_reverse(request):
	quests = Quest.objects.order_by('pk')
	paginator = Paginator(quests, 6)
	page = request.GET.get('page')
	try:
		quests = paginator.page(page)
	except PageNotAnInteger:
		quests = paginator.page(1)
	except EmptyPage:
		quests = paginator.page(paginator.num_pages)
	return render(request, 'questscreed/quests.html', {'quests': quests})

def quests_popular(request):
	quests = Quest.objects.order_by('-votes')
	paginator = Paginator(quests, 6)
	page = request.GET.get('page')
	try:
		quests = paginator.page(page)
	except PageNotAnInteger:
		quests = paginator.page(1)
	except EmptyPage:
		quests = paginator.page(paginator.num_pages)
	return render(request, 'questscreed/quests.html', {'quests': quests})

def rules(request):
	return render(request, 'questscreed/rules.html')

def quest_detail(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	print(quest.quest_title)
	return render(request, 'questscreed/quest_detail.html', {'quest': quest})

@login_required
def quest_edit(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	form = QuestForm(request.POST, instance=quest)
	if form.is_valid():
		quest = form.save(commit=False)
		quest.save()
		return redirect('quest_detail', pk=quest.pk)
	else:
		form = QuestForm(instance=quest)
	return render(request, 'questscreed/quest_edit.html', {'form': form})

@login_required
def add_quest(request):
	if request.method == "POST":
		form = QuestForm(request.POST)
		if form.is_valid():
			quest = form.save(commit=False)
			quest.save()
			return redirect('quests')
	else:
		form = QuestForm()
	return render(request, 'questscreed/quest_form.html', {'form': form})

@login_required
def delete_quest(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	quest.delete()
	return redirect('quests')

def news_detail(request, pk):
	article = get_object_or_404(Article, pk=pk)
	return render(request, 'questscreed/news_detail.html', {'article': article})

@login_required
def news_edit(request, pk):
	article = get_object_or_404(Article, pk=pk)
	form = ArticleForm(request.POST, instance=article)
	if form.is_valid():
		article = form.save(commit=False)
		article.article_published_date = timezone.now()
		article.save()
		return redirect('news_detail', pk=article.pk)
	else:
		form = ArticleForm(instance=article)
	return render(request, 'questscreed/news_edit.html', {'form': form})

@login_required
def add_comment(request):
	if request.method == "POST":
		form = ComoncommentForm(request.POST)
		if form.is_valid():
			commoncomment = form.save(commit=False)
			commoncomment.common_comment_created_date = timezone.now()
			commoncomment.save()
			return redirect('index')
	else:
		form = CommoncommentForm()
	return render(request, 'questscreed/review_form.html', {'form': form})

@login_required
def add_comment_to_quest(request, pk):
    quest = get_object_or_404(Quest, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_created_date = timezone.now()
            comment.quest_title = quest
            comment.save()
            return redirect('quest_detail', pk=quest.pk)
    else:
        form = CommentForm()
    return render(request, 'questscreed/review_form.html', {'form': form})

@login_required
def add_article(request):
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.article_published_date = timezone.now()
			article.save()
			return redirect('news')
	else:
		form = ArticleForm()
	return render(request, 'questscreed/news_form.html', {'form': form})

@login_required
def delete_article(request, pk):
	article = get_object_or_404(Article, pk=pk)
	article.delete()
	return redirect('news')

@login_required
def commoncomment_approve(request, pk):
    commoncomment = get_object_or_404(Commoncomment, pk=pk)
    commoncomment.approve()
    return redirect('index')

@login_required
def commoncomment_remove(request, pk):
    commoncomment = get_object_or_404(Commoncomment, pk=pk)
    commoncomment.delete()
    return redirect('index')

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('quest_detail', pk=comment.comment_quest.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('quest_detail', pk=comment.comment_quest.pk)

@login_required
def quest_vote(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	quest.vote()
	return redirect('quest_detail', pk=quest.pk)

@login_required
def stage_list(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	stages = Stage.objects.order_by('pk')
	return render(request, 'questscreed/stage_list.html', {'stages': stages, 'quest': quest})

@login_required
def stage_edit(request, pk):
	stage = get_object_or_404(Stage, pk=pk)
	form = StageForm(request.POST, instance=stage)
	if form.is_valid():
		stage = form.save(commit=False)
		stage.save()
		return redirect('stage_list', pk=stage.stage_quest.pk)
	else:
		form = StageForm(instance=stage)
	return render(request, 'questscreed/stage_edit.html', {'form': form})

@login_required
def stage_add(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	if request.method == "POST":
		form = StageForm(request.POST)
		if form.is_valid():
			stage = form.save(commit=False)
			stage.stage_quest = quest
			stage.save()
			return redirect('stage_list', pk=quest.pk)
	else:
		form = StageForm()
	return render(request, 'questscreed/stage_form.html', {'form': form})

@login_required
def quest_pass_index(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	return render(request, 'questscreed/quest_pass_index.html', {'quest': quest})

@login_required
def quest_pass_last(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	statistic = get_object_or_404(Statistic, pk=request.session["stat"])
	start_time = statistic.start_time
	end_time = timezone.now()
	time = (end_time - statistic.start_time)
	time_pretty = "%.2d:%.2d" % ((time.seconds//60)%60, time.seconds%60)
	Statistic(pk=request.session["stat"], stat_quest=quest, stat_login=request.user.username, start_time=start_time, end_time=end_time, time=time_pretty).save()
	return render(request, 'questscreed/quest_pass_last.html', {'quest': quest, 'time': time_pretty})

@login_required
def quest_pass_stage(request, quest_pk, stage_pk):
	quest_pk = get_object_or_404(Quest, pk=quest_pk)
	quest = quest_pk.pk
	if Stage.objects.filter(stage_quest=quest_pk, stage_number=stage_pk).exists():
		stage = Stage.objects.get(stage_quest=quest_pk, stage_number=stage_pk)
		stage_pk = stage.stage_number
		if stage.question_type == "QWC":
			if request.method == "POST":
				if stage_pk == 1:
					start_time = timezone.now()
					Statistic(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time, end_time=start_time, time=start_time).save()
					statistic = Statistic.objects.get(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time)
					request.session["stat"] = statistic.pk
				answer = request.POST.get('quest_radio')
				if answer == stage.answer_right_choice:
					stage_pk = stage.stage_number + 1
					if Stage.objects.filter(stage_quest=quest_pk, stage_number=stage_pk).exists():
						return redirect('quest_pass_stage', quest_pk=quest, stage_pk=stage_pk)
					else:
						return redirect('quest_pass_last', pk=quest)
			return render(request, 'questscreed/quest_pass_stage.html', {'quest': quest_pk, 'stage_pk': stage_pk, 'stage': stage})
		if stage.question_type == "QWE":
			if request.method == "POST":
				if stage_pk == 1:
					start_time = timezone.now()
					Statistic(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time, end_time=start_time, time=start_time).save()
					statistic = Statistic.objects.get(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time)
					request.session["stat"] = statistic.pk
				answer_1 = request.POST.get('question_equivalent_1')
				answer_2 = request.POST.get('question_equivalent_2')
				answer_3 = request.POST.get('question_equivalent_3')
				answer_4 = request.POST.get('question_equivalent_4')
				if answer_1 == '3':
					if answer_2 == '4':
						if answer_3 == '1':
							if answer_4 == '2':
								stage_pk = stage.stage_number + 1
								if Stage.objects.filter(stage_quest=quest_pk, stage_number=stage_pk).exists():
									return redirect('quest_pass_stage', quest_pk=quest, stage_pk=stage_pk)
								else:
									return redirect('quest_pass_last', pk=quest)
			return render(request, 'questscreed/quest_pass_stage.html', {'quest': quest_pk, 'stage_pk': stage_pk, 'stage': stage})
		if stage.question_type == "QWA":
			if request.method == "POST":
				if stage_pk == 1:
					start_time = timezone.now()
					Statistic(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time, end_time=start_time).save()
					statistic = Statistic.objects.get(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time)
					request.session["stat"] = statistic.pk
				form = AnswerForm(request.POST)
				if form.is_valid():
					answer = form.save(commit=False)
					answer.answer_stage = stage
					if answer.answer == stage.answer_text:
						stage_pk = stage.stage_number + 1
						if Stage.objects.filter(stage_quest=quest_pk, stage_number=stage_pk).exists():
							return redirect('quest_pass_stage', quest_pk=quest, stage_pk=stage_pk)
						else:
							return redirect('quest_pass_last', pk=quest)
			else:
				form = AnswerForm()
		else:
			if stage.question_type == "QWP":
				if request.method == "POST":
					if stage_pk == 1:
						start_time = timezone.now()
						Statistic(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time, end_time=start_time).save()
						statistic = Statistic.objects.get(stat_quest=quest_pk, stat_login=request.user.username, start_time=start_time)
						request.session["stat"] = statistic.pk
					form = AnswerPicForm(request.POST)
					if form.is_valid():
						answer = form.save(commit=False)
						answer.answer_stage = stage
						if answer.answer == stage.answer_text:
							stage_pk = stage.stage_number + 1
							if Stage.objects.filter(stage_quest=quest_pk, stage_number=stage_pk).exists():
								return redirect('quest_pass_stage', quest_pk=quest, stage_pk=stage_pk)
							else:
								return redirect('quest_pass_last', pk=quest)
				else:
					form = AnswerPicForm()
		return render(request, 'questscreed/quest_pass_stage.html', {'quest': quest_pk, 'form': form, 'stage_pk': stage_pk, 'stage': stage})
	else:
		return render(request, 'questscreed/empty_page.html')

def statistics(request, pk):
	quest = get_object_or_404(Quest, pk=pk)
	statistics = Statistic.objects.order_by('time')
	return render(request, 'questscreed/statistics.html', {'quest': quest, 'statistics': statistics})

@login_required
def universary_pass(request, stage_pk, quest_pk=4):
	quest_pk = get_object_or_404(Quest, pk=quest_pk)
	quest = quest_pk.pk
	if Stage.objects.filter(stage_quest=quest_pk, stage_number=stage_pk).exists():
		stage = Stage.objects.get(stage_quest=quest_pk, stage_number=stage_pk)
		stage_pk = stage.stage_number
		if stage.question_type == "QWC":
			if request.method == "POST":
				answer = request.POST.get('quest_radio')
				if answer == stage.answer_right_choice:
					return redirect('universary')
			return render(request, 'questscreed/quest_pass_stage.html', {'quest': quest_pk, 'stage_pk': stage_pk, 'stage': stage})
		if stage.question_type == "QWE":
			if request.method == "POST":
				answer_1 = request.POST.get('question_equivalent_1')
				answer_2 = request.POST.get('question_equivalent_2')
				answer_3 = request.POST.get('question_equivalent_3')
				answer_4 = request.POST.get('question_equivalent_4')
				if answer_1 == '3':
					if answer_2 == '4':
						if answer_3 == '1':
							if answer_4 == '2':
								return redirect('universary')
			return render(request, 'questscreed/quest_pass_stage.html', {'quest': quest_pk, 'stage_pk': stage_pk, 'stage': stage})
		if stage.question_type == "QWA":
			if request.method == "POST":
				form = AnswerForm(request.POST)
				if form.is_valid():
					answer = form.save(commit=False)
					answer.answer_stage = stage
					if answer.answer == stage.answer_text:
						return redirect('universary')
			else:
				form = AnswerForm()
			return render(request, 'questscreed/quest_pass_stage.html', {'quest': quest_pk, 'form': form, 'stage_pk': stage_pk, 'stage': stage})
	else:
		return render(request, 'questscreed/empty_page.html')