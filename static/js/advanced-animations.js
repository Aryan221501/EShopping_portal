/**
 * Advanced Animations with Three.js & GSAP
 * Immersive 3D visuals and coordinated motion
 */

(function() {
  'use strict';
  
  // Check if libraries are loaded
  const hasThree = typeof THREE !== 'undefined';
  const hasGSAP = typeof gsap !== 'undefined';
  const isDesktop = window.innerWidth > 768;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  if (!hasGSAP || prefersReducedMotion) return;
  
  // Register GSAP plugins
  if (typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
  }
  if (typeof ScrollToPlugin !== 'undefined') {
    gsap.registerPlugin(ScrollToPlugin);
  }
  
  // ============================================
  // THREE.JS BACKGROUND SCENE
  // ============================================
  
  let scene, camera, renderer, particles;
  
  function initThreeBackground() {
    if (!hasThree || !isDesktop) return;
    
    // Create canvas container
    const canvas = document.createElement('canvas');
    canvas.id = 'three-background';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.zIndex = '-1';
    canvas.style.pointerEvents = 'none';
    document.body.prepend(canvas);
    
    // Setup Three.js scene
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 50;
    
    renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    
    // Create particle system
    const particleCount = 1000;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);
    
    for (let i = 0; i < particleCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 100;
      positions[i + 1] = (Math.random() - 0.5) * 100;
      positions[i + 2] = (Math.random() - 0.5) * 100;
      
      // Blue-ish colors
      colors[i] = 0.3 + Math.random() * 0.3;
      colors[i + 1] = 0.5 + Math.random() * 0.3;
      colors[i + 2] = 0.8 + Math.random() * 0.2;
    }
    
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    
    const material = new THREE.PointsMaterial({
      size: 0.5,
      vertexColors: true,
      transparent: true,
      opacity: 0.6,
      blending: THREE.AdditiveBlending
    });
    
    particles = new THREE.Points(geometry, material);
    scene.add(particles);
    
    // Animation loop
    function animate() {
      requestAnimationFrame(animate);
      
      particles.rotation.x += 0.0001;
      particles.rotation.y += 0.0002;
      
      renderer.render(scene, camera);
    }
    
    animate();
    
    // Handle resize
    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });
  }
  
  // ============================================
  // GSAP PAGE ENTRANCE ANIMATIONS
  // ============================================
  
  function initPageEntrance() {
    if (!hasGSAP) return;
    
    // Create a master timeline for synchronized animations
    const masterTimeline = gsap.timeline({
      defaults: { ease: 'power2.out' }
    });
    
    // 1. Navbar slides in first
    masterTimeline.from('.navbar', {
      y: -100,
      opacity: 0,
      duration: 0.6
    }, 0);
    
    // 2. Hero text follows
    masterTimeline.from('h1, h2', {
      x: -30,
      opacity: 0,
      duration: 0.8,
      stagger: 0.15
    }, 0.2);
    
    // 3. Cards animate in - only if they exist and are visible
    const cards = document.querySelectorAll('.card');
    if (cards.length > 0) {
      // Ensure cards are in the DOM and visible
      const visibleCards = Array.from(cards).filter(card => {
        return card.offsetParent !== null; // Check if visible
      });
      
      if (visibleCards.length > 0) {
        masterTimeline.from(visibleCards, {
          y: 40,
          opacity: 0,
          scale: 0.95,
          duration: 0.6,
          stagger: 0.08,
          ease: 'back.out(1.2)'
        }, 0.4);
      }
    }
    
    // 4. Buttons pop in last
    masterTimeline.from('.btn', {
      scale: 0,
      opacity: 0,
      duration: 0.4,
      stagger: 0.03,
      ease: 'back.out(1.5)'
    }, 0.6);
  }
  
  // ============================================
  // GSAP SCROLL ANIMATIONS
  // ============================================
  
  function initScrollAnimations() {
    if (typeof ScrollTrigger === 'undefined') return;
    
    // Refresh ScrollTrigger to ensure proper calculations
    ScrollTrigger.refresh();
    
    // ============================================
    // 1. FADE IN ON SCROLL - Cards & Products
    // ============================================
    const scrollElements = document.querySelectorAll('.card, .product-item, .cart-item');
    const visibleElements = Array.from(scrollElements).filter(el => {
      return el.offsetParent !== null && el.offsetHeight > 0;
    });
    
    visibleElements.forEach((element, index) => {
      // Skip if already animated by page entrance
      if (element.classList.contains('gsap-animated')) return;
      
      gsap.from(element, {
        scrollTrigger: {
          trigger: element,
          start: 'top 85%',
          end: 'top 20%',
          toggleActions: 'play none none reverse',
          once: false,
          // markers: true, // Uncomment for debugging
        },
        y: 50,
        opacity: 0,
        scale: 0.95,
        duration: 0.8,
        ease: 'power2.out',
        onComplete: () => {
          element.classList.add('gsap-animated');
        }
      });
    });
    
    // ============================================
    // 2. PARALLAX SCROLLING - Containers
    // ============================================
    gsap.utils.toArray('.container').forEach(container => {
      gsap.to(container, {
        scrollTrigger: {
          trigger: container,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1.5,
        },
        y: -20,
        ease: 'none'
      });
    });
    
    // ============================================
    // 3. REVEAL ANIMATION - Headings
    // ============================================
    gsap.utils.toArray('h1, h2, h3').forEach(heading => {
      gsap.from(heading, {
        scrollTrigger: {
          trigger: heading,
          start: 'top 90%',
          toggleActions: 'play none none reverse',
        },
        x: -50,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out'
      });
    });
    
    // ============================================
    // 4. SCALE UP ON SCROLL - Buttons
    // ============================================
    gsap.utils.toArray('.btn').forEach(btn => {
      gsap.from(btn, {
        scrollTrigger: {
          trigger: btn,
          start: 'top 95%',
          toggleActions: 'play none none reverse',
        },
        scale: 0,
        opacity: 0,
        duration: 0.5,
        ease: 'back.out(1.7)'
      });
    });
    
    // ============================================
    // 5. STAGGER ANIMATION - Badges
    // ============================================
    const badgeGroups = document.querySelectorAll('.category-badge, .badge');
    if (badgeGroups.length > 0) {
      gsap.from(badgeGroups, {
        scrollTrigger: {
          trigger: badgeGroups[0],
          start: 'top 90%',
          toggleActions: 'play none none reverse',
        },
        y: -20,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power2.out'
      });
    }
    
    // ============================================
    // 6. PRICE TAG REVEAL
    // ============================================
    gsap.utils.toArray('.price-tag').forEach(price => {
      gsap.from(price, {
        scrollTrigger: {
          trigger: price,
          start: 'top 90%',
          toggleActions: 'play none none reverse',
        },
        scale: 0,
        opacity: 0,
        duration: 0.6,
        ease: 'elastic.out(1, 0.5)'
      });
    });
    
    // ============================================
    // 7. HORIZONTAL SCROLL - Search Results
    // ============================================
    const searchResults = document.querySelector('#search-results');
    if (searchResults) {
      gsap.from(searchResults.children, {
        scrollTrigger: {
          trigger: searchResults,
          start: 'top 90%',
          toggleActions: 'play none none reverse',
        },
        x: -30,
        opacity: 0,
        duration: 0.5,
        stagger: 0.1,
        ease: 'power2.out'
      });
    }
    
    // ============================================
    // 8. ROTATE IN - Icons
    // ============================================
    gsap.utils.toArray('.bi').forEach(icon => {
      gsap.from(icon, {
        scrollTrigger: {
          trigger: icon,
          start: 'top 95%',
          toggleActions: 'play none none reverse',
        },
        rotation: -180,
        opacity: 0,
        duration: 0.6,
        ease: 'back.out(1.5)'
      });
    });
    
    // ============================================
    // 9. PIN ANIMATION - Navbar (optional)
    // ============================================
    const navbar = document.querySelector('.navbar');
    if (navbar) {
      ScrollTrigger.create({
        trigger: 'body',
        start: 'top -100',
        end: 'bottom bottom',
        onEnter: () => {
          gsap.to(navbar, {
            backgroundColor: 'rgba(22, 27, 34, 0.95)',
            backdropFilter: 'blur(10px)',
            duration: 0.3
          });
        },
        onLeaveBack: () => {
          gsap.to(navbar, {
            backgroundColor: 'var(--bg-secondary)',
            backdropFilter: 'none',
            duration: 0.3
          });
        }
      });
    }
    
    // ============================================
    // 10. PROGRESS INDICATOR (optional)
    // ============================================
    gsap.to('.progress-bar', {
      scrollTrigger: {
        trigger: 'body',
        start: 'top top',
        end: 'bottom bottom',
        scrub: 0.5,
      },
      width: '100%',
      ease: 'none'
    });
  }
  
  // ============================================
  // GSAP HOVER ANIMATIONS
  // ============================================
  
  function initHoverAnimations() {
    // Card hover
    document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('mouseenter', function() {
        gsap.to(this, {
          y: -10,
          scale: 1.02,
          boxShadow: '0 15px 40px rgba(88, 166, 255, 0.3)',
          duration: 0.3,
          ease: 'power2.out'
        });
      });
      
      card.addEventListener('mouseleave', function() {
        gsap.to(this, {
          y: 0,
          scale: 1,
          boxShadow: '0 0 0 rgba(88, 166, 255, 0)',
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
          duration: 0.3,
          ease: 'power2.out'
        });
      });
      
      btn.addEventListener('mouseleave', function() {
        gsap.to(this, {
          scale: 1,
          duration: 0.3,
          ease: 'power2.out'
        });
      });
      
      btn.addEventListener('click', function() {
        gsap.timeline()
          .to(this, { scale: 0.95, duration: 0.1 })
          .to(this, { scale: 1.05, duration: 0.2, ease: 'elastic.out(1, 0.3)' });
      });
    });
  }
  
  // ============================================
  // GSAP TIMELINE SEQUENCES
  // ============================================
  
  function createSuccessTimeline(element) {
    const tl = gsap.timeline();
    
    tl.to(element, {
      scale: 1.2,
      duration: 0.2,
      ease: 'power2.out'
    })
    .to(element, {
      scale: 1,
      duration: 0.4,
      ease: 'elastic.out(1, 0.5)'
    })
    .to(element, {
      backgroundColor: '#3fb950',
      duration: 0.3
    }, '-=0.3')
    .to(element, {
      backgroundColor: 'var(--accent-color)',
      duration: 0.3,
      delay: 1
    });
    
    return tl;
  }
  
  function createErrorTimeline(element) {
    const tl = gsap.timeline();
    
    tl.to(element, {
      x: -10,
      duration: 0.1
    })
    .to(element, {
      x: 10,
      duration: 0.1
    })
    .to(element, {
      x: -10,
      duration: 0.1
    })
    .to(element, {
      x: 0,
      duration: 0.1
    });
    
    return tl;
  }
  
  // ============================================
  // GSAP BADGE ANIMATIONS
  // ============================================
  
  function animateBadge(badge) {
    gsap.timeline()
      .to(badge, {
        scale: 1.5,
        duration: 0.2,
        ease: 'power2.out'
      })
      .to(badge, {
        scale: 1,
        duration: 0.4,
        ease: 'elastic.out(1, 0.5)'
      });
  }
  
  // ============================================
  // GSAP FLOATING ANIMATIONS
  // ============================================
  
  function initFloatingElements() {
    gsap.to('.category-badge, .badge', {
      y: -5,
      duration: 1.5,
      repeat: -1,
      yoyo: true,
      ease: 'sine.inOut',
      stagger: 0.2
    });
    
    gsap.to('.price-tag', {
      scale: 1.05,
      duration: 1,
      repeat: -1,
      yoyo: true,
      ease: 'sine.inOut',
      stagger: 0.3
    });
  }
  
  // ============================================
  // GSAP LOADING ANIMATIONS
  // ============================================
  
  function showLoadingAnimation(container) {
    const loader = document.createElement('div');
    loader.className = 'gsap-loader';
    loader.innerHTML = '<div class="loader-dot"></div><div class="loader-dot"></div><div class="loader-dot"></div>';
    container.appendChild(loader);
    
    gsap.to('.loader-dot', {
      y: -20,
      duration: 0.6,
      repeat: -1,
      yoyo: true,
      ease: 'power1.inOut',
      stagger: 0.2
    });
    
    return loader;
  }
  
  // ============================================
  // GSAP CART ANIMATIONS
  // ============================================
  
  function animateCartAdd(button) {
    const tl = gsap.timeline();
    
    tl.to(button, {
      scale: 0.9,
      duration: 0.1
    })
    .to(button, {
      scale: 1.1,
      duration: 0.3,
      ease: 'elastic.out(1, 0.5)'
    })
    .to(button, {
      backgroundColor: '#3fb950',
      duration: 0.2
    }, '-=0.2');
    
    // Animate cart badge
    const badge = document.getElementById('cart-badge');
    if (badge) {
      gsap.timeline()
        .to(badge, {
          scale: 1.5,
          duration: 0.2
        })
        .to(badge, {
          scale: 1,
          duration: 0.4,
          ease: 'elastic.out(1, 0.5)'
        });
    }
  }
  
  function animateCartRemove(item) {
    gsap.to(item, {
      x: 100,
      opacity: 0,
      duration: 0.4,
      ease: 'power2.in',
      onComplete: () => item.remove()
    });
  }
  
  // ============================================
  // GSAP SEARCH ANIMATIONS
  // ============================================
  
  function animateSearchResults(results) {
    gsap.from(results.children, {
      x: -20,
      opacity: 0,
      duration: 0.4,
      stagger: 0.05,
      ease: 'power2.out'
    });
  }
  
  // ============================================
  // INITIALIZE ALL ANIMATIONS (SYNCHRONIZED)
  // ============================================
  
  function init() {
    // Wait for everything to be ready
    if (!hasGSAP) {
      console.log('GSAP not loaded, skipping animations');
      return;
    }
    
    // Ensure all content is visible first
    document.querySelectorAll('.card, .product-item, .cart-item').forEach(el => {
      el.style.opacity = '1';
      el.style.visibility = 'visible';
    });
    
    // Small delay to ensure DOM is fully painted
    setTimeout(() => {
      initThreeBackground();
      
      // Wait for Three.js to initialize before other animations
      setTimeout(() => {
        initPageEntrance();
        initScrollAnimations();
        initHoverAnimations();
        initFloatingElements();
        initScrollToTop();
      }, 100);
    }, 50);
  }
  
  // Wait for complete page load including images
  function startAnimations() {
    if (document.readyState === 'complete') {
      init();
    } else {
      window.addEventListener('load', init);
    }
  }
  
  // Start when DOM is ready but wait for full load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startAnimations);
  } else {
    startAnimations();
  }
  
  // ============================================
  // SCROLL TO TOP BUTTON
  // ============================================
  
  function initScrollToTop() {
    const scrollBtn = document.getElementById('scroll-to-top');
    if (!scrollBtn) return;
    
    // Show/hide button based on scroll position
    ScrollTrigger.create({
      start: 'top -200',
      end: 'max',
      onUpdate: (self) => {
        if (self.progress > 0.1) {
          scrollBtn.classList.add('visible');
        } else {
          scrollBtn.classList.remove('visible');
        }
      }
    });
    
    // Smooth scroll to top on click
    scrollBtn.addEventListener('click', () => {
      gsap.to(window, {
        scrollTo: { y: 0, autoKill: false },
        duration: 1,
        ease: 'power2.inOut'
      });
    });
  }
  
  // ============================================
  // SYNCHRONIZATION HELPER
  // ============================================
  
  function syncNewContent(container) {
    if (!hasGSAP) return;
    
    // Ensure new elements are visible
    const newElements = container.querySelectorAll('.card, .product-item, .cart-item');
    newElements.forEach(el => {
      el.style.opacity = '1';
      el.style.visibility = 'visible';
    });
    
    // Animate new elements in
    gsap.from(newElements, {
      y: 30,
      opacity: 0,
      scale: 0.95,
      duration: 0.6,
      stagger: 0.08,
      ease: 'back.out(1.2)'
    });
    
    // Refresh ScrollTrigger
    if (typeof ScrollTrigger !== 'undefined') {
      ScrollTrigger.refresh();
    }
  }
  
  // Export functions for external use
  window.gsapAnimations = {
    success: createSuccessTimeline,
    error: createErrorTimeline,
    badge: animateBadge,
    cartAdd: animateCartAdd,
    cartRemove: animateCartRemove,
    searchResults: animateSearchResults,
    loading: showLoadingAnimation,
    syncNewContent: syncNewContent,
    refresh: () => {
      if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.refresh();
      }
    }
  };
  
})();
