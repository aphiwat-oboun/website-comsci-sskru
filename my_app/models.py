from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class News(models.Model):
    CATEGORY_CHOICES = [
        ('news', 'ข่าวสาร'),
        ('activity', 'กิจกรรม'),
        ('showcase', 'ผลงานนักศึกษา'),
        ('contest', 'การแข่งขัน'),
        ('workshop', 'อบรม'),
    ]

    title = models.CharField(max_length=255, verbose_name="หัวข้อข่าว")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL Slug")
    description = models.TextField(verbose_name="คำอธิบายย่อ")
    content = models.TextField(verbose_name="เนื้อหาข่าวแบบละเอียด")
    image = models.CharField(max_length=500, blank=True, default="", verbose_name="รูปภาพประกอบ (URL/Static)")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='news', verbose_name="หมวดหมู่")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="วันที่เผยแพร่")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="อัปเดตล่าสุด")
    is_published = models.BooleanField(default=True, verbose_name="เผยแพร่")

    class Meta:
        verbose_name = "ข่าวสารและกิจกรรม"
        verbose_name_plural = "ข่าวสารและกิจกรรม"
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            clean_title = slugify(self.title)
            base_slug = clean_title if clean_title else "news"
            slug = base_slug
            count = 1
            while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="ชื่อหลักสูตร")
    description = models.TextField(verbose_name="คำอธิบายหลักสูตร")
    duration = models.CharField(max_length=100, default="4 ปี", verbose_name="ระยะเวลาศึกษา")
    degree = models.CharField(max_length=255, default="วิทยาศาสตรบัณฑิต (วท.บ.)", verbose_name="ชื่อปริญญา")
    image = models.CharField(max_length=500, blank=True, default="", verbose_name="ภาพประกอบหลักสูตร")
    icon_class = models.CharField(max_length=100, default="bi-code-slash", verbose_name="Bootstrap Icon Class")
    tech_tags = models.CharField(max_length=255, default="Python, Web, Cloud, AI", verbose_name="เทคโนโลยีที่เรียน")
    is_active = models.BooleanField(default=True, verbose_name="เปิดสอนอยู่")

    class Meta:
        verbose_name = "หลักสูตร"
        verbose_name_plural = "หลักสูตร"

    def __str__(self):
        return self.name


class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('coding', 'Coding & Development'),
        ('workshop', 'Workshop'),
        ('hackathon', 'Hackathon'),
        ('competition', 'การแข่งขัน'),
        ('ai', 'AI & Robotics'),
        ('project', 'โครงงานนักศึกษา'),
        ('activities', 'กิจกรรมสาขา'),
    ]

    title = models.CharField(max_length=255, verbose_name="ชื่อกิจกรรม/รูปภาพ")
    image = models.CharField(max_length=500, verbose_name="URL/Path รูปภาพ")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='activities', verbose_name="หมวดหมู่")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่เพิ่ม")

    class Meta:
        verbose_name = "แกลเลอรีภาพ"
        verbose_name_plural = "แกลเลอรีภาพ"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Admission(models.Model):
    title = models.CharField(max_length=255, verbose_name="รอบการรับสมัคร (เช่น TCAS 1 Portfolio)")
    description = models.TextField(verbose_name="รายละเอียดการรับสมัคร")
    start_date = models.DateField(verbose_name="วันเริ่มเปิดรับสมัคร")
    end_date = models.DateField(verbose_name="วันสิ้นสุดรับสมัคร")
    link = models.URLField(blank=True, default="https://admission.sskru.ac.th", verbose_name="ลิงก์ระบบรับสมัคร")
    is_active = models.BooleanField(default=True, verbose_name="เปิดรับสมัครอยู่")

    class Meta:
        verbose_name = "ข้อมูลการรับสมัคร"
        verbose_name_plural = "ข้อมูลการรับสมัคร"
        ordering = ['start_date']

    def __str__(self):
        return self.title


class ContactInformation(models.Model):
    dept_name = models.CharField(max_length=255, default="สาขาวิทยาการคอมพิวเตอร์", verbose_name="ชื่อสาขา")
    university = models.CharField(max_length=255, default="มหาวิทยาลัยราชภัฏศรีสะเกษ", verbose_name="ชื่อมหาวิทยาลัย")
    address = models.TextField(default="319 ถนนไทยพันทา ตำบลโพธิ์ อำเภอเมืองศรีสะเกษ จังหวัดศรีสะเกษ 33000", verbose_name="ที่อยู่")
    phone = models.CharField(max_length=100, default="045-643600 ต่อ 1234", verbose_name="เบอร์โทรศัพท์")
    email = models.EmailField(default="cs@sskru.ac.th", verbose_name="อีเมล")
    facebook = models.URLField(default="https://www.facebook.com/ComputerScienceSSKRU", verbose_name="Facebook Page")
    instagram = models.URLField(default="https://www.instagram.com/cs_sskru", verbose_name="Instagram")
    youtube = models.URLField(default="https://www.youtube me.com/@CS_SSKRU", verbose_name="YouTube")
    tiktok = models.URLField(default="https://www.tiktok.com/@cs_sskru", verbose_name="TikTok")
    google_maps_url = models.TextField(default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3862.684347585098!2d104.3315!3d15.1189!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3116e254e2f9d8ab%3A0x4464c20d75a894b9!2z4Lih4Lir4Liy4Lin4Li04LiX4Lii4Liy4Lil4Lix4Lii4Lij4Liy4LiK4Lmg4Lij4LmE4LiU4Lih4Liy4Lio4Lij4Li14LiB4Li14Lih4LmM!5e0!3m2!1sth!2sth!4v1700000000000!5m2!1sth!2sth", verbose_name="Google Maps Embed URL")

    class Meta:
        verbose_name = "ข้อมูลการติดต่อสาขา"
        verbose_name_plural = "ข้อมูลการติดต่อสาขา"

    def __str__(self):
        return f"{self.dept_name} - {self.university}"


class Lecturer(models.Model):
    TITLE_CHOICES = [
        ('asst_prof_dr', 'ผู้ช่วยศาสตราจารย์ ดร.'),
        ('asst_prof', 'ผู้ช่วยศาสตราจารย์'),
        ('assoc_prof_dr', 'รองศาสตราจารย์ ดร.'),
        ('dr', 'ดร.'),
        ('mr', 'อาจารย์'),
    ]

    title = models.CharField(max_length=30, choices=TITLE_CHOICES, default='dr', verbose_name="คำนำหน้า/ตำแหน่ง")
    first_name = models.CharField(max_length=100, verbose_name="ชื่อ (ภาษาไทย)")
    last_name = models.CharField(max_length=100, verbose_name="นามสกุล (ภาษาไทย)")
    full_name_en = models.CharField(max_length=200, blank=True, default="", verbose_name="ชื่อ-นามสกุล (ภาษาอังกฤษ)")
    photo_url = models.CharField(max_length=500, blank=True, default="", verbose_name="URL รูปภาพ")
    expertise = models.CharField(max_length=255, default="วิทยาการคอมพิวเตอร์", verbose_name="ความเชี่ยวชาญ")
    icon_class = models.CharField(max_length=100, default="bi-person-fill", verbose_name="Bootstrap Icon")
    role = models.CharField(max_length=200, default="อาจารย์ผู้รับผิดชอบหลักสูตร", verbose_name="บทบาทในหลักสูตร")
    is_head = models.BooleanField(default=False, verbose_name="หัวหน้าสาขาวิชาฯ")
    profile_link = models.URLField(blank=True, default="", verbose_name="ลิงก์ประวัติวิชาการ")
    order = models.PositiveIntegerField(default=99, verbose_name="ลำดับการแสดงผล")
    is_active = models.BooleanField(default=True, verbose_name="แสดงบนเว็บไซต์")

    class Meta:
        verbose_name = "อาจารย์ประจำหลักสูตร"
        verbose_name_plural = "อาจารย์ประจำหลักสูตร"
        ordering = ['order', 'last_name']

    def __str__(self):
        return f"{self.get_title_display()}{self.first_name} {self.last_name}"

    @property
    def full_name_th(self):
        return f"{self.get_title_display()}{self.first_name} {self.last_name}"

