from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CreateCardPackage, CreateCardGroup, CreateCards, CreateComments
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Card_Packages, Card_Groups, Cards, Comments, Sorted_Package
from django.template.response import TemplateResponse
from django.contrib import messages 
from django.db.models import Q

def index(request):
    """
    View function for home page of site.
    """
	# Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
		context={'num_visits':num_visits}, # num_visits appended
    )
	
def create(request):
    return render(
        request,
        'project.html',
    )
	
def cards(request):
	if request.method =='POST':
		form = CreateCardPackage(request.POST, instance=Card_Packages())
		if form.is_valid():
			titles = request.POST.getlist('title')
			texts = request.POST.getlist('text')
			groups = request.POST.getlist('group')
			names = request.POST.getlist('name')
			user = request.user
			for name in names:
				cardPackage = Card_Packages(name = name, user = user)
				cardPackage.save()
			for title in titles:
				group = Card_Groups(card_package = cardPackage, title = title)
				group.save()
			for text in texts:
				card = Cards(card_package = cardPackage, text = text)
				card.save()
			return render(
		    request,
            'index.html',
            )
		else:
			form = CreateCardPackage(instance=Card_Packages())
			args = {'form': form}
			return render(
			request,
			'project.html',
			{'form': form}
		)
	else:
		form = CreateCardPackage(instance=Card_Packages())
		args = {'form': form}
		return render(
		request,
		'project.html',
		{'form': form}
	)
	
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(
            request,
            'index.html',
            )
        else:
            form = RegistrationForm()
            args = {'form': form}
            return render(
            request,
            'register.html',
            {'form': form}
        )
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(
        request,
        'register.html',
		{'form': form}
    )
	
def view(request):
	cardPackages = Card_Packages.objects.all()
	return render(
		request,
		'view.html',
    )

def package(request):
	cardPackages = Card_Packages.objects.all()
	context = {'cardPackages': cardPackages}
	return render(
		request,
		'package.html',
		context
    )

def packageList(request, package):
	package = Card_Packages.objects.get(id__exact=package)
	user = request.user
	if request.user.is_anonymous:
		comments = Comments.objects.filter(card_package__exact= package)
	else :	
		comments = Comments.objects.filter(card_package__exact= package).filter(user__exact= user)
	"commentsList = Comments.objects.filter( Q(card_package=package) & Q(user=user) )"
	context = {'package': package, 'user': user, 'comments': comments}
	return render(
		request,
		'packageList.html',
		context
    )

def admin(request):
	cardPackages = Card_Packages.objects.all()
	context = {'cardPackages': cardPackages}
	return render(
		request,
		'admin.html',
		context
    )

def edit(request, package):
	package = Card_Packages.objects.get(id__exact=package)
	context = {'package': package}
	return render(
		request,
		'edit.html',
		context
    )	
	
def comments(request, package):
	if request.method =='POST':
		commentID = request.POST.get('commentID')
		name = request.POST.get('name')
		user = request.user
		text = request.POST.get('comment')
		cardPackage = Card_Packages.objects.get(id__exact=package)
		
		
		cardsList = request.POST.getlist('cardsList')
		#sortedCards = request.POST.getlist('sortedCards')
		sortedCardsInts = list(filter(None, request.POST.getlist('sortedCards')))
		#aaaas = map(int, sortedCardsInt)
		cardTesting = Cards.objects.all() 
		cardsTest = []
		sort = Sorted_Package()
		#cardListIDs = request.POST.getlist('cardListID')
		cardGroupIDs = request.POST.getlist('cardGroupID')
		for cardGroupID, sortedCardsInt in zip(cardGroupIDs,sortedCardsInts):
			#testing1 = Card_Groups.objects.get(id__exact=cardGroupID)
			#testing2 = Cards.objects.get(id__exact=aaaa)
			#cardsTest.append(testing2)
			
			sort.card_package = cardPackage
			sort.user = user
			sort.card_group = Card_Groups.objects.get(id__exact=cardGroupID)
			sort.cards.add(Cards.objects.get(id__exact=sortedCardsInt))
			sort.save()
			#sort.card_group.add(Card_Groups.objects.get(id__exact=cardGroupID))
			
			#sort.cards.add(testing2)
			#sort.card_package = cardPackage
			#sort.user = user
			#sort.save();
			#sort.card_group.add(test)
		#for sortedCards in sortedCards:
			#test1 = Cards.objects.get(id__exact=sortedCards)
			#sort.cards.add(test1)	
		#	test.append(group)
		#	for cardListID in cardListIDs:
		#		card = Cards()
		#		card = Cards.objects.get(id__exact=cardListID)
		#		card.card_group = group
		#		card.save()
			
		
		
		#test = None
		#group = Card_Groups()
		#cardList = Cards.objects.all()
		#cardGroups = Card_Groups.objects.all() 
		#test = list(sortedCards)

		#cardGroupIDs = request.POST.getlist('cardGroupID')
		#sort = Sorted_Package()
		#for cardGroupIDs in cardGroups:
			#test = Card_Groups.objects.get(title = cardGroupIDs ) 
			#if cardGroupIDs == test:
				#sort.card_package = cardPackage
			
				#
				#sort.save()
			#if sortedCard in cardList:
			#	sort.cards.add(sortedCard)
			#sort.card_group.add(group)
		
		comment = Comments()
		comment.card_package = cardPackage
		comment.user = user
		comment.comment = text
		comment.id = commentID
		comment.save()
		return render(
		request,
			'index.html',
			{'sort': sort }
		)
	else:
		form = CreateComments(instance=Comments())
		args = {'form': form}
		return render(
		request,
		'packageList.html',
		{'form': form}
	)	
	
def editPackage(request, package):
	if request.method =='POST':
		form = CreateCardPackage(request.POST, instance=Card_Packages())
		if form.is_valid():
			cardPackage = Card_Packages.objects.get(id__exact=package)
			titles = request.POST.getlist('title')
			texts = request.POST.getlist('text')
			cardGroupIDs = request.POST.getlist('cardGroupID')
			cardListIDs = request.POST.getlist('cardListID')
			newGroups = request.POST.getlist('newGroup')
			newCards = request.POST.getlist('newCard')
			deleteGroups = request.POST.getlist('deleteGroup')
			deleteCards = request.POST.getlist('deleteCard')
			name = request.POST.get('name')
			user = request.user
			cardPackage.name = name
			cardPackage.save()
			group = Card_Groups()
			test = Card_Groups()
			card = Cards()
		
			for newGroup in newGroups:
				group = Card_Groups(card_package = cardPackage, title = newGroup)
				group.save()
			for newCard in newCards:
				card = Cards(card_package = cardPackage, text = newCard)
				card.save()				
			for cardGroupID, title in zip(cardGroupIDs, titles):
				group.id = cardGroupID
				group.card_package = cardPackage
				group.title = title
				group.save()
			for cardListID, text in zip(cardListIDs, texts):
				card.id = cardListID
				card.card_package = cardPackage
				card.text = text
				card.save()
			for deleteCard in deleteCards:
				test = Cards.objects.get(id__exact= deleteCard)
				test.delete()
				
			for deleteGroup in deleteGroups:
				test1 = Card_Groups.objects.filter(card_package = cardPackage).filter(id__exact= deleteGroup)
				test1.delete()	
			return render(
			request,
			'admin.html',
			)       
		else:
			form = CreateCardPackage(instance=Card_Packages())
			args = {'form': form}
			return render(
			request,
			'admin.html',
			{'form': form}
		)
	else:
		form = CreateCardPackage(instance=Card_Packages())
		args = {'form': form}
		return render(
		request,
		'admin.html',
		{'form': form}
	)	
	
def cardPackages(request):
    cardPackages = Card_Packages.objects.all() 
    return TemplateResponse(request, views.index, {'cardPackages': cardPackages})
	
def cardGroups(request):
    cardGroups = Card_Groups.objects.all() 
    return TemplateResponse(request, views.index, {'cardGroups': cardGroups})

def cardList(request):
    cardList = Cards.objects.all() 
    return TemplateResponse(request, views.index, {'cardList': cardList})

def commentList(request):
    commentList = Comments.objects.all() 
    return TemplateResponse(request, views.index, {'commentList': commentList})	
	
def sortedList(request):
    sortedList = Sorted_Package.objects.all() 
    return TemplateResponse(request, views.index, {'sortedList': sortedList})		