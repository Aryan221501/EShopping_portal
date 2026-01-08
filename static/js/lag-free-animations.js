/**
 * LAG-FREE ANIMATIONS - Zero Lag, Maximum Performance
 * Optimized for 60fps on all devices
 */

(function() {
  'use strict';
  
  // Performance settings
  const isLowEnd = navigator.hardwareConcurrency < 4 || window.innerWidth < 768;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  if (prefersReducedMotion) {
    console.log('Animations disabled - user preference');
    return;
  }
  
  // ============================================
  // ESSENTIAL FUNCTIONS ONLY
  // ============================================
  
  // Simple progress bar (CSS only)
  function initProgressBar() {
    const progressBar = document.querySelector('.progress-bar');
    if (!progressBar) return;
    
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
  
  // Scroll to top button
  function initScrollButton() {
    const scrollBtn = document.getElementById('scroll-to-top');
    if (!scrollBtn) return;
    
    let ticking = false;
    
    function updateButton() {
      const show = window.pageYOffset > 300;
      scrollBtn.style.opacity = show ? '1' : '0';
      scrollBtn.style.pointerEvents = show ? 'auto' : 'none';
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
  
  // Simple card hover (desktop only)
  function initCardHovers() {
    if (isLowEnd) return;
    
    document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-3px)';
        this.style.boxShadow = '0 8px 16px rgba(0,0,0,0.4)';
        this.style.borderColor = 'var(--accent-color)';
      });
      
      card.addEventListener('mouseleave', function() {
        this.style.transform = '';
        this.style.boxShadow = '';
        this.style.borderColor = '';
      });
    });
  }
  
  // Cart badge animation
  function animateCartBadge(badge) {
    if (!badge || isLowEnd) return;
    
    badge.style.transform = 'scale(1.2)';
    setTimeout(() => {
      badge.style.transform = '';
    }, 150);
  }
  
  // ============================================
  // INITIALIZE
  // ============================================
  
  function init() {
    // Ensure all elements are visible
    document.querySelectorAll('.card, .btn').forEach(el => {
      el.style.opacity = '1';
      el.style.visibility = 'visible';
    });
    
    // Initialize only essential features
    initProgressBar();
    initScrollButton();
    
    // Only add hover effects on desktop
    if (!isLowEnd) {
      setTimeout(initCardHovers, 100);
    }
  }
  
  // Start immediately
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  
  // Export minimal API
  window.lagFreeAnimations = {
    cartBadge: animateCartBadge
  };
  
})();