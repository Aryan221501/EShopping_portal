/**
 * Premium Anime.js Animations - Optimized & Responsive
 * Best animations with performance optimization
 */

(function() {
  'use strict';
  
  // Performance check
  const isDesktop = window.innerWidth > 768;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const shouldAnimate = isDesktop && !prefersReducedMotion && typeof anime !== 'undefined';
  
  if (!shouldAnimate) return;
  
  // ============================================
  // 1. PAGE ENTRANCE ANIMATIONS
  // ============================================
  
  function initPageEntrance() {
    // Hero section fade in
    anime({
      targets: 'h1, h2',
      opacity: [0, 1],
      translateY: [-30, 0],
      duration: 800,
      easing: 'easeOutExpo',
      delay: anime.stagger(100)
    });
    
    // Cards stagger entrance
    anime({
      targets: '.card',
      opacity: [0, 1],
      translateY: [40, 0],
      scale: [0.95, 1],
      duration: 600,
      easing: 'easeOutCubic',
      delay: anime.stagger(60, {start: 200})
    });
    
    // Navbar slide down
    anime({
      targets: '.navbar',
      translateY: [-100, 0],
      opacity: [0, 1],
      duration: 700,
      easing: 'easeOutExpo'
    });
    
    // Buttons pop in
    anime({
      targets: '.btn',
      scale: [0, 1],
      opacity: [0, 1],
      duration: 500,
      easing: 'easeOutElastic(1, .6)',
      delay: anime.stagger(50, {start: 400})
    });
  }
  
  // ============================================
  // 2. HOVER ANIMATIONS
  // ============================================
  
  function initHoverAnimations() {
    // Card hover with 3D tilt
    document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('mouseenter', function(e) {
        anime({
          targets: this,
          translateY: -8,
          scale: 1.02,
          duration: 300,
          easing: 'easeOutCubic'
        });
        
        // Glow effect
        anime({
          targets: this,
          boxShadow: [
            '0 0 0 rgba(88, 166, 255, 0)',
            '0 10px 40px rgba(88, 166, 255, 0.4)'
          ],
          duration: 300,
          easing: 'easeOutCubic'
        });
      });
      
      card.addEventListener('mouseleave', function() {
        anime({
          targets: this,
          translateY: 0,
          scale: 1,
          boxShadow: '0 0 0 rgba(88, 166, 255, 0)',
          duration: 300,
          easing: 'easeOutCubic'
        });
      });
      
    });
    
    // Button hover effects
    document.querySelectorAll('.btn').forEach(btn => {
      btn.addEventListener('mouseenter', function() {
        anime({
          targets: this,
          scale: 1.05,
          duration: 250,
          easing: 'easeOutCubic'
        });
      });
      
      btn.addEventListener('mouseleave', function() {
        anime({
          targets: this,
          scale: 1,
          duration: 250,
          easing: 'easeOutCubic'
        });
      });
      
      btn.addEventListener('mousedown', function() {
        anime({
          targets: this,
          scale: 0.95,
          duration: 100,
          easing: 'easeOutCubic'
        });
      });
      
      btn.addEventListener('mouseup', function() {
        anime({
          targets: this,
          scale: 1.05,
          duration: 150,
          easing: 'easeOutElastic(1, .5)'
        });
      });
    });
  }
  
  // ============================================
  // 3. SCROLL ANIMATIONS
  // ============================================
  
  function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          anime({
            targets: entry.target,
            opacity: [0, 1],
            translateY: [30, 0],
            duration: 600,
            easing: 'easeOutCubic'
          });
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.card, .product-item').forEach(el => {
      observer.observe(el);
    });
  }
  
  // ============================================
  // 4. CLICK RIPPLE EFFECT
  // ============================================
  
  function initRippleEffect() {
    document.addEventListener('click', function(e) {
      const ripple = document.createElement('div');
      ripple.className = 'click-ripple';
      ripple.style.left = e.clientX + 'px';
      ripple.style.top = e.clientY + 'px';
      document.body.appendChild(ripple);
      
      anime({
        targets: ripple,
        scale: [0, 3],
        opacity: [0.6, 0],
        duration: 600,
        easing: 'easeOutExpo',
        complete: () => ripple.remove()
      });
    });
  }
  
  // ============================================
  // 5. FLOATING BADGES
  // ============================================
  
  function initFloatingBadges() {
    anime({
      targets: '.badge, .category-badge',
      translateY: [
        { value: -5, duration: 1000 },
        { value: 0, duration: 1000 }
      ],
      loop: true,
      easing: 'easeInOutSine',
      delay: anime.stagger(200)
    });
  }
  
  // ============================================
  // 6. PRICE TAG PULSE
  // ============================================
  
  function initPricePulse() {
    anime({
      targets: '.price-tag',
      scale: [
        { value: 1.05, duration: 800 },
        { value: 1, duration: 800 }
      ],
      loop: true,
      easing: 'easeInOutQuad',
      delay: anime.stagger(300)
    });
  }
  
  // ============================================
  // 7. NAVBAR GRADIENT ANIMATION
  // ============================================
  
  function initNavbarAnimation() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    
    anime({
      targets: navbar,
      backgroundPosition: ['0% 50%', '100% 50%'],
      duration: 15000,
      loop: true,
      easing: 'linear'
    });
  }
  
  // ============================================
  // 8. SEARCH BAR FOCUS ANIMATION
  // ============================================
  
  function initSearchAnimation() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;
    
    searchInput.addEventListener('focus', function() {
      anime({
        targets: this,
        scale: 1.02,
        boxShadow: '0 0 20px rgba(88, 166, 255, 0.3)',
        duration: 300,
        easing: 'easeOutCubic'
      });
    });
    
    searchInput.addEventListener('blur', function() {
      anime({
        targets: this,
        scale: 1,
        boxShadow: '0 0 0 rgba(88, 166, 255, 0)',
        duration: 300,
        easing: 'easeOutCubic'
      });
    });
  }
  
  // ============================================
  // 9. CART BADGE BOUNCE
  // ============================================
  
  function animateCartBadge() {
    const badge = document.getElementById('cart-badge');
    if (!badge || badge.style.display === 'none') return;
    
    anime({
      targets: badge,
      scale: [1, 1.2, 1],
      duration: 500,
      easing: 'easeOutElastic(1, .5)'
    });
  }
  
  // ============================================
  // 10. LOADING SPINNER
  // ============================================
  
  function initLoadingAnimation() {
    const spinner = document.querySelector('.loading-spinner');
    if (!spinner) return;
    
    anime({
      targets: spinner,
      rotate: 360,
      duration: 1000,
      loop: true,
      easing: 'linear'
    });
  }
  
  // ============================================
  // 11. FORM VALIDATION SHAKE
  // ============================================
  
  function shakeElement(element) {
    anime({
      targets: element,
      translateX: [
        { value: -10, duration: 100 },
        { value: 10, duration: 100 },
        { value: -10, duration: 100 },
        { value: 10, duration: 100 },
        { value: 0, duration: 100 }
      ],
      easing: 'easeInOutSine'
    });
  }
  
  // ============================================
  // 12. SUCCESS NOTIFICATION
  // ============================================
  
  function showSuccessAnimation(element) {
    anime({
      targets: element,
      scale: [0, 1],
      opacity: [0, 1],
      duration: 500,
      easing: 'easeOutElastic(1, .6)'
    });
    
    setTimeout(() => {
      anime({
        targets: element,
        opacity: [1, 0],
        translateY: [0, -20],
        duration: 400,
        easing: 'easeInCubic'
      });
    }, 3000);
  }
  
  // ============================================
  // 13. PARTICLE EFFECTS
  // ============================================
  
  function createParticles(x, y) {
    for (let i = 0; i < 8; i++) {
      const particle = document.createElement('div');
      particle.className = 'particle';
      particle.style.left = x + 'px';
      particle.style.top = y + 'px';
      document.body.appendChild(particle);
      
      const angle = (Math.PI * 2 * i) / 8;
      const velocity = 50;
      
      anime({
        targets: particle,
        translateX: Math.cos(angle) * velocity,
        translateY: Math.sin(angle) * velocity,
        opacity: [1, 0],
        scale: [1, 0],
        duration: 800,
        easing: 'easeOutCubic',
        complete: () => particle.remove()
      });
    }
  }
  
  // ============================================
  // 14. IMAGE LAZY LOAD ANIMATION
  // ============================================
  
  function initImageAnimations() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
      img.addEventListener('load', function() {
        anime({
          targets: this,
          opacity: [0, 1],
          scale: [0.9, 1],
          duration: 500,
          easing: 'easeOutCubic'
        });
      });
    });
  }
  
  // ============================================
  // INITIALIZE ALL ANIMATIONS
  // ============================================
  
  function init() {
    initPageEntrance();
    initHoverAnimations();
    initScrollAnimations();
    initRippleEffect();
    initFloatingBadges();
    initPricePulse();
    initNavbarAnimation();
    initSearchAnimation();
    initLoadingAnimation();
    initImageAnimations();
  }
  
  // Start animations when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  
  // Export functions for external use
  window.animeEffects = {
    shake: shakeElement,
    success: showSuccessAnimation,
    particles: createParticles,
    cartBadge: animateCartBadge
  };
  
})();
