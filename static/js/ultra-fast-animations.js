/**
 * Ultra-Fast Animations - Maximum Performance
 * Minimal, optimized animations for 60fps performance
 */

(function() {
  'use strict';
  
  // Performance checks
  const isDesktop = window.innerWidth > 768;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasGSAP = typeof gsap !== 'undefined';
  
  if (prefersReducedMotion) {
    console.log('Animations disabled - reduced motion preference');
    return;
  }
  
  // ============================================
  // MINIMAL PAGE ENTRANCE
  // ============================================
  
  function initMinimalEntrance() {
    if (!hasGSAP) return;
    
    // Only animate cards - nothing else
    const cards = document.querySelectorAll('.card');
    if (cards.length > 0) {
      gsap.from(cards, {
        opacity: 0,
        duration: 0.4,
        stagger: 0.02,
        ease: 'power1.out',
        clearProps: 'all'
      });
    }
  }
  
  // ============================================
  // ESSENTIAL HOVER EFFECTS ONLY
  // ============================================
  
  function initEssentialHovers() {
    // Only card hover - remove all others
    document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('mouseenter', function() {
        if (hasGSAP) {
          gsap.to(this, {
            y: -3,
            duration: 0.2,
            ease: 'power1.out'
          });
        }
      });
      
      card.addEventListener('mouseleave', function() {
        if (hasGSAP) {
          gsap.to(this, {
            y: 0,
            duration: 0.2,
            ease: 'power1.out'
          });
        }
      });
    });
  }
  
  // ============================================
  // CART BADGE ONLY
  // ============================================
  
  function animateBadge(badge) {
    if (!badge || !hasGSAP) return;
    gsap.to(badge, {
      scale: 1.2,
      duration: 0.15,
      yoyo: true,
      repeat: 1,
      ease: 'power1.inOut'
    });
  }
  
  // ============================================
  // PROGRESS BAR (CSS ONLY)
  // ============================================
  
  function initProgressBar() {
    const progressBar = document.querySelector('.progress-bar');
    if (!progressBar) return;
    
    // Use requestAnimationFrame for smooth scrolling
    let ticking = false;
    
    function updateProgress() {
      const scrolled = (window.pageYOffset / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
      progressBar.style.width = Math.min(scrolled, 100) + '%';
      ticking = false;
    }
    
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(updateProgress);
        ticking = true;
      }
    }, { passive: true });
  }
  
  // ============================================
  // SCROLL TO TOP (SIMPLE)
  // ============================================
  
  function initScrollToTop() {
    const scrollBtn = document.getElementById('scroll-to-top');
    if (!scrollBtn) return;
    
    let ticking = false;
    
    function updateButton() {
      if (window.pageYOffset > 300) {
        scrollBtn.style.opacity = '1';
        scrollBtn.style.pointerEvents = 'auto';
      } else {
        scrollBtn.style.opacity = '0';
        scrollBtn.style.pointerEvents = 'none';
      }
      ticking = false;
    }
    
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(updateButton);
        ticking = true;
      }
    }, { passive: true });
    
    scrollBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
  
  // ============================================
  // INITIALIZE (MINIMAL)
  // ============================================
  
  function init() {
    // Ensure visibility first
    document.querySelectorAll('.card, .btn').forEach(el => {
      el.style.opacity = '1';
      el.style.visibility = 'visible';
    });
    
    // Only essential animations
    setTimeout(() => {
      if (isDesktop) {
        initMinimalEntrance();
        initEssentialHovers();
      }
      initProgressBar();
      initScrollToTop();
    }, 50);
  }
  
  // Start when ready
  if (document.readyState === 'complete') {
    init();
  } else {
    window.addEventListener('load', init);
  }
  
  // Export minimal functions
  window.fastAnimations = {
    badge: animateBadge
  };
  
})();