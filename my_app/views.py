from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import News, Course, Gallery, Admission, ContactInformation, Lecturer

_cached_contact = None

def get_contact_info():
    global _cached_contact
    if _cached_contact is None:
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
                google_maps_url="https://maps.google.com/maps?q=%E0%B8%95%E0%B8%B6%E0%B8%814%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A8%E0%B8%B4%E0%B8%A5%E0%B8%9B%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8Call%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%20%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%20%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A5%E0%B8%B1%E0%B8%A2%E0%B8%A3%E0%B8%B2%E0%B8%88%E0%B8%A0%E0%B8%B1%E0%B8%8F%E0%B8%A8%E0%B8%B5%E0%B8%AA%E0%B8%B0%E0%B9%80%E0%B8%81%E0%B8%A9&t=&z=17&ie=UTF8&iwloc=&output=embed"
            )
        _cached_contact = info
    return _cached_contact

def home_view(request):
    latest_news = News.objects.filter(is_published=True).order_by('-published_at')[:4]
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
    news_list = News.objects.filter(is_published=True).order_by('-published_at')
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
    # ดึงรูปจากโฟลเดอร์ statics/images/activities โดยตรง
    activities_dir = settings.BASE_DIR / 'statics' / 'images' / 'activities'
    gallery_items = []
    
    # รายการชื่อหัวข้อของภาพกิจกรรม
    activity_titles = {
        'activity_01.jpg': 'การแข่งขันหุ่นยนต์เยาวชน ศรีสะเกษโรโบติกส์ (Sisaket Robotics)',
        'activity_02.jpg': 'การอบรมเชิงปฏิบัติการ Generative AI & Machine Learning',
        'activity_03.jpg': 'โครงการพัฒนาทักษะการเขียนโปรแกรมและการพัฒนาเว็บแอปพลิเคชัน',
        'activity_04.jpg': 'นิทรรศการแสดงผลงานโครงงานนวัตกรรมซอฟต์แวร์ของนักศึกษา',
        'activity_05.jpg': 'กิจกรรมบายศรีสู่ขวัญ ต้อนรับนักศึกษาใหม่ CS SSKRU',
        'activity_06.jpg': 'เปิดรับสมัครนักศึกษาใหม่ สาขาวิชาวิทยาการคอมพิวเตอร์ (วท.บ.)',
        'activity_07.jpg': 'กิจกรรมศึกษาดูงานด้านเทคโนโลยีศูนย์ดิจิทัล (Tech Field Trip)',
        'activity_08.jpg': 'กิจกรรมบริการวิชาการถ่ายทอดทักษะโค้ดดิ้งแก่นักเรียน',
        'activity_09.jpg': 'บรรยากาศการเรียนในห้องปฏิบัติการคอมพิวเตอร์',
        'activity_10.jpg': 'การฝึกอบรมและสอบวัดสมรรถนะมาตรฐานวิชาชีพไอที',
        'robotics_01.jpg': 'การแข่งขันหุ่นยนต์ Sisaket Robotics Championship',
    }
    
    if activities_dir.exists():
        valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
        for file_path in sorted(activities_dir.iterdir()):
            if file_path.suffix.lower() in valid_extensions:
                file_name = file_path.name
                title = activity_titles.get(
                    file_name,
                    file_path.stem.replace('_', ' ').replace('-', ' ').title()
                )
                gallery_items.append({
                    'title': title,
                    'image': f'/static/images/activities/{file_name}',
                    'get_category_display': 'กิจกรรมสาขาวิชา',
                })
    
    # หากในโฟลเดอร์ไม่มีรูป ให้ดึงจากฐานข้อมูลสำรอง
    if not gallery_items:
        gallery_items = list(Gallery.objects.all())
        
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
