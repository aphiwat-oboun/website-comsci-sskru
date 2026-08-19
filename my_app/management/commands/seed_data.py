from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from my_app.models import News, Course, Gallery, Admission, ContactInformation, Lecturer

class Command(BaseCommand):
    help = 'Populates the database with realistic sample data for CS Sisaket Rajabhat University'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # 1. Contact Information
        ContactInformation.objects.get_or_create(
            id=1,
            defaults={
                'dept_name': "สาขาวิทยาการคอมพิวเตอร์",
                'university': "มหาวิทยาลัยราชภัฏศรีสะเกษ",
                'address': "ชั้น 5 อาคาร LASC คณะศิลปศาสตร์และวิทยาศาสตร์ มหาวิทยาลัยราชภัฏศรีสะเกษ 319 ถ.ไทยพันทา ต.โพธิ์ อ.เมือง จ.ศรีสะเกษ 33000",
                'phone': "043-009700 ต่อ 50528",
                'email': "phisan.s@sskru.ac.th",
                'facebook': "https://www.facebook.com/comsci.sskru",
                'instagram': "https://www.instagram.com/cs_sskru",
                'youtube': "https://www.youtube.com/@CS_SSKRU",
                'tiktok': "https://www.tiktok.com/@comsciencesskru",
                'google_maps_url': "https://maps.google.com/maps?q=%E0%B8%95%E0%B8%B6%E0%B8%814%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A8%E0%B8%B4%E0%B8%A5%E0%B8%9B%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%20%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A5%E0%B8%B1%E0%B8%A2%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%A0%E0%B8%8F%E0%B8%A8%E0%B8%A3%E0%B8%B5%E0%B8%AA%E0%B8%B0%E0%B9%80%E0%B8%81%E0%B8%A9&t=&z=17&ie=UTF8&iwloc=&output=embed"
            }
        )

        # 2. Lecturers (หัวหน้าสาขาวิชาฯ อยู่บนสุด order=1)
        lecturers_data = [
            {
                'title': 'asst_prof_dr',
                'first_name': 'กนิษฐา',
                'last_name': 'อินธิชิต',
                'full_name_en': 'Kanittha Inthichit',
                'photo_url': 'https://comsci-sskru.vercel.app/_next/image?url=%2Fkanittha.jpg&w=256&q=75',
                'expertise': 'เทคโนโลยีสารสนเทศ',
                'icon_class': 'bi-database-fill',
                'role': 'อาจารย์ผู้รับผิดชอบหลักสูตร',
                'is_head': True,
                'order': 1,
                'is_active': True,
            },
            {
                'title': 'asst_prof_dr',
                'first_name': 'เจษฎา',
                'last_name': 'โพนแก้ว',
                'full_name_en': 'Jessada Phonkaew',
                'photo_url': 'https://comsci-sskru.vercel.app/_next/image?url=%2Fjessada_p.jpg&w=256&q=75',
                'expertise': 'วิทยาการคอมพิวเตอร์',
                'icon_class': 'bi-pc-display-horizontal',
                'role': 'อาจารย์ผู้รับผิดชอบหลักสูตร',
                'is_head': False,
                'order': 2,
                'is_active': True,
            },
            {
                'title': 'dr',
                'first_name': 'เจษฎา',
                'last_name': 'ชาตรี',
                'full_name_en': 'Jessada Chatree',
                'photo_url': 'https://comsci-sskru.vercel.app/_next/image?url=%2Fjessada_c.jpg&w=256&q=75',
                'expertise': 'Computer Science and Engineering',
                'icon_class': 'bi-code-square',
                'role': 'อาจารย์ผู้รับผิดชอบหลักสูตร',
                'is_head': False,
                'order': 3,
                'is_active': True,
            },
            {
                'title': 'dr',
                'first_name': 'กริชบดินทร์',
                'last_name': 'ผิวหอม',
                'full_name_en': 'Krichbodin Phewhom',
                'photo_url': 'https://comsci-sskru.vercel.app/_next/image?url=%2Fkrichbodin.jpg&w=256&q=75',
                'expertise': 'วิศวกรรมคอมพิวเตอร์',
                'icon_class': 'bi-robot',
                'role': 'อาจารย์ผู้รับผิดชอบหลักสูตร',
                'is_head': False,
                'order': 4,
                'is_active': True,
            },
            {
                'title': 'asst_prof',
                'first_name': 'พิศาล',
                'last_name': 'สุขขี',
                'full_name_en': 'Phisan Sukkee',
                'photo_url': 'https://comsci-sskru.vercel.app/_next/image?url=%2Fphisan.jpg&w=256&q=75',
                'expertise': 'วิทยาการคอมพิวเตอร์',
                'icon_class': 'bi-terminal-fill',
                'role': 'อาจารย์ผู้รับผิดชอบหลักสูตร',
                'is_head': False,
                'order': 5,
                'is_active': True,
            },
        ]

        for item in lecturers_data:
            Lecturer.objects.get_or_create(
                first_name=item['first_name'],
                last_name=item['last_name'],
                defaults=item
            )

        # 3. Courses
        courses_data = [
            {
                'name': 'วิทยาการคอมพิวเตอร์ (Computer Science)',
                'description': 'เน้นการพัฒนาซอฟต์แวร์ อัลกอริทึม การออกแบบระบบ ปัญญาประดิษฐ์ และการแก้ปัญหาทางคอมพิวเตอร์ระดับสูง เพื่อก้าวสู่การเป็น Full-Stack Developer และ Software Engineer มืออาชีพ',
                'duration': '4 ปี (133 หน่วยกิต)',
                'degree': 'วิทยาศาสตรบัณฑิต (วท.บ.)',
                'image': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80',
                'icon_class': 'bi-code-slash',
                'tech_tags': 'Python Java Web-Dev Algorithms Cloud',
                'is_active': True
            },
            {
                'name': 'เทคโนโลยีสารสนเทศ (Information Technology)',
                'description': 'มุ่งเน้นการจัดการระบบเครือข่ายความเร็วสูง การบริหารจัดการฐานข้อมูลขนาดใหญ่ และการประยุกต์ใช้ไอทีในการขับเคลื่อนองค์กรยุคดิจิทัล',
                'duration': '4 ปี (133 หน่วยกิต)',
                'degree': 'วิทยาศาสตรบัณฑิต (วท.บ.)',
                'image': 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=800&q=80',
                'icon_class': 'bi-hdd-network',
                'tech_tags': 'Network Cloud-Computing Database DevOps',
                'is_active': True
            },
            {
                'name': 'วิทยาการข้อมูลและปัญญาประดิษฐ์ (Data Science & AI)',
                'description': 'เจาะลึกการวิเคราะห์ข้อมูลขนาดใหญ่ (Big Data), Machine Learning, Deep Learning และการสร้างโมเดล AI เพื่อทำนายและวิเคราะห์ข้อมูลทางธุรกิจ',
                'duration': '4 ปี (133 หน่วยกิต)',
                'degree': 'วิทยาศาสตรบัณฑิต (วท.บ.)',
                'image': 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&w=800&q=80',
                'icon_class': 'bi-cpu',
                'tech_tags': 'Python ML Data-Analytics PyTorch SQL',
                'is_active': True
            },
            {
                'name': 'ความมั่นคงปลอดภัยไซเบอร์ (Cyber Security)',
                'description': 'เรียนรู้ระบบรักษาความปลอดภัยซอฟต์แวร์และเครือข่าย การทดสอบเจาะระบบ (Ethical Hacking) การป้องกันภัยคุกคามไซเบอร์ และ Digital Forensics',
                'duration': '4 ปี (133 หน่วยกิต)',
                'degree': 'วิทยาศาสตรบัณฑิต (วท.บ.)',
                'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=800&q=80',
                'icon_class': 'bi-shield-lock',
                'tech_tags': 'Ethical-Hacking Network-Security Forensics Cryptography',
                'is_active': True
            },
        ]

        for item in courses_data:
            Course.objects.get_or_create(name=item['name'], defaults=item)

        # 4. News
        news_data = [
            {
                'title': 'นักศึกษาวิทยาการคอมพิวเตอร์ SSKRU คว้ารางวัลชนะเลิศ Hackathon ระดับภาคอีสาน',
                'slug': 'cs-sskru-wins-hackathon-2026',
                'description': 'ทีม CS SSKRU พัฒนาแอปพลิเคชันปัญญาประดิษฐ์ช่วยวิเคราะห์การเกษตร คว้ารางวัลชนะเลิศอันดับ 1 พร้อมเงินรางวัล 50,000 บาท',
                'content': '<p>เมื่อวันที่ 12 สิงหาคม 2569 สาขาวิทยาการคอมพิวเตอร์ มหาวิทยาลัยราชภัฏศรีสะเกษ ได้ส่งตัวแทนนักศึกษาเข้าร่วมการแข่งขัน Hackathon นวัตกรรมเทคโนโลยีดิจิทัลระดับภาคอีสาน</p><p>ผลการแข่งขัน ปรากฏว่าทีม CS SSKRU สามารถคว้าชัยชนะอันดับ 1 ด้วยผลงานระบบตรวจจับโรคพืชด้วย AI บน Mobile Application</p>',
                'image': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=800&q=80',
                'category': 'contest',
                'is_published': True
            },
            {
                'title': 'โครงการอบรมเชิงปฏิบัติการ Full-Stack Web Development with Django',
                'slug': 'workshop-fullstack-django-2026',
                'description': 'สาขาวิทยาการคอมพิวเตอร์จัดอบรมการเขียนเว็บแอปพลิเคชันยุคใหม่แก่นักศึกษาชั้นปีที่ 1-4 ฟรีตลอดหลักสูตร',
                'content': '<p>สาขาวิทยาการคอมพิวเตอร์ จัดกิจกรรมพัฒนาทักษะวิชาการและการปฏิบัติงานจริง ในหัวข้อ Full-Stack Web Development</p>',
                'image': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80',
                'category': 'workshop',
                'is_published': True
            },
            {
                'title': 'เปิดบ้าน CS SSKRU Open House 2569 ต้อนรับน้องๆ มัธยมปลายทั่วภาคอีสาน',
                'slug': 'cs-sskru-open-house-2026',
                'description': 'สัมผัสประสบการณ์การเรียนโค้ดดิ้ง ทดลองขับเคลื่อนหุ่นยนต์ AI และร่วมเวิร์กชอปสร้างเกมด้วย Python',
                'content': '<p>บรรยากาศงาน Open House สาขาวิทยาการคอมพิวเตอร์ มหาวิทยาลัยราชภัฏศรีสะเกษ เป็นไปอย่างคึกคัก มีน้องๆ นักเรียนมัธยมเข้าร่วมกว่า 500 คน</p>',
                'image': 'https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&w=800&q=80',
                'category': 'activity',
                'is_published': True
            },
            {
                'title': 'โชว์เคสผลงานภาคนิพนธ์นักศึกษาปี 4 ซอฟต์แวร์และ AI สำหรับองค์กรจริง',
                'slug': 'senior-project-showcase-2026',
                'description': 'ชมนวัตกรรมระบบบริหารจัดการโรงพยาบาล ระบบตรวจจับใบหน้า และ IoT สมาร์ตฟาร์มจากฝีมือนักศึกษา CS SSKRU',
                'content': '<p>สาขาวิชาวิทยาการคอมพิวเตอร์ จัดนิทรรศการแสดงผลงานภาคนิพนธ์นักศึกษาชั้นปีที่ 4 Senior Project Showcase</p>',
                'image': 'https://images.unsplash.com/photo-1515187029135-18ee286d815b?auto=format&fit=crop&w=800&q=80',
                'category': 'showcase',
                'is_published': True
            },
            {
                'title': 'CS SSKRU จับมือบริษัทไอทีชั้นนำเปิดรับนักศึกษาฝึกงานและทำงานตรงสาย 100%',
                'slug': 'cs-sskru-mou-tech-partners',
                'description': 'ลงนามความร่วมมือ (MOU) ด้านเทคโนโลยีซอฟต์แวร์ เพิ่มโอกาสให้นักศึกษาได้ฝึกงานจริงกับบริษัทระดับประเทศ',
                'content': '<p>ความร่วมมือระหว่างมหาวิทยาลัยและภาคเอกชน ช่วยส่งเสริมนักศึกษาสาขาวิทยาการคอมพิวเตอร์</p>',
                'image': 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=800&q=80',
                'category': 'news',
                'is_published': True
            },
        ]

        for item in news_data:
            News.objects.get_or_create(slug=item['slug'], defaults=item)

        # 5. Gallery
        gallery_data = [
            {'title': 'บรรยากาศกิจกรรม Coding BootCamp', 'image': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=800&q=80', 'category': 'coding'},
            {'title': 'อบรมเชิงปฏิบัติการ AI & Machine Learning', 'image': 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&w=800&q=80', 'category': 'ai'},
            {'title': 'การแข่งขัน Hackathon SSKRU Tech 2026', 'image': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80', 'category': 'hackathon'},
            {'title': 'บรรยากาศการเรียนในห้องปฏิบัติการคอมพิวเตอร์', 'image': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80', 'category': 'activities'},
            {'title': 'ผลงานหุ่นยนต์และ IoT สมาร์ตฟาร์ม', 'image': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=800&q=80', 'category': 'project'},
            {'title': 'ทีมนักศึกษาคว้ารางวัลระดับประเทศ', 'image': 'https://images.unsplash.com/photo-1511632765486-a01980e01a18?auto=format&fit=crop&w=800&q=80', 'category': 'competition'},
            {'title': 'Workshop Cybersecurity & Penetration Testing', 'image': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=800&q=80', 'category': 'workshop'},
            {'title': 'กิจกรรมต้อนรับน้องใหม่ CS Freshy Day', 'image': 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=800&q=80', 'category': 'activities'},
        ]

        for item in gallery_data:
            Gallery.objects.get_or_create(title=item['title'], defaults=item)

        # 6. Admission
        today = date.today()
        admission_data = [
            {
                'title': 'รอบที่ 1 Portfolio (แฟ้มสะสมผลงาน)',
                'description': 'พิจารณาจากแฟ้มสะสมผลงาน เกรดเฉลี่ยสะสม (GPAX) และผลงานด้านเทคโนโลยี/คอมพิวเตอร์ที่เคยเข้าร่วม เหมาะสำหรับนักเรียนที่มีความสนใจด้านเขียนโค้ด',
                'start_date': today - timedelta(days=30),
                'end_date': today + timedelta(days=15),
                'link': 'https://www.oass.sskru.ac.th/std.sskru/s1.html',
                'is_active': True
            },
            {
                'title': 'รอบที่ 2 Quota (โควตาภาคตะวันออกเฉียงเหนือ)',
                'description': 'เปิดรับสมัครนักเรียนในเขตพื้นที่ภาคอีสาน พิจารณาจากผลการเรียนและทักษะพื้นฐาน ไม่ต้องใช้คะแนนสอบส่วนกลางซับซ้อน',
                'start_date': today + timedelta(days=20),
                'end_date': today + timedelta(days=60),
                'link': 'https://www.oass.sskru.ac.th/std.sskru/s1.html',
                'is_active': True
            },
            {
                'title': 'รอบที่ 3 Admission (รับตรงร่วมกัน)',
                'description': 'ยื่นคะแนนสอบกลางตามเกณฑ์ที่กำหนด เลือกสาขาวิทยาการคอมพิวเตอร์ มหาวิทยาลัยราชภัฏศรีสะเกษ ได้โดยตรง',
                'start_date': today + timedelta(days=70),
                'end_date': today + timedelta(days=100),
                'link': 'https://www.oass.sskru.ac.th/std.sskru/s1.html',
                'is_active': True
            },
            {
                'title': 'รอบที่ 4 รายงานตัว & รับตรงอิสระ (Direct Admission)',
                'description': 'รอบเก็บตกสำหรับผู้ที่ต้องการเข้าศึกษาตรง ยื่นเอกสารและสอบสัมภาษณ์กับอาจารย์ประจำสาขาโดยตรง',
                'start_date': today + timedelta(days=105),
                'end_date': today + timedelta(days=130),
                'link': 'https://www.oass.sskru.ac.th/std.sskru/s1.html',
                'is_active': True
            },
        ]

        for item in admission_data:
            Admission.objects.get_or_create(title=item['title'], defaults=item)

        self.stdout.write(self.style.SUCCESS('Successfully seeded all data including lecturers!'))
