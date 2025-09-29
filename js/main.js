// OSHUNJA Website - Main JavaScript
// Handles navigation, testimonials slider, form validation, and interactive features

// ============================================
// GLOBAL VARIABLES & INITIALIZATION
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all features
    initNavigation();
    initTestimonialSlider();
    initContactForm();
    initFAQ();
    initSmoothScroll();
    initDatePicker();
});

// ============================================
// STICKY HEADER & MOBILE NAVIGATION
// ============================================

function initNavigation() {
    const header = document.getElementById('header');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navLinks = document.getElementById('navLinks');

    // Sticky header on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Mobile menu toggle
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', function() {
            const isActive = navLinks.classList.contains('active');

            // Toggle mobile menu
            navLinks.classList.toggle('active');

            // Update ARIA attribute
            mobileMenuBtn.setAttribute('aria-expanded', !isActive);

            // Change icon
            mobileMenuBtn.textContent = isActive ? '☰' : '✕';
        });

        // Close menu when clicking on a link
        const navItems = navLinks.querySelectorAll('a');
        navItems.forEach(item => {
            item.addEventListener('click', function() {
                if (window.innerWidth <= 768) {
                    navLinks.classList.remove('active');
                    mobileMenuBtn.setAttribute('aria-expanded', 'false');
                    mobileMenuBtn.textContent = '☰';
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navLinks.contains(event.target);
            const isClickOnButton = mobileMenuBtn.contains(event.target);

            if (!isClickInsideNav && !isClickOnButton && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileMenuBtn.setAttribute('aria-expanded', 'false');
                mobileMenuBtn.textContent = '☰';
            }
        });
    }
}

// ============================================
// TESTIMONIAL SLIDER
// ============================================

function initTestimonialSlider() {
    const track = document.getElementById('testimonialTrack');
    const dotsContainer = document.getElementById('sliderDots');
    const prevBtn = document.querySelector('.slider-prev');
    const nextBtn = document.querySelector('.slider-next');

    // Exit if slider elements don't exist on this page
    if (!track || !dotsContainer) return;

    const testimonials = track.querySelectorAll('.testimonial');
    const totalSlides = testimonials.length;
    let currentSlide = 0;
    let autoPlayInterval;

    // Create navigation dots
    function createDots() {
        dotsContainer.innerHTML = '';
        for (let i = 0; i < totalSlides; i++) {
            const dot = document.createElement('button');
            dot.classList.add('dot');
            dot.setAttribute('aria-label', `Go to testimonial ${i + 1}`);
            if (i === 0) dot.classList.add('active');

            dot.addEventListener('click', () => goToSlide(i));
            dotsContainer.appendChild(dot);
        }
    }

    // Update slider position
    function updateSlider() {
        // Move track
        track.style.transform = `translateX(-${currentSlide * 100}%)`;

        // Update dots
        const dots = dotsContainer.querySelectorAll('.dot');
        dots.forEach((dot, index) => {
            if (index === currentSlide) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    // Go to specific slide
    function goToSlide(slideIndex) {
        currentSlide = slideIndex;
        updateSlider();
        resetAutoPlay();
    }

    // Next slide
    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateSlider();
    }

    // Previous slide
    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        updateSlider();
    }

    // Auto play
    function startAutoPlay() {
        autoPlayInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
    }

    // Reset auto play
    function resetAutoPlay() {
        clearInterval(autoPlayInterval);
        startAutoPlay();
    }

    // Stop auto play on hover
    track.addEventListener('mouseenter', () => {
        clearInterval(autoPlayInterval);
    });

    track.addEventListener('mouseleave', () => {
        startAutoPlay();
    });

    // Navigation button event listeners
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            prevSlide();
            resetAutoPlay();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            nextSlide();
            resetAutoPlay();
        });
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            prevSlide();
            resetAutoPlay();
        } else if (e.key === 'ArrowRight') {
            nextSlide();
            resetAutoPlay();
        }
    });

    // Touch/swipe support
    let touchStartX = 0;
    let touchEndX = 0;

    track.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    });

    track.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        const swipeThreshold = 50;
        if (touchStartX - touchEndX > swipeThreshold) {
            // Swipe left - next slide
            nextSlide();
            resetAutoPlay();
        } else if (touchEndX - touchStartX > swipeThreshold) {
            // Swipe right - previous slide
            prevSlide();
            resetAutoPlay();
        }
    }

    // Initialize
    createDots();
    startAutoPlay();
}

// ============================================
// CONTACT FORM VALIDATION & SUBMISSION
// ============================================

function initContactForm() {
    const form = document.getElementById('contactForm');

    // Exit if form doesn't exist on this page
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form values
        const formData = {
            name: document.getElementById('name').value.trim(),
            email: document.getElementById('email').value.trim(),
            phone: document.getElementById('phone').value.trim(),
            procedure: document.getElementById('procedure').value,
            appointmentDate: document.getElementById('appointmentDate').value,
            message: document.getElementById('message').value.trim(),
            consent: document.getElementById('consent').checked
        };

        // Validate form
        const validation = validateForm(formData);

        if (!validation.isValid) {
            showFormMessage(validation.message, 'error');
            return;
        }

        // Simulate form submission
        // In production, this would send data to your backend
        handleFormSubmission(formData);
    });
}

// Form validation
function validateForm(data) {
    // Name validation
    if (data.name.length < 2) {
        return {
            isValid: false,
            message: 'Please enter your full name (at least 2 characters).'
        };
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
        return {
            isValid: false,
            message: 'Please enter a valid email address.'
        };
    }

    // Phone validation (basic)
    const phoneRegex = /^[\d\s\-\+\(\)]+$/;
    if (!phoneRegex.test(data.phone) || data.phone.length < 10) {
        return {
            isValid: false,
            message: 'Please enter a valid phone number.'
        };
    }

    // Procedure selection
    if (!data.procedure) {
        return {
            isValid: false,
            message: 'Please select a procedure of interest.'
        };
    }

    // Consent checkbox
    if (!data.consent) {
        return {
            isValid: false,
            message: 'Please consent to being contacted by checking the consent box.'
        };
    }

    return { isValid: true };
}

// Handle form submission
function handleFormSubmission(formData) {
    // Show loading state
    const submitButton = document.querySelector('#contactForm button[type="submit"]');
    const originalButtonText = submitButton.textContent;
    submitButton.textContent = 'Submitting...';
    submitButton.disabled = true;

    // Simulate API call (replace with actual backend integration)
    setTimeout(() => {
        // Log form data to console (for demonstration)
        console.log('=== CONSULTATION REQUEST SUBMITTED ===');
        console.log('Name:', formData.name);
        console.log('Email:', formData.email);
        console.log('Phone:', formData.phone);
        console.log('Procedure:', formData.procedure);
        console.log('Preferred Date:', formData.appointmentDate || 'Not specified');
        console.log('Message:', formData.message || 'No additional message');
        console.log('Consent Given:', formData.consent);
        console.log('Timestamp:', new Date().toISOString());
        console.log('======================================');

        // TODO: Replace this with actual backend integration
        // Example: fetch('/api/consultations', { method: 'POST', body: JSON.stringify(formData) })

        // Show success message
        showFormMessage(
            'Thank you for your consultation request! Our team will contact you within 24 hours to schedule your appointment.',
            'success'
        );

        // Reset form
        document.getElementById('contactForm').reset();

        // Reset button
        submitButton.textContent = originalButtonText;
        submitButton.disabled = false;

        // Scroll to success message
        document.getElementById('formMessage').scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    }, 1500); // Simulate network delay
}

// Show form message (success or error)
function showFormMessage(message, type) {
    const messageElement = document.getElementById('formMessage');
    messageElement.textContent = message;
    messageElement.className = `form-message ${type} show`;

    // Hide message after 8 seconds
    setTimeout(() => {
        messageElement.classList.remove('show');
    }, 8000);
}

// ============================================
// FAQ ACCORDION
// ============================================

function initFAQ() {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const faqItem = this.parentElement;
            const answer = this.nextElementSibling;
            const isActive = this.classList.contains('active');

            // Close all other FAQs (optional - comment out for multiple open)
            faqQuestions.forEach(q => {
                if (q !== this) {
                    q.classList.remove('active');
                    q.setAttribute('aria-expanded', 'false');
                    q.nextElementSibling.style.maxHeight = null;
                }
            });

            // Toggle current FAQ
            if (isActive) {
                this.classList.remove('active');
                this.setAttribute('aria-expanded', 'false');
                answer.style.maxHeight = null;
            } else {
                this.classList.add('active');
                this.setAttribute('aria-expanded', 'true');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });
}

// ============================================
// SMOOTH SCROLL FOR ANCHOR LINKS
// ============================================

function initSmoothScroll() {
    // Smooth scroll for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Skip if href is just "#"
            if (href === '#') return;

            const targetElement = document.querySelector(href);

            if (targetElement) {
                e.preventDefault();

                // Calculate offset for fixed header
                const headerHeight = document.getElementById('header').offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ============================================
// DATE PICKER MINIMUM DATE
// ============================================

function initDatePicker() {
    const dateInput = document.getElementById('appointmentDate');

    if (dateInput) {
        // Set minimum date to tomorrow
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);

        const year = tomorrow.getFullYear();
        const month = String(tomorrow.getMonth() + 1).padStart(2, '0');
        const day = String(tomorrow.getDate()).padStart(2, '0');

        dateInput.setAttribute('min', `${year}-${month}-${day}`);
    }
}

// ============================================
// SERVICE CARD CLICK HANDLERS
// ============================================

// Add keyboard accessibility for service cards with onclick
document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
        if (e.target.classList.contains('service-card') && e.target.hasAttribute('onclick')) {
            e.preventDefault();
            e.target.click();
        }
    }
});

// ============================================
// UTILITY FUNCTIONS
// ============================================

// Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Check if element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// ============================================
// CONSOLE MESSAGE
// ============================================

console.log('%cOSHUNJA Website', 'font-size: 20px; font-weight: bold; color: #C49A6C;');
console.log('%cWhere Medicine Meets Aesthetics', 'font-size: 14px; color: #8B7355;');
console.log('%cKingston, Jamaica', 'font-size: 12px; color: #666;');
console.log('%c© 2025 OSHUNJA. All rights reserved.', 'font-size: 10px; color: #999;');