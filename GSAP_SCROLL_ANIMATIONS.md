# 🎢 GSAP Scroll-Based Animations Guide

## Overview

Your AI E-Shop now features **advanced scroll-triggered animations** using GSAP ScrollTrigger, creating an immersive, interactive scrolling experience.

## Features Implemented

### 1. **Scroll Progress Indicator**
- Visual progress bar at top of page
- Shows how far user has scrolled
- Gradient color (blue to green)
- Smooth animation with scrub

### 2. **Fade In on Scroll**
- Cards fade in as they enter viewport
- Products animate from bottom
- Cart items reveal smoothly
- Opacity + translateY animation

### 3. **Parallax Scrolling**
- Containers move at different speeds
- Creates depth perception
- Subtle effect (not overwhelming)
- Smooth scrubbing

### 4. **Heading Reveals**
- H1, H2, H3 slide in from left
- Opacity fade combined with movement
- Triggered at 90% viewport
- Power3 easing for smoothness

### 5. **Button Scale Up**
- Buttons pop in from zero scale
- Back easing for bounce effect
- Triggered near bottom of viewport
- Elastic feel

### 6. **Badge Stagger**
- Category badges animate in sequence
- Stagger delay between each
- Slide down effect
- Coordinated timing

### 7. **Price Tag Reveal**
- Prices scale up with elastic bounce
- Eye-catching animation
- Draws attention to pricing
- Playful feel

### 8. **Search Results Slide**
- Results slide in from left
- Stagger effect for each item
- Smooth horizontal movement
- Quick duration

### 9. **Icon Rotation**
- Icons rotate in from -180°
- Back easing for overshoot
- Adds playfulness
- Subtle but noticeable

### 10. **Navbar Background Change**
- Navbar becomes translucent on scroll
- Backdrop blur effect
- Smooth color transition
- Triggered after 100px scroll

### 11. **Scroll to Top Button**
- Appears after scrolling down
- Smooth scroll animation
- Fades in/out based on position
- Click to return to top

## GSAP ScrollTrigger Configuration

### Basic Syntax
```javascript
gsap.from(element, {
  scrollTrigger: {
    trigger: element,
    start: 'top 85%',      // When top of element hits 85% of viewport
    end: 'top 20%',        // When top of element hits 20% of viewport
    toggleActions: 'play none none reverse',
    scrub: true,           // Smooth scrubbing
    markers: false         // Debug markers (set true for debugging)
  },
  y: 50,                   // Start 50px below
  opacity: 0,              // Start invisible
  duration: 0.8,           // Animation duration
  ease: 'power2.out'       // Easing function
});
```

### Toggle Actions
```
'play none none reverse'
 │    │    │    └─ onLeaveBack
 │    │    └────── onLeave
 │    └─────────── onEnterBack
 └──────────────── onEnter
```

## Animation Types

### 1. Fade In from Bottom
```javascript
gsap.from('.element', {
  scrollTrigger: { trigger: '.element', start: 'top 85%' },
  y: 50,
  opacity: 0,
  duration: 0.8
});
```

### 2. Parallax Effect
```javascript
gsap.to('.element', {
  scrollTrigger: {
    trigger: '.element',
    scrub: 1.5  // Smooth scrubbing
  },
  y: -20
});
```

### 3. Scale Up
```javascript
gsap.from('.element', {
  scrollTrigger: { trigger: '.element', start: 'top 90%' },
  scale: 0,
  duration: 0.6,
  ease: 'back.out(1.7)'
});
```

### 4. Rotate In
```javascript
gsap.from('.element', {
  scrollTrigger: { trigger: '.element', start: 'top 95%' },
  rotation: -180,
  opacity: 0,
  duration: 0.6
});
```

### 5. Stagger Animation
```javascript
gsap.from('.elements', {
  scrollTrigger: { trigger: '.elements', start: 'top 90%' },
  y: 20,
  opacity: 0,
  stagger: 0.1,  // 100ms between each
  duration: 0.6
});
```

## Scroll Progress Indicator

### HTML
```html
<div class="scroll-progress-container">
  <div class="progress-bar"></div>
</div>
```

### Animation
```javascript
gsap.to('.progress-bar', {
  scrollTrigger: {
    trigger: 'body',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 0.5
  },
  width: '100%'
});
```

## Scroll to Top Button

### HTML
```html
<div class="scroll-indicator" id="scroll-to-top">
  <i class="bi bi-arrow-up"></i>
</div>
```

### Functionality
```javascript
// Show/hide based on scroll
ScrollTrigger.create({
  start: 'top -200',
  onUpdate: (self) => {
    if (self.progress > 0.1) {
      scrollBtn.classList.add('visible');
    }
  }
});

// Smooth scroll to top
scrollBtn.addEventListener('click', () => {
  gsap.to(window, {
    scrollTo: { y: 0 },
    duration: 1,
    ease: 'power2.inOut'
  });
});
```

## Viewport Positions

```
Viewport (100%)
├─ 0%   (top)
├─ 20%  (near top)
├─ 50%  (middle)
├─ 80%  (near bottom)
└─ 100% (bottom)

Common Triggers:
- start: 'top 85%'  → Element enters near bottom
- start: 'top 50%'  → Element reaches middle
- start: 'top 20%'  → Element near top
```

## Easing Functions

| Easing | Effect | Use Case |
|--------|--------|----------|
| `power2.out` | Smooth deceleration | General animations |
| `power3.out` | Strong deceleration | Dramatic entrances |
| `back.out(1.7)` | Overshoot & settle | Buttons, badges |
| `elastic.out(1, 0.5)` | Bouncy | Prices, playful elements |
| `none` | Linear | Parallax, progress bars |

## Performance Tips

### ✅ Do
- Use `scrub` for smooth parallax
- Set `once: true` for one-time animations
- Use `toggleActions` for control
- Batch similar animations
- Use `will-change` CSS property

### ❌ Don't
- Animate too many elements
- Use complex calculations in scrub
- Forget to refresh ScrollTrigger
- Animate layout properties (width, height)
- Overuse parallax effects

## Debugging

### Enable Markers
```javascript
scrollTrigger: {
  trigger: element,
  markers: true  // Shows start/end points
}
```

### Console Commands
```javascript
// Refresh all ScrollTriggers
ScrollTrigger.refresh();

// Get all ScrollTriggers
ScrollTrigger.getAll();

// Kill all ScrollTriggers
ScrollTrigger.killAll();

// Check if element has ScrollTrigger
ScrollTrigger.getById('myId');
```

## Browser Support

✅ Chrome 90+  
✅ Firefox 88+  
✅ Safari 14+  
✅ Edge 90+  
✅ Mobile browsers (optimized)  

## Files

- `/static/js/advanced-animations.js` - Scroll animation logic
- `/static/css/animations.css` - Scroll animation styles
- `/templates/base.html` - Progress bar & scroll button

## CDN Links

```html
<!-- GSAP Core -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

<!-- ScrollTrigger Plugin -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

<!-- ScrollToPlugin -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollToPlugin.min.js"></script>
```

## Customization

### Change Animation Speed
```javascript
duration: 1.2  // Slower
duration: 0.4  // Faster
```

### Adjust Trigger Point
```javascript
start: 'top 90%'  // Earlier
start: 'top 70%'  // Later
```

### Modify Parallax Speed
```javascript
scrub: 0.5  // Faster
scrub: 3    // Slower
```

### Change Stagger Delay
```javascript
stagger: 0.05  // Faster
stagger: 0.2   // Slower
```

## Examples

### Product Card Reveal
```javascript
gsap.from('.product-item', {
  scrollTrigger: {
    trigger: '.product-item',
    start: 'top 85%',
    toggleActions: 'play none none reverse'
  },
  y: 50,
  opacity: 0,
  scale: 0.95,
  duration: 0.8,
  ease: 'power2.out'
});
```

### Navbar Blur on Scroll
```javascript
ScrollTrigger.create({
  start: 'top -100',
  onEnter: () => {
    gsap.to('.navbar', {
      backgroundColor: 'rgba(22, 27, 34, 0.95)',
      backdropFilter: 'blur(10px)',
      duration: 0.3
    });
  }
});
```

### Smooth Parallax
```javascript
gsap.to('.container', {
  scrollTrigger: {
    trigger: '.container',
    start: 'top bottom',
    end: 'bottom top',
    scrub: 1.5
  },
  y: -20
});
```

## Summary

✅ **10+ scroll animations** implemented  
✅ **ScrollTrigger** for viewport detection  
✅ **ScrollToPlugin** for smooth scrolling  
✅ **Progress indicator** shows scroll position  
✅ **Scroll-to-top button** for easy navigation  
✅ **Parallax effects** for depth  
✅ **Stagger animations** for coordination  
✅ **Performance optimized** for smooth 60fps  

Your site now has **professional scroll-based animations** that create an engaging, interactive experience! 🎢
