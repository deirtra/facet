""" Media Asset handling views for editorial app.

    editorial/views/assetviews.py
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView , UpdateView, DetailView
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

from editorial.forms import (
    ImageAssetForm,
    AddImageForm,
    DocumentAssetForm,
    AddDocumentForm,
    AudioAssetForm,
    AddAudioForm,
    VideoAssetForm,
    AddVideoForm,
    )

from editorial.models import (
    WebFacet,
    PrintFacet,
    AudioFacet,
    VideoFacet,
    ImageAsset,
    DocumentAsset)


#----------------------------------------------------------------------#
#   Asset Library Views
#----------------------------------------------------------------------#

def asset_library(request):
    """ Display media library of all organization assets."""

    images = ImageAsset.objects.filter(organization=request.user.organization)
    documents = DocumentAsset.objects.filter(organization=request.user.organization)

    return render(request, 'editorial/assets.html', {
        'images': images,
        'documents': documents,
    })

#----------------------------------------------------------------------#
#   Asset Detail Views
#----------------------------------------------------------------------#

def image_asset_detail(request, pk):
    """ Display detail information for a specific image asset."""

    image = get_object_or_404(ImageAsset, id=pk)
    image_usage = ImageAsset.get_image_usage(image)
    print "IU: ", image_usage

    if request.method =="POST":
        editimageform = ImageAssetForm(data=request.POST, instance=image)
        if editimageform.is_valid():
            editimageform.save()
            return redirect('asset_detail', pk=image.id)
    else:
        editimageform = ImageAssetForm(instance=image)

    return render(request, 'editorial/imageassetdetail.html', {
        'image': image,
        'image_usage': image_usage,
        'editimageform': editimageform,
    })

def document_asset_detail(request, pk):
    """ Display detail information for a specific document asset."""

    document = get_object_or_404(DocumentAsset, id=pk)
    document_usage = DocumentAsset.get_document_usage(document)
    print "IU: ", document_usage

    # if request.method =="POST":
    #     editimageform = ImageAssetForm(data=request.POST, instance=image)
    #     if editimageform.is_valid():
    #         editimageform.save()
    #         return redirect('asset_detail', pk=image.id)
    # else:
    #     editimageform = ImageAssetForm(instance=image)
    #
    # return render(request, 'editorial/imageassetdetail.html', {
    #     'image': image,
    #     'image_usage': image_usage,
    #     'editimageform': editimageform,
    # })


#----------------------------------------------------------------------#
#   Upload Image Asset Views
#----------------------------------------------------------------------#

def upload_webfacet_image(request):
    """ Add image to a webfacet."""

    if request.method == 'POST':
        imageform=ImageAssetForm(request.POST, request.FILES)
        if imageform.is_valid():
            webimage = imageform.save(commit=False)
            # retrieve the webfacet the image should be associated with
            webfacet_id = request.POST.get('webfacet')
            print "webfacetID: ", webfacet_id
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            # set request based attributes
            webimage.owner = request.user
            webimage.organization = request.user.organization
            webimage.save()
            # add image asset to webfacet image_assets
            webfacet.image_assets.add(webimage)
            webfacet.save()
    return redirect('story_detail', pk=webfacet.story.id)

def upload_printfacet_image(request):
    """ Add image to a printfacet."""

    if request.method == 'POST':
        imageform=ImageAssetForm(request.POST, request.FILES)
        if imageform.is_valid():
            printimage = imageform.save(commit=False)
            # retrieve the printfacet the image should be associated with
            printfacet_id = request.POST.get('printfacet')
            printfacet = get_object_or_404(PrintFacet, id=printfacet_id)
            # set request based attributes
            printimage.owner = request.user
            printimage.organization = request.user.organization
            printimage.save()
            # add image asset to printfacet image_assets
            printfacet.image_assets.add(printimage)
            printfacet.save()
    return redirect('story_detail', pk=printfacet.story.id)

def upload_audiofacet_image(request):
    """ Add image to a audiofacet."""

    if request.method == 'POST':
        imageform=ImageAssetForm(request.POST, request.FILES)
        if imageform.is_valid():
            audioimage = imageform.save(commit=False)
            # retrieve the audiofacet the image should be associated with
            audiofacet_id = request.POST.get('audiofacet')
            audiofacet = get_object_or_404(AudioFacet, id=audiofacet_id)
            # set request based attributes
            audioimage.owner = request.user
            audioimage.organization = request.user.organization
            audioimage.save()
            # add image asset to audiofacet image_assets
            audiofacet.image_assets.add(audioimage)
            audiofacet.save()
    return redirect('story_detail', pk=audiofacet.story.id)

def upload_videofacet_image(request):
    """ Add image to a videofacet."""

    if request.method == 'POST':
        imageform=ImageAssetForm(request.POST, request.FILES)
        if imageform.is_valid():
            videoimage = imageform.save(commit=False)
            # retrieve the videofacet the image should be associated with
            videofacet_id = request.POST.get('videofacet')
            videofacet = get_object_or_404(VideoFacet, id=videofacet_id)
            # set request based attributes
            videoimage.owner = request.user
            videoimage.organization = request.user.organization
            videoimage.save()
            # add image asset to videofacet image_assets
            videofacet.image_assets.add(videoimage)
            videofacet.save()
    return redirect('story_detail', pk=videofacet.story.id)


#----------------------------------------------------------------------#
#   Add Image Asset Views
#----------------------------------------------------------------------#

def add_webfacet_image(request):
    """ Add existing image(s) in the library to another webfacet."""

    if request.method == "POST":
        add_image_form = AddImageForm(request.POST, request=request)
        if add_image_form.is_valid():
            webfacet_id = request.POST.get('webfacet')
            print "WEBFACETid: ", webfacet_id
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            images = request.POST.getlist('images')
            print "IMAGES: ", images
            for image in images:
                img_ins = get_object_or_404(ImageAsset, id=image)
                print "IMGins: ", img_ins
                webfacet.image_assets.add(img_ins)
            webfacet.save()
    return redirect('story_detail', pk=webfacet.story.id)


def add_printfacet_image(request):
    """ Add existing image(s) in the library to another printfacet."""

    if request.method == "POST":
        add_image_form = AddImageForm(request.POST, request=request)
        if add_image_form.is_valid():
            printfacet_id = request.POST.get('printfacet')
            print "printFACETid: ", printfacet_id
            printfacet = get_object_or_404(PrintFacet, id=printfacet_id)
            images = request.POST.getlist('images')
            print "IMAGES: ", images
            for image in images:
                img_ins = get_object_or_404(ImageAsset, id=image)
                print "IMGins: ", img_ins
                printfacet.image_assets.add(img_ins)
            printfacet.save()
    return redirect('story_detail', pk=printfacet.story.id)


def add_audiofacet_image(request):
    """ Add existing image(s) in the library to another audiofacet."""

    if request.method == "POST":
        add_image_form = AddImageForm(request.POST, request=request)
        if add_image_form.is_valid():
            audiofacet_id = request.POST.get('audiofacet')
            print "audioFACETid: ", audiofacet_id
            audiofacet = get_object_or_404(AudioFacet, id=audiofacet_id)
            images = request.POST.getlist('images')
            print "IMAGES: ", images
            for image in images:
                img_ins = get_object_or_404(ImageAsset, id=image)
                print "IMGins: ", img_ins
                audiofacet.image_assets.add(img_ins)
            audiofacet.save()
    return redirect('story_detail', pk=audiofacet.story.id)


def add_videofacet_image(request):
    """ Add existing image(s) in the library to another videofacet."""

    if request.method == "POST":
        add_image_form = AddImageForm(request.POST, request=request)
        if add_image_form.is_valid():
            videofacet_id = request.POST.get('videofacet')
            print "videoFACETid: ", videofacet_id
            videofacet = get_object_or_404(VideoFacet, id=videofacet_id)
            images = request.POST.getlist('images')
            print "IMAGES: ", images
            for image in images:
                img_ins = get_object_or_404(ImageAsset, id=image)
                print "IMGins: ", img_ins
                videofacet.image_assets.add(img_ins)
            videofacet.save()
    return redirect('story_detail', pk=videofacet.story.id)

#----------------------------------------------------------------------#
#   Upload Document Asset Views
#----------------------------------------------------------------------#

def upload_webfacet_document(request):
    """ Add document to a webfacet."""

    if request.method == 'POST':
        documentform=DocumentAssetForm(request.POST, request.FILES)
        if documentform.is_valid():
            webdocument = documentform.save(commit=False)
            # retrieve the webfacet the document should be associated with
            webfacet_id = request.POST.get('webfacet')
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            # set request based attributes
            webdocument.owner = request.user
            webdocument.organization = request.user.organization
            webdocument.save()
            # add document asset to webfacet document_assets
            webfacet.document_assets.add(webdocument)
            webfacet.save()
    return redirect('story_detail', pk=webfacet.story.id)

def upload_printfacet_document(request):
    """ Add document to a printfacet."""

    if request.method == 'POST':
        documentform=DocumentAssetForm(request.POST, request.FILES)
        if documentform.is_valid():
            printdocument = documentform.save(commit=False)
            # retrieve the printfacet the document should be associated with
            printfacet_id = request.POST.get('printfacet')
            printfacet = get_object_or_404(PrintFacet, id=printfacet_id)
            # set request based attributes
            printdocument.owner = request.user
            printdocument.organization = request.user.organization
            printdocument.save()
            # add document asset to printfacet document_assets
            printfacet.document_assets.add(printdocument)
            printfacet.save()
    return redirect('story_detail', pk=printfacet.story.id)

def upload_audiofacet_document(request):
    """ Add document to a audiofacet."""

    if request.method == 'POST':
        documentform=DocumentAssetForm(request.POST, request.FILES)
        if documentform.is_valid():
            audiodocument = documentform.save(commit=False)
            # retrieve the audiofacet the document should be associated with
            audiofacet_id = request.POST.get('audiofacet')
            audiofacet = get_object_or_404(AudioFacet, id=audiofacet_id)
            # set request based attributes
            audiodocument.owner = request.user
            audiodocument.organization = request.user.organization
            audiodocument.save()
            # add document asset to audiofacet document_assets
            audiofacet.document_assets.add(audiodocument)
            audiofacet.save()
    return redirect('story_detail', pk=audiofacet.story.id)

def upload_videofacet_document(request):
    """ Add document to a videofacet."""

    if request.method == 'POST':
        documentform=DocumentAssetForm(request.POST, request.FILES)
        if documentform.is_valid():
            videodocument = documentform.save(commit=False)
            # retrieve the videofacet the document should be associated with
            videofacet_id = request.POST.get('videofacet')
            videofacet = get_object_or_404(VideoFacet, id=videofacet_id)
            # set request based attributes
            videodocument.owner = request.user
            videodocument.organization = request.user.organization
            videodocument.save()
            # add document asset to videofacet document_assets
            videofacet.document_assets.add(videodocument)
            videofacet.save()
    return redirect('story_detail', pk=videofacet.story.id)

#----------------------------------------------------------------------#
#   Add Document Asset Views
#----------------------------------------------------------------------#

def add_webfacet_document(request):
    """ Add existing document(s) in the library to another webfacet."""

    if request.method == "POST":
        add_document_form = AddDocumentForm(request.POST, request=request)
        if add_document_form.is_valid():
            webfacet_id = request.POST.get('webfacet')
            print "WEBFACETid: ", webfacet_id
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            documents = request.POST.getlist('documents')
            print "DOCS: ", documents
            for document in documents:
                doc_ins = get_object_or_404(DocumentAsset, id=document)
                print "DOCins: ", doc_ins
                webfacet.document_assets.add(doc_ins)
            webfacet.save()
    return redirect('story_detail', pk=webfacet.story.id)


def add_printfacet_document(request):
    """ Add existing document(s) in the library to another printfacet."""

    if request.method == "POST":
        add_document_form = AddDocumentForm(request.POST, request=request)
        if add_document_form.is_valid():
            printfacet_id = request.POST.get('printfacet')
            print "printFACETid: ", printfacet_id
            printfacet = get_object_or_404(PrintFacet, id=printfacet_id)
            documents = request.POST.getlist('documents')
            print "IMAGES: ", documents
            for document in documents:
                doc_ins = get_object_or_404(DocumentAsset, id=document)
                print "docins: ", doc_ins
                printfacet.document_assets.add(doc_ins)
            printfacet.save()
    return redirect('story_detail', pk=printfacet.story.id)


def add_audiofacet_document(request):
    """ Add existing document(s) in the library to another audiofacet."""

    if request.method == "POST":
        add_document_form = AddDocumentForm(request.POST, request=request)
        if add_document_form.is_valid():
            audiofacet_id = request.POST.get('audiofacet')
            print "audioFACETid: ", audiofacet_id
            audiofacet = get_object_or_404(AudioFacet, id=audiofacet_id)
            documents = request.POST.getlist('documents')
            print "IMAGES: ", documents
            for document in documents:
                doc_ins = get_object_or_404(DocumentAsset, id=document)
                print "docins: ", doc_ins
                audiofacet.document_assets.add(doc_ins)
            audiofacet.save()
    return redirect('story_detail', pk=audiofacet.story.id)


def add_videofacet_document(request):
    """ Add existing document(s) in the library to another videofacet."""

    if request.method == "POST":
        add_document_form = AddDocumentForm(request.POST, request=request)
        if add_document_form.is_valid():
            videofacet_id = request.POST.get('videofacet')
            print "videoFACETid: ", videofacet_id
            videofacet = get_object_or_404(VideoFacet, id=videofacet_id)
            documents = request.POST.getlist('documents')
            print "IMAGES: ", documents
            for document in documents:
                doc_ins = get_object_or_404(DocumentAsset, id=document)
                print "docins: ", doc_ins
                videofacet.document_assets.add(doc_ins)
            videofacet.save()
    return redirect('story_detail', pk=videofacet.story.id)

#----------------------------------------------------------------------#
#   Upload Audio Asset Views
#----------------------------------------------------------------------#

def upload_webfacet_audio(request):
    """ Add audio to a webfacet."""

    if request.method == 'POST':
        audioform=AudioAssetForm(request.POST, request.FILES)
        if audioform.is_valid():
            webaudio = audioform.save(commit=False)
            # retrieve the webfacet the audio should be associated with
            webfacet_id = request.POST.get('webfacet')
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            # set request based attributes
            webaudio.owner = request.user
            webaudio.organization = request.user.organization
            webaudio.save()
            # add audio asset to webfacet audio_assets
            webfacet.audio_assets.add(webaudio)
            webfacet.save()
    return redirect('story_detail', pk=webfacet.story.id)


def upload_printfacet_audio(request):
    """ Add audio to a printfacet."""

    if request.method == 'POST':
        audioform=AudioAssetForm(request.POST, request.FILES)
        if audioform.is_valid():
            printaudio = audioform.save(commit=False)
            # retrieve the printfacet the audio should be associated with
            printfacet_id = request.POST.get('printfacet')
            printfacet = get_object_or_404(PrintFacet, id=printfacet_id)
            # set request based attributes
            printaudio.owner = request.user
            printaudio.organization = request.user.organization
            printaudio.save()
            # add audio asset to printfacet audio_assets
            printfacet.audio_assets.add(printaudio)
            printfacet.save()
    return redirect('story_detail', pk=printfacet.story.id)


def upload_audiofacet_audio(request):
    """ Add audio to a audiofacet."""

    if request.method == 'POST':
        audioform=AudioAssetForm(request.POST, request.FILES)
        if audioform.is_valid():
            audioaudio = audioform.save(commit=False)
            # retrieve the audiofacet the audio should be associated with
            audiofacet_id = request.POST.get('audiofacet')
            audiofacet = get_object_or_404(AudioFacet, id=audiofacet_id)
            # set request based attributes
            audioaudio.owner = request.user
            audioaudio.organization = request.user.organization
            audioaudio.save()
            # add audio asset to audiofacet audio_assets
            audiofacet.audio_assets.add(audioaudio)
            audiofacet.save()
    return redirect('story_detail', pk=audiofacet.story.id)


def upload_videofacet_audio(request):
    """ Add audio to a videofacet."""

    if request.method == 'POST':
        audioform=AudioAssetForm(request.POST, request.FILES)
        if audioform.is_valid():
            videoaudio = audioform.save(commit=False)
            # retrieve the videofacet the audio should be associated with
            videofacet_id = request.POST.get('videofacet')
            videofacet = get_object_or_404(VideoFacet, id=videofacet_id)
            # set request based attributes
            videoaudio.owner = request.user
            videoaudio.organization = request.user.organization
            vaudio.save()
            # add audio asset to videofacet audio_assets
            videofacet.audio_assets.add(videoaudio)
            videofacet.save()
    return redirect('story_detail', pk=videofacet.story.id)

#----------------------------------------------------------------------#
#   Add Audio Asset Views
#----------------------------------------------------------------------#

def add_webfacet_audio(request):
    """ Add existing audio(s) in the library to another webfacet."""

    if request.method == "POST":
        add_audio_form = AddAudioForm(request.POST, request=request)
        if add_audio_form.is_valid():
            webfacet_id = request.POST.get('webfacet')
            print "WEBFACETid: ", webfacet_id
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            audios = request.POST.getlist('audios')
            print "DOCS: ", audios
            for audio in audios:
                audio_ins = get_object_or_404(AudioAsset, id=audio)
                print "DOCins: ", audio_ins
                webfacet.audio_assets.add(audio_ins)
            webfacet.save()
    return redirect('story_detail', pk=webfacet.story.id)


def add_printfacet_audio(request):
    """ Add existing audio(s) in the library to another printfacet."""

    if request.method == "POST":
        add_audio_form = AddAudioForm(request.POST, request=request)
        if add_audio_form.is_valid():
            printfacet_id = request.POST.get('printfacet')
            print "WEBFACETid: ", printfacet_id
            printfacet = get_object_or_404(PrintFacet, id=printfacet_id)
            audios = request.POST.getlist('audios')
            print "DOCS: ", audios
            for audio in audios:
                audio_ins = get_object_or_404(AudioAsset, id=audio)
                print "DOCins: ", audio_ins
                printfacet.audio_assets.add(audio_ins)
            printfacet.save()
    return redirect('story_detail', pk=printfacet.story.id)


def add_audiofacet_audio(request):
    """ Add existing audio(s) in the library to another audiofacet."""

    if request.method == "POST":
        add_audio_form = AddAudioForm(request.POST, request=request)
        if add_audio_form.is_valid():
            audiofacet_id = request.POST.get('audiofacet')
            print "WEBFACETid: ", audiofacet_id
            audiofacet = get_object_or_404(AudioFacet, id=audiofacet_id)
            audios = request.POST.getlist('audios')
            print "DOCS: ", audios
            for audio in audios:
                audio_ins = get_object_or_404(AudioAsset, id=audio)
                print "DOCins: ", audio_ins
                audiofacet.audio_assets.add(audio_ins)
            audiofacet.save()
    return redirect('story_detail', pk=audiofacet.story.id)


def add_videofacet_audio(request):
    """ Add existing audio(s) in the library to another videofacet."""

    if request.method == "POST":
        add_audio_form = AddAudioForm(request.POST, request=request)
        if add_audio_form.is_valid():
            videofacet_id = request.POST.get('videofacet')
            print "WEBFACETid: ", videofacet_id
            videofacet = get_object_or_404(VideoFacet, id=videofacet_id)
            audios = request.POST.getlist('audios')
            print "DOCS: ", audios
            for audio in audios:
                audio_ins = get_object_or_404(AudioAsset, id=audio)
                print "DOCins: ", audio_ins
                videofacet.audio_assets.add(audio_ins)
            videofacet.save()
    return redirect('story_detail', pk=videofacet.story.id)

#----------------------------------------------------------------------#
#   Upload Video Asset Views
#----------------------------------------------------------------------#

def upload_webfacet_video(request):
    """ Add video to a webfacet."""

    print "In the function"
    if request.method == 'POST':
        print "POST"
        videoform=VideoAssetForm(request.POST, request.FILES)
        print videoform
        import pdb; pdb.set_trace()
        if videoform.is_valid():
            # retrieve the webfacet the video should be associated with
            webfacet_id = request.POST.get('webfacet')
            print "WF I: ", webfacet_id
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            print "WF: ", webfacet
            webvideo = videoform.save(commit=False)
            # set request based attributes
            webvideo.owner = request.user
            webvideo.organization = request.user.organization
            webvideo.save()
            # add video asset to webfacet video_assets
            webfacet.video_assets.add(webvideo)
            webfacet.save()
        else:
            print "VALID"
    return redirect('story_detail', pk=webfacet.story.id)

#----------------------------------------------------------------------#
#   Add Video Asset Views
#----------------------------------------------------------------------#

def add_webfacet_video(request):
    """ Add existing video(s) in the library to another webfacet."""

    if request.method == "POST":
        add_video_form = AddVideoForm(request.POST, request=request)
        if add_video_form.is_valid():
            webfacet_id = request.POST.get('webfacet')
            print "WEBFACETid: ", webfacet_id
            webfacet = get_object_or_404(WebFacet, id=webfacet_id)
            videos = request.POST.getlist('videos')
            print "DOCS: ", videos
            for video in videos:
                video_ins = get_object_or_404(VideoAsset, id=video)
                print "DOCins: ", video_ins
                webfacet.video_assets.add(video_ins)
            webfacet.save()
    return redirect('story_detail', pk=webfacet.story.id)
