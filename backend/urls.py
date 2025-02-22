"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend_app.views import RegisterView, UploadedFilesView, UploadedAudioView, UploadedVideoView, NoteView, FormTemplateView, UploadedTextFileView, UploadedPdfFileView, SilaView, CommunityView, MemberView, CourseWebUserView, AlarmView, TutorialView, OwnerView, ContentView, CartItemsView, NewfolderView

router = routers.DefaultRouter()
router.register('users', RegisterView, 'user')
router.register('uploadfiles', UploadedFilesView, 'uploadfile')
router.register('uploadaudios', UploadedAudioView, 'uploadaudio')
router.register('uploadvideos', UploadedVideoView, 'uploadvideo')
router.register('notes', NoteView, 'note')
router.register('formtemplates', FormTemplateView, 'formtemplate')
router.register('uploadtextfiles', UploadedTextFileView, 'uploadtextfile')
router.register('uploadpdffiles', UploadedPdfFileView, 'uploadpdffile')
router.register('registers1', SilaView , 'registers1')
router.register('communities', CommunityView, 'community')
router.register('members', MemberView, 'member')
router.register('coursewebusers', CourseWebUserView, 'coursewebuser')
router.register('alarms', AlarmView, 'alarm')
router.register('tutorials', TutorialView, 'tutorial')
router.register('owners', OwnerView, 'owner')
router.register('contents', ContentView, 'content')
router.register('cartitems', CartItemsView, 'cartitem')
router.register('create_folders', NewfolderView, 'create_folder')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
