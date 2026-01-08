/**
 * Stable Animations - Optimized for Performance
 * Clean, smooth, and reliable
 */

(function() {
  'use strict';
  
  // Check environment
  const hasGSAP = typeof gsap !== 'undefined';
  const hasScrollTrigger = typeof ScrollTrigger !== 'undefined';
  const isDesktop = window.innerWidth > 768;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  if (!hasGSAP || prefersReducedMotion) {
    console.log('Animations disabled');
    return;
  }
  
  // Register plugins
  if (hasScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
  }
  if (typeof ScrollToPlugin !== 'undefined') {
    gsap.registerPlugin(ScrollToPlugin);
  }
  
  // ============================================
  // SIMPLE PAGE ENTRANCE
  // ============================================
  
  function initPageEntrance() {
    // Ensure everything is visible first
    gsap.set('.card, .product-item, .cart-item, .btn', { opacity: 1 });
    
    // Simple fade in for cards
    const cards = document.querySelectorAll('.card');
    if (cards.length > 0) {
      gsap.from(cards, {
        opacity: 0,
        y: 20,
        duration: 0.6,
        stagger: 0.05,
        ease: 'power2.out',
        clearProps: 'all'
      });
    }
  }
  
  // ============================================
  // SIMPLE SCROLL ANIMATIONS
  // ============================================
  
  function initScrollAnimations() {
    if (!hasScrollTrigger) return;
    
    // Simple fade in on scroll
    const scrollElements = document.querySelectorAll('.card, .product-item');
    
    scrollElements.forEach(element => {
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: 'top 90%',
          toggleActions: 'play none none none',
          once: true
        },
        opacity: 0,
        y: 20,
        duration: 0.5,
        ease: 'power2.out',
        clearProps: 'all'
      });
    });
  }
  
  // ============================================
  // SIMPLE HOVER EFFECTS
  // ============================================
  
  function initHoverEffects() {
    // Card hover
    document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('mouseenter', function() {
        gsap.to(this, {
          y: -5,
          duration: 0.3,
          ease: 'power2.out'
        });
      });
      
      card.addEventListener('mouseleave', function() {
        gsap.to(this, {
          y: 0,
          duration: 0.3,
          ease: 'power2.out'
        });
      });
    });
    
    // Button hover
    document.querySelectorAll('.btn').forEach(btn => {
      btn.addEventListener('mouseenter', function() {
        gsap.to(this, {
          scale: 1.05,
          duration: 0.2,
          ease: 'power2.out'
        });
      });
      
      btn.addEventListener('mouseleave', function() {
        gsap.to(this, {
          scale: 1,
          duration: 0.2,
          ease: 'power2.out'
        });
      });
    });
  }
  
  // ============================================
  // SCROLL TO TOP
  // ============================================
  
  function initScrollToTop() {
    const scrollBtn = document.getElementById('scroll-to-top');
    if (!scrollBtn || !hasScrollTrigger) return;
    
    ScrollTrigger.create({
      start: 'top -300',
      end: 'max',
      onUpdate: (self) => {
        if (self.direction === -1 && self.progress > 0.1) {
          scrollBtn.style.opacity = '1';
          scrollBtn.style.pointerEvents = 'auto';
        } else if (self.direction === 1 || self.progress < 0.05) {
          scrollBtn.style.opacity = '0';
          scrollBtn.style.pointerEvents = 'none';
        }
      }
    });
    
    scrollBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
  
  // ============================================
  // PROGRESS BAR
  // ============================================
  
  function initProgressBar() {
    const progressBar = document.querySelector('.progress-bar');
    if (!progressBar) return;
    
    window.addEventListener('scroll', () => {
      const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrolled = (window.pageYOffset / windowHeight) * 100;
      progressBar.style.width = scrolled + '%';
    });
  }
  
  // ============================================
  // CART ANIMATIONS
  // ============================================
  
  function animateBadge(badge) {
    if (!badge) return;
    gsap.timeline()
      .to(badge, { scale: 1.3, duration: 0.2 })
      .to(badge, { scale: 1, duration: 0.3, ease: 'elastic.out(1, 0.5)' });
  }
  
  function animateCartAdd(button) {
    if (!button) return;
    gsap.timeline()
      .to(button, { scale: 0.95, duration: 0.1 })
      .to(button, { scale: 1.05, duration: 0.2, ease: 'back.out(1.5)' })
      .to(button, { scale: 1, duration: 0.2 });
  }
  
  function animateCartRemove(item) {
    if (!item) return;
    gsap.to(item, {
      x: 100,
      opacity: 0,
      duration: 0.4,
      ease: 'power2.in',
      onComplete: () => item.remove()
    });
  }
  
  // ============================================
  // SYNC NEW CONTENT
  // ============================================
  
  function syncNewContent(container) {
    if (!container) return;
    
    const newElements = container.querySelectorAll('.card, .product-item');
    gsap.set(newElements, { opacity: 1 });
    
    gsap.from(newElements, {
      opacity: 0,
      y: 20,
      duration: 0.5,
      stagger: 0.05,
      ease: 'power2.out',
      clearProps: 'all'
    });
    
    if (hasScrollTrigger) {
      ScrollTrigger.refresh();
    }
  }
  
  // ============================================
  // INITIALIZE
  // ============================================
  
  function init() {
    // Ensure all content is visible
    document.querySelectorAll('.card, .product-item, .cart-item, .btn').forEach(el => {
      el.style.opacity = '1';
      el.style.visibility = 'visible';
    });
    
    // Initialize animations with delay
    setTimeout(() => {
      initPageEntrance();
      initScrollAnimations();
      initHoverEffects();
      initScrollToTop();
      initProgressBar();
    }, 100);
  }
  
  // Start when page is fully loaded
  if (document.readyState === 'complete') {
    init();
  } else {
    window.addEventListener('load', init);
  }
  
  // Export functions
  window.stableAnimations = {
    badge: animateBadge,
    cartAdd: animateCartAdd,
    cartRemove: animateCartRemove,
    syncNewContent: syncNewContent,
    refresh: () => {
      if (hasScrollTrigger) {
        ScrollTrigger.refresh();
      }
    }
  };
  
})();
