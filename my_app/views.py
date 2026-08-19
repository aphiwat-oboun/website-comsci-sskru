from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import News, Course, Gallery, Admission, ContactInformation, Lecturer

def get_contact_info():
    info = ContactInformation.objects.first()
    if not info:
        info = ContactInformation(
            dept_name="สาขาวิทยาการคอมพิวเตอร์",
            university="มหาวิทยาลัยราชภัฏศรีสะเกษ",
            address="ชั้น 5 อาคารสำนักงานคณบดี คณะศิลปศาสตร์และวิทยาศาสตร์ (LASC) มรภ.ศรีสะเกษ ถ.ไทยพันทา อ.เมือง จ.ศรีสะเกษ 33000",
            phone="043-009700 ต่อ 50528",
            email="phisan.s@sskru.ac.th",
            facebook="https://www.facebook.com/comsci.sskru",
            instagram="https://www.instagram.com/cs_sskru",
            youtube="https://www.youtube.com/@CS_SSKRU",
            tiktok="https://www.tiktok.com/@comsciencesskru",
            google_maps_url="https://maps.google.com/maps?q=%E0%B8%95%E0%B8%B6%E0%B8%814%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A8%E0%B8%B4%E0%B8%A5%E0%B8%9B%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8Call%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%20%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A5%E0%B8%B1%E0%B8%A2%E0%B8%A3%E0%B8%B2%E0%B8%88%E0%B8%A0%E0%B8%B1%E0%B8%8F%E0%B8%A8%E0%B8%B5%E0%B8%AA%E0%B8%B0%E0%B9%80%E0%B8%81%E0%B8%A9&t=&z=17&ie=UTF8&iwloc=&output=embed"
        )
    return info

def home_view(request):
    latest_news = News.objects.filter(is_published=True)[:4]
    courses = Course.objects.filter(is_active=True)
    active_admissions = Admission.objects.filter(is_active=True)
    gallery_preview = Gallery.objects.all()[:6]
    lecturers = Lecturer.objects.filter(is_active=True).order_by('order', 'last_name')
    contact = get_contact_info()

    context = {
        'latest_news': latest_news,
        'courses': courses,
        'active_admissions': active_admissions,
        'gallery_preview': gallery_preview,
        'lecturers': lecturers,
        'contact': contact,
        'active_page': 'home',
    }
    return render(request, 'home.html', context)

def about_view(request):
    lecturers = Lecturer.objects.filter(is_active=True).order_by('order', 'last_name')
    contact = get_contact_info()
    context = {
        'lecturers': lecturers,
        'contact': contact,
        'active_page': 'about',
    }
    return render(request, 'about.html', context)

def curriculum_view(request):
    courses = Course.objects.filter(is_active=True)
    contact = get_contact_info()
    context = {
        'courses': courses,
        'contact': contact,
        'active_page': 'curriculum',
    }
    return render(request, 'curriculum.html', context)

def news_view(request):
    news_list = News.objects.filter(is_published=True)
    contact = get_contact_info()
    context = {
        'news_list': news_list,
        'contact': contact,
        'active_page': 'news',
    }
    return render(request, 'news.html', context)

def news_detail_view(request, slug):
    news_item = get_object_or_404(News, slug=slug, is_published=True)
    contact = get_contact_info()
    context = {
        'news_item': news_item,
        'contact': contact,
        'active_page': 'news',
    }
    return render(request, 'news_detail.html', context)

def gallery_view(request):
    gallery_items = Gallery.objects.all()
    contact = get_contact_info()
    context = {
        'gallery_items': gallery_items,
        'contact': contact,
        'active_page': 'gallery',
    }
    return render(request, 'gallery.html', context)

def admission_view(request):
    admissions = Admission.objects.filter(is_active=True)
    contact = get_contact_info()
    context = {
        'admissions': admissions,
        'contact': contact,
        'active_page': 'admission',
    }
    return render(request, 'admission.html', context)

def contact_view(request):
    contact = get_contact_info()
    context = {
        'contact': contact,
        'active_page': 'contact',
    }
    return render(request, 'contact.html', context)
