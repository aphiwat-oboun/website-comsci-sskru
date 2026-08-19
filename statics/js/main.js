/**
 * CS SSKRU - Innovative Futuristic Interactive Engine
 * Golden 2-Column Academic Dossier & Seamless Modular Experience
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Island Header & Back-To-Top
  const siteHeader = document.querySelector('.futuristic-header');
  const backToTopBtn = document.getElementById('backToTopBtn');

  window.addEventListener('scroll', () => {
    const pos = window.scrollY;
    if (siteHeader) {
      if (pos > 35) siteHeader.classList.add('scrolled');
      else siteHeader.classList.remove('scrolled');
    }
    if (backToTopBtn) {
      if (pos > 400) backToTopBtn.classList.add('visible');
      else backToTopBtn.classList.remove('visible');
    }
  }, { passive: true });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 2. Mobile Side Offcanvas Drawer Toggle
  const navToggleBtn = document.getElementById('navToggleBtn');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  const mobileDrawerBackdrop = document.getElementById('mobileDrawerBackdrop');
  const mobileDrawerClose = document.getElementById('mobileDrawerClose');

  const openMobileDrawer = () => {
    if (mobileNavDrawer) mobileNavDrawer.classList.add('show');
    if (mobileDrawerBackdrop) mobileDrawerBackdrop.classList.add('show');
    document.body.style.overflow = 'hidden';
  };

  const closeMobileDrawer = () => {
    if (mobileNavDrawer) mobileNavDrawer.classList.remove('show');
    if (mobileDrawerBackdrop) mobileDrawerBackdrop.classList.remove('show');
    document.body.style.overflow = '';
  };

  if (navToggleBtn) {
    navToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (mobileNavDrawer && mobileNavDrawer.classList.contains('show')) {
        closeMobileDrawer();
      } else {
        openMobileDrawer();
      }
    });
  }

  if (mobileDrawerClose) {
    mobileDrawerClose.addEventListener('click', closeMobileDrawer);
  }

  if (mobileDrawerBackdrop) {
    mobileDrawerBackdrop.addEventListener('click', closeMobileDrawer);
  }

  if (mobileNavDrawer) {
    mobileNavDrawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', closeMobileDrawer);
    });
  }

  // 3. Robust ScrollSpy Engine (Zero Mismatch) - Syncs Desktop & Mobile Bottom Bar
  const navPills = document.querySelectorAll('.nav-pill-item');
  const mobileTabs = document.querySelectorAll('.mobile-tab-item');
  const sections = Array.from(document.querySelectorAll('section[id]'));

  const updateScrollSpy = () => {
    const scrollPosition = window.scrollY + 110;
    let currentId = null;

    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 60) {
      if (sections.length > 0) currentId = sections[sections.length - 1].getAttribute('id');
    } else {
      sections.forEach(sec => {
        const top = sec.offsetTop;
        const height = sec.offsetHeight;
        if (scrollPosition >= top && scrollPosition < top + height) {
          currentId = sec.getAttribute('id');
        }
      });
    }

    if (currentId) {
      navPills.forEach(pill => {
        const href = pill.getAttribute('href') || '';
        if (href.endsWith(`#${currentId}`) || (currentId === 'hero' && (href === '/' || href.endsWith('/#hero')))) {
          pill.classList.add('active');
        } else {
          pill.classList.remove('active');
        }
      });

      mobileTabs.forEach(tab => {
        const target = tab.getAttribute('data-tab');
        const href = tab.getAttribute('href') || '';
        if (target === currentId || href.endsWith(`#${currentId}`) || (currentId === 'hero' && (target === 'hero' || href === '/'))) {
          tab.classList.add('active');
        } else {
          tab.classList.remove('active');
        }
      });
    }
  };

  if (sections.length > 0) {
    window.addEventListener('scroll', updateScrollSpy, { passive: true });
    updateScrollSpy();
  }

  // 4. Interactive 4-Year Skill-Tree Stepper
  const skillNodes = document.querySelectorAll('.skilltree-node-btn');
  const skillPanels = document.querySelectorAll('.skilltree-quest-pane');

  skillNodes.forEach(node => {
    node.addEventListener('click', () => {
      const targetYear = node.getAttribute('data-year');
      skillNodes.forEach(n => n.classList.remove('active'));
      node.classList.add('active');

      skillPanels.forEach(panel => {
        if (panel.id === `quest-pane-${targetYear}`) {
          panel.style.display = 'block';
        } else {
          panel.style.display = 'none';
        }
      });
    });
  });

  // 5. Strategic About Segmented Controller
  const segmentedTriggers = document.querySelectorAll('.segmented-pill-trigger');
  const strategicPanes = document.querySelectorAll('.strategic-pane-item');

  segmentedTriggers.forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = btn.getAttribute('data-tab');
      segmentedTriggers.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      strategicPanes.forEach(pane => {
        if (pane.id === `strategic-pane-${tab}`) {
          pane.style.display = 'block';
        } else {
          pane.style.display = 'none';
        }
      });
    });
  });

  // 6. Curriculum Track Filter
  const trackButtons = document.querySelectorAll('.track-tab-btn, .track-filter-btn');
  const trackDisplays = document.querySelectorAll('.track-display-box');

  trackButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const track = btn.getAttribute('data-track');
      trackButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      trackDisplays.forEach(box => {
        if (box.id === `track-box-${track}`) {
          box.style.display = 'block';
        } else {
          box.style.display = 'none';
        }
      });
    });
  });

  // 7. Golden 2-Column Academic Dossier Engine (Matching & Improving User Reference)
  const facultyData = {
    "5": {
      name: "ผู้ช่วยศาสตราจารย์ ดร.กนิษฐา อินธิชิต",
      nameEn: "Asst. Prof. Dr. Kanittha Inthichit",
      role: "หัวหน้าสาขาวิชาฯ · อาจารย์ผู้รับผิดชอบหลักสูตร",
      expertise: "เทคโนโลยีสารสนเทศ",
      email: "kanittha.i@sskru.ac.th",
      office: "ห้องพักอาจารย์สาขาวิทยาการคอมพิวเตอร์ ชั้น 5 อาคาร LASC",
      image: "/static/images/kanittha.jpg",
      education: [
        { degree: "ปร.ด. (การจัดการเทคโนโลยี)", school: "มหาวิทยาลัยราชภัฏมหาสารคาม", year: "พ.ศ. 2561" },
        { degree: "วท.ม. (เทคโนโลยีสารสนเทศการเกษตรและพัฒนาชนบท)", school: "มหาวิทยาลัยอุบลราชธานี", year: "พ.ศ. 2550" },
        { degree: "วท.บ. (วิทยาการคอมพิวเตอร์)", school: "มหาวิทยาลัยราชภัฏมหาสารคาม", year: "พ.ศ. 2546" }
      ],
      courses: [
        { code: "4123202", name: "ระบบฐานข้อมูล", credits: "3(2-2-5)" },
        { code: "4122506", name: "การวิเคราะห์และออกแบบระบบเชิงวัตถุ", credits: "3(2-2-5)" },
        { code: "4123665", name: "เทคโนโลยีท้องถิ่น", credits: "3(2-2-5)" },
        { code: "4124920", name: "โครงงานทางวิทยาการคอมพิวเตอร์", credits: "3(0-6-3)" }
      ],
      research: [
        {
          title: "การพัฒนาแอปพลิเคชันช่วยตัดสินใจในการเลือกเรียนสาขาวิชาคอมพิวเตอร์ในมหาวิทยาลัยราชภัฏศรีสะเกษบนระบบปฏิบัติการแอนดรอยด์ โดยใช้เทคนิคต้นไม้ตัดสินใจ",
          author: "กนิษฐา อินธิชิต",
          year: "พ.ศ. 2566",
          journal: "วารสารวิชาการการจัดการเทคโนโลยี มหาวิทยาลัยราชภัฏมหาสารคาม ปีที่ 10 ฉบับที่ 1 หน้า 32-39"
        },
        {
          title: "ระบบสารสนเทศเพื่อการบริหารจัดการข้อมูลชุมชนท้องถิ่นและการบูรณาการข้อมูลดิจิทัล",
          author: "กนิษฐา อินธิชิต",
          year: "พ.ศ. 2565",
          journal: "วารสารวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏศรีสะเกษ"
        }
      ]
    },
    "1": {
      name: "ผู้ช่วยศาสตราจารย์ ดร.เจษฎา โพนแก้ว",
      nameEn: "Asst. Prof. Dr. Jessada Phonkaew",
      role: "อาจารย์ผู้รับผิดชอบหลักสูตร",
      expertise: "วิทยาการคอมพิวเตอร์",
      email: "jessada.p@sskru.ac.th",
      office: "ห้องพักอาจารย์สาขาวิทยาการคอมพิวเตอร์ ชั้น 5 อาคาร LASC",
      image: "/static/images/jessada_p.jpg",
      education: [
        { degree: "ปร.ด. (วิทยาการคอมพิวเตอร์)", school: "มหาวิทยาลัยขอนแก่น", year: "พ.ศ. 2557" },
        { degree: "วท.ม. (วิทยาการคอมพิวเตอร์)", school: "มหาวิทยาลัยขอนแก่น", year: "พ.ศ. 2548" },
        { degree: "วศ.บ. (วิศวกรรมไฟฟ้าอิเล็กทรอนิกส์และคอมพิวเตอร์)", school: "มหาวิทยาลัยอุบลราชธานี", year: "พ.ศ. 2543" }
      ],
      courses: [
        { code: "4122706", name: "สถาปัตยกรรมคอมพิวเตอร์", credits: "3(2-2-5)" },
        { code: "4123652", name: "การออกแบบและพัฒนาเกมคอมพิวเตอร์", credits: "3(2-2-5)" },
        { code: "4124511", name: "การประมวลผลภาพ", credits: "3(2-2-5)" }
      ],
      research: [
        {
          title: "การพัฒนาแอปพลิเคชันการเขียนโปรแกรมด้วยบล็อกภาพผ่านมือถือเพื่อการควบคุมหุ่นยนต์เดินตามเส้นขนาดเล็ก",
          author: "เจษฎา โพนแก้ว",
          year: "พ.ศ. 2566",
          journal: "วารสารวิชาการการจัดการเทคโนโลยี มหาวิทยาลัยราชภัฏมหาสารคาม ปีที่ 10 ฉบับที่ 1 หน้า 32-39"
        }
      ]
    },
    "2": {
      name: "ดร.เจษฎา ชาตรี",
      nameEn: "Dr. Jessada Chatree",
      role: "อาจารย์ผู้รับผิดชอบหลักสูตร",
      expertise: "Computer Science and Engineering",
      email: "jessada.c@sskru.ac.th",
      office: "ห้องพักอาจารย์สาขาวิทยาการคอมพิวเตอร์ ชั้น 5 อาคาร LASC",
      image: "/static/images/jessada_c.jpg",
      education: [
        { degree: "Ph.D. (Computer Science and Engineering)", school: "University of North Texas, USA", year: "พ.ศ. 2557 (2014)" },
        { degree: "วท.ม. (การศึกษาวิทยาศาสตร์ - คอมพิวเตอร์)", school: "สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง", year: "พ.ศ. 2547" },
        { degree: "ค.บ. (คอมพิวเตอร์ศึกษา)", school: "มหาวิทยาลัยราชภัฏสุรินทร์", year: "พ.ศ. 2538" }
      ],
      courses: [
        { code: "4113501", name: "การวิจัยดำเนินงาน", credits: "3(3-0-6)" },
        { code: "4124507", name: "การทำเหมืองข้อมูล", credits: "3(2-2-5)" },
        { code: "4122401", name: "ระบบปฏิบัติการ", credits: "3(2-2-5)" }
      ],
      research: [
        {
          title: "การพัฒนาแอปพลิเคชัน น้องลำดวน ไลน์แชทบอท เพื่อแนะนำสถานที่ท่องเที่ยวในจังหวัดศรีสะเกษ",
          author: "เจษฎา ชาตรี",
          year: "พ.ศ. 2566",
          journal: "วารสารวิทยาการสารสนเทศและการสื่อสาร"
        }
      ]
    },
    "3": {
      name: "ดร.กริชบดินทร์ ผิวหอม",
      nameEn: "Dr. Krichbodin Phewhom",
      role: "อาจารย์ผู้รับผิดชอบหลักสูตร",
      expertise: "วิศวกรรมคอมพิวเตอร์",
      email: "krichbodin.p@sskru.ac.th",
      office: "ห้องพักอาจารย์สาขาวิทยาการคอมพิวเตอร์ ชั้น 5 อาคาร LASC",
      image: "/static/images/krichbodin.jpg",
      education: [
        { degree: "ปร.ด. (วิศวกรรมคอมพิวเตอร์)", school: "มหาวิทยาลัยขอนแก่น", year: "พ.ศ. 2564" },
        { degree: "วท.ม. (วิทยาการคอมพิวเตอร์)", school: "มหาวิทยาลัยขอนแก่น", year: "พ.ศ. 2555" },
        { degree: "วท.บ. (วิทยาการคอมพิวเตอร์)", school: "มหาวิทยาลัยรามคำแหง", year: "พ.ศ. 2544" }
      ],
      courses: [
        { code: "4121206", name: "การเขียนโปรแกรมคอมพิวเตอร์", credits: "3(2-2-5)" },
        { code: "4121701", name: "ดิจิตอลเบื้องต้น", credits: "3(2-2-5)" },
        { code: "4124509", name: "การสื่อสารระหว่างมนุษย์กับคอมพิวเตอร์", credits: "3(2-2-5)" },
        { code: "4124501", name: "ปัญญาประดิษฐ์", credits: "3(2-2-5)" }
      ],
      research: [
        {
          title: "การเปรียบเทียบประสิทธิภาพอัลกอริทึม Apriori และ FP-Growth ด้วยชุดข้อมูลร้านขายของชำ",
          author: "กริชบดินทร์ ผิวหอม",
          year: "พ.ศ. 2565",
          journal: "วารสารวิชาการคอมพิวเตอร์และเทคโนโลยี"
        }
      ]
    },
    "4": {
      name: "ผู้ช่วยศาสตราจารย์ พิศาล สุขขี",
      nameEn: "Asst. Prof. Phisan Sukkee",
      role: "อาจารย์ผู้รับผิดชอบหลักสูตร",
      expertise: "วิทยาการคอมพิวเตอร์",
      email: "phisan.s@sskru.ac.th",
      office: "ห้องพักอาจารย์สาขาวิทยาการคอมพิวเตอร์ ชั้น 5 อาคาร LASC",
      image: "/static/images/phisan.jpg",
      education: [
        { degree: "วท.ม. (วิทยาการคอมพิวเตอร์)", school: "มหาวิทยาลัยศิลปากร", year: "พ.ศ. 2554" },
        { degree: "วท.บ. (วิทยาการคอมพิวเตอร์)", school: "มหาวิทยาลัยศิลปากร", year: "พ.ศ. 2548" }
      ],
      courses: [
        { code: "4121203", name: "การเขียนโปรแกรมเชิงวัตถุ", credits: "3(2-2-5)" },
        { code: "4122104", name: "การออกแบบและพัฒนาเว็บ", credits: "3(2-2-5)" },
        { code: "4123505", name: "การเขียนโปรแกรมคอมพิวเตอร์ขั้นสูง", credits: "3(2-2-5)" },
        { code: "4122204", name: "โครงสร้างข้อมูลและอัลกอริทึม", credits: "3(2-2-5)" },
        { code: "4124614", name: "การพัฒนาแอปพลิเคชันบนมือถือ", credits: "3(2-2-5)" }
      ],
      research: [
        {
          title: "การพัฒนาแอปพลิเคชัน น้องลำดวน ไลน์แชทบอท เพื่อแนะนำสถานที่ท่องเที่ยวในจังหวัดศรีสะเกษ",
          author: "พิศาล สุขขี",
          year: "พ.ศ. 2566",
          journal: "วารสารวิทยาศาสตร์และเทคโนโลยีการประยุกต์"
        }
      ]
    }
  };

  const modalBackdrop = document.getElementById('futuristicModalBackdrop');
  const modalPayload = document.getElementById('modalDossierPayload');

  const openDossier = (id) => {
    const data = facultyData[id];
    if (!data || !modalBackdrop || !modalPayload) return;

    modalPayload.innerHTML = `
      <!-- TOP NAVY HEADER BANNER -->
      <div class="dossier-top-banner">
        <div class="d-flex align-items-center gap-3">
          <div class="dossier-avatar-disc">
            <img src="${data.image}" alt="${data.name}">
          </div>
          <div>
            <h3 class="dossier-header-title">${data.name}</h3>
            <div class="dossier-header-subtitle">${data.nameEn}</div>
            <div class="d-flex flex-wrap gap-2 align-items-center">
              <span class="dossier-role-pill-dark">${data.role}</span>
              <span class="dossier-role-pill-cyan">${data.expertise}</span>
            </div>
          </div>
        </div>
        <button type="button" class="dossier-close-cross" onclick="document.getElementById('futuristicModalBackdrop').classList.remove('active'); document.body.style.overflow='';" aria-label="ปิด">
          <i class="bi bi-x-lg"></i>
        </button>
      </div>

      <!-- MAIN 2-COLUMN SCROLLABLE BODY -->
      <div class="dossier-body-scrollable">
        <div class="row g-4">
          <!-- LEFT COLUMN: EDUCATION (40%) -->
          <div class="col-12 col-lg-5">
            <div class="dossier-column-heading">
              <span class="dossier-heading-icon" style="background: #e0f2fe; color: #0284c7;">
                <i class="bi bi-mortarboard-fill"></i>
              </span>
              <span>ประวัติการศึกษา</span>
            </div>
            <div class="academic-timeline-tree">
              ${data.education.map(edu => `
                <div class="timeline-step-node">
                  <div class="timeline-step-circle"></div>
                  <div class="timeline-degree-name">${edu.degree}</div>
                  <div class="timeline-school-name">${edu.school}</div>
                  <span class="timeline-year-chip">${edu.year}</span>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- RIGHT COLUMN: COURSES & RESEARCH (60%) -->
          <div class="col-12 col-lg-7">
            <!-- Courses Section -->
            <div class="mb-4">
              <div class="dossier-column-heading">
                <span class="dossier-heading-icon" style="background: #dcfce7; color: #16a34a;">
                  <i class="bi bi-book-half"></i>
                </span>
                <span>รายวิชาที่สอนหลัก</span>
              </div>
              <div class="course-card-grid">
                ${data.courses.map(c => `
                  <div class="course-golden-card">
                    <div class="course-golden-code">${c.code}</div>
                    <div class="course-golden-title">${c.name}</div>
                    <div class="course-golden-credits">หน่วยกิต: ${c.credits}</div>
                  </div>
                `).join('')}
              </div>
            </div>

            <!-- Research Publications Section -->
            <div>
              <div class="dossier-column-heading">
                <span class="dossier-heading-icon" style="background: #fef3c7; color: #d97706;">
                  <i class="bi bi-journal-bookmark-fill"></i>
                </span>
                <span>ผลงานตีพิมพ์ทางวิชาการ</span>
              </div>
              <div>
                ${data.research.map(res => `
                  <div class="research-quote-card">
                    <div class="research-quote-title">
                      <span style="color: #0284c7; margin-right: 4px;">❝</span> ${res.title}
                    </div>
                    <div class="research-author-year">
                      ผู้เขียน: ${res.author} | ปีที่พิมพ์: ${res.year}
                    </div>
                    <span class="research-journal-badge">
                      ${res.journal}
                    </span>
                  </div>
                `).join('')}
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- BOTTOM ACTION BAR -->
      <div class="dossier-footer-strip">
        <button type="button" class="btn-dossier-dismiss" onclick="document.getElementById('futuristicModalBackdrop').classList.remove('active'); document.body.style.overflow='';">
          ปิดหน้าต่างประวัติ
        </button>
      </div>
    `;

    modalBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  const closeDossier = () => {
    if (!modalBackdrop) return;
    modalBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  };

  document.querySelectorAll('[data-faculty-id]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = btn.getAttribute('data-faculty-id');
      if (id) {
        e.preventDefault();
        openDossier(id);
      }
    });
  });

  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) closeDossier();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalBackdrop && modalBackdrop.classList.contains('active')) {
      closeDossier();
    }
  });

  // 8. Mobile FAB Speed Dial Toggle
  const mobileFabContainer = document.getElementById('mobileFabContainer');
  const mobileFabTrigger = document.getElementById('mobileFabTrigger');

  if (mobileFabTrigger && mobileFabContainer) {
    mobileFabTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      mobileFabContainer.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (!mobileFabContainer.contains(e.target)) {
        mobileFabContainer.classList.remove('open');
      }
    });
  }

  // 9. PWA Service Worker Registration & Install Banner
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/static/sw.js').catch(() => {});
    });
  }

  let deferredPrompt = null;
  const pwaInstallBanner = document.getElementById('pwaInstallBanner');
  const btnPwaInstall = document.getElementById('btnPwaInstall');
  const btnPwaDismiss = document.getElementById('btnPwaDismiss');

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    if (pwaInstallBanner && !sessionStorage.getItem('pwa_dismissed')) {
      pwaInstallBanner.style.display = 'flex';
    }
  });

  if (btnPwaInstall) {
    btnPwaInstall.addEventListener('click', async () => {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        deferredPrompt = null;
      }
      if (pwaInstallBanner) pwaInstallBanner.style.display = 'none';
    });
  }

  if (btnPwaDismiss) {
    btnPwaDismiss.addEventListener('click', () => {
      if (pwaInstallBanner) pwaInstallBanner.style.display = 'none';
      sessionStorage.setItem('pwa_dismissed', 'true');
    });
  }
});
