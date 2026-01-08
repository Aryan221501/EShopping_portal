# 🎨 Advanced Animations Guide

## Overview

Your e-shop now features smooth, professional animations powered by **Anime.js** with cursor-reactive effects!

---

## ✨ Features Implemented

### 1. Custom Cursor
- **Dot cursor** - Follows mouse instantly
- **Outline cursor** - Smooth delayed follow
- **Interactive states** - Scales on hover over clickable elements
- **Color changes** - Blue accent on interactive elements
- **Click feedback** - Shrinks on click

### 2. Card Animations
- **3D Tilt Effect** - Cards tilt based on mouse position
- **Hover Scale** - Slight zoom on hover
- **Shimmer Effect** - Light sweep across card on hover
- **Glow Effect** - Blue glow shadow on hover
- **Parallax Scroll** - Cards move at different speeds while scrolling

### 3. Button Animations
- **Hover Scale** - Buttons grow slightly on hover
- **Glow Shadow** - Blue shadow appears on hover
- **Ripple Effect** - Click creates expanding ripple
- **Press Effect** - Shrinks slightly when clicked

### 4. Page Load Animations
- **Navbar Slide** - Slides down from top
- **Container Fade** - Fades in with upward motion
- **Card Stagger** - Cards appear one by one
- **Heading Slide** - Headings slide in from left

### 5. Scroll Animations
- **Parallax Effect** - Background elements move slower
- **Fade In on Scroll** - Elements appear as you scroll
- **Smooth Scroll** - Animated scrolling for anchor links

### 6. Special Effects
- **Floating Badges** - Category badges float up and down
- **Pulse Price Tags** - Prices pulse to draw attention
- **Gradient Navbar** - Animated gradient background
- **Click Ripples** - Ripple effect on any click
- **Particle Effect** - Floating particles in background

---

## 🎯 How It Works

### Cursor Tracking
```javascript
// Instant dot follow
document.addEventListener('mousemove', (e) => {
  cursorDot.style.left = e.clientX + 'px';
  cursorDot.style.top = e.clientY + 'px';
});

// Smooth outline follow with easing
function animateOutline() {
  outlineX += (mouseX - outlineX) * 0.15;
  outlineY += (mouseY - outlineY) * 0.15;
  requestAnimationFrame(animateOutline);
}
```

### 3D Card Tilt
```javascript
card.addEventListener('mousemove', function(e) {
  const rotateX = (y - centerY) / 15;
  const rotateY = (centerX - x) / 15;
  
  anime({
    targets: this,
    rotateX: rotateX,
    rotateY: rotateY,
    duration: 300
  });
});
```

### Stagger Animation
```javascript
anime({
  targets: '.card',
  translateY: [50, 0],
  opacity: [0, 1],
  delay: anime.stagger(100),  // 100ms between each
  duration: 800
});
```

---

## 🎨 Animation Types

### 1. Transform Animations
- `translateX/Y/Z` - Move elements
- `scale` - Resize elements
- `rotate` - Rotate elements
- `skew` - Skew elements

### 2. Opacity Animations
- Fade in/out effects
- Smooth transitions

### 3. Color Animations
- Border color changes
- Background color transitions
- Shadow color shifts

### 4. Path Animations
- SVG path animations
- Custom motion paths

---

## 🛠️ Customization

### Change Cursor Size
Edit `static/css/animations.css`:
```css
#cursor-dot {
  width: 8px;  /* Change size */
  height: 8px;
}

#cursor-outline {
  width: 30px;  /* Change size */
  height: 30px;
}
```

### Adjust Animation Speed
Edit `static/js/animations.js`:
```javascript
anime({
  targets: '.card',
  duration: 800,  /* Change duration (ms) */
  easing: 'easeOutExpo'  /* Change easing */
});
```

### Change Easing Functions
Available easings:
- `linear` - Constant speed
- `easeInQuad` - Slow start
- `easeOutQuad` - Slow end
- `easeInOutQuad` - Slow start and end
- `easeOutExpo` - Very smooth end
- `easeOutElastic` - Bouncy end
- `spring` - Spring physics

### Disable Specific Animations
Comment out in `static/js/animations.js`:
```javascript
// Disable card tilt
// initCardAnimations();

// Disable particles
// initParticleEffect();
```

---

## 📱 Mobile Optimization

Animations automatically adjust for mobile:
- Cursor effects disabled on touch devices
- Reduced animation intensity
- Particles hidden on mobile
- Simplified transitions

### Accessibility
Respects `prefers-reduced-motion`:
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 🎭 Animation Classes

### Add to HTML Elements

**Hover Effects:**
```html
<div class="hover-lift">Lifts on hover</div>
<div class="scale-hover">Scales on hover</div>
<div class="rotate-hover">Rotates on hover</div>
```

**Animations:**
```html
<div class="bounce">Bounces continuously</div>
<div class="pulse">Pulses continuously</div>
<div class="shimmer">Shimmer effect</div>
```

**Scroll Effects:**
```html
<div class="fade-in-scroll">Fades in on scroll</div>
```

**Stagger Delays:**
```html
<div class="stagger-1">Delay 0.1s</div>
<div class="stagger-2">Delay 0.2s</div>
<div class="stagger-3">Delay 0.3s</div>
```

---

## 🚀 Performance

### Optimizations Implemented:
1. **RequestAnimationFrame** - Smooth 60fps animations
2. **Will-change** - GPU acceleration hints
3. **Transform over position** - Hardware accelerated
4. **Debouncing** - Scroll events optimized
5. **Lazy loading** - Animations init on demand

### Performance Tips:
- Animations use CSS transforms (GPU accelerated)
- Minimal repaints and reflows
- Efficient event listeners
- Cached selectors
- Throttled scroll events

---

## 🎨 Color Scheme

Animations use CSS variables:
```css
--accent-color: #58a6ff;
--accent-hover: #1f6feb;
--text-primary: #c9d1d9;
--text-secondary: #8b949e;
```

Change in `static/css/dark-theme.css` to customize colors.

---

## 📊 Animation Timeline

**Page Load (0-2s):**
1. Navbar slides down (0-0.8s)
2. Container fades in (0.2-1.2s)
3. Cards stagger in (0.4-1.6s)
4. Headings slide in (0.4-1.2s)

**User Interaction:**
- Hover: Instant feedback (<300ms)
- Click: Ripple effect (600ms)
- Scroll: Parallax (continuous)

---

## 🔧 Troubleshooting

### Cursor Not Showing
**Check:**
1. Is anime.js loaded? (Check browser console)
2. Are cursor elements in DOM? (Inspect page)
3. Is JavaScript enabled?

**Fix:**
```javascript
// Verify in console
console.log(document.getElementById('cursor-dot'));
```

### Animations Too Slow
**Solution:**
Reduce duration in `animations.js`:
```javascript
duration: 400,  // Instead of 800
```

### Animations Too Fast
**Solution:**
Increase duration:
```javascript
duration: 1200,  // Instead of 800
```

### Cards Not Tilting
**Check:**
1. Is mouse moving over card?
2. Is 3D transform supported?

**Fix:**
```css
.card {
  transform-style: preserve-3d;
  perspective: 1000px;
}
```

### Performance Issues
**Solutions:**
1. Reduce particle count
2. Disable parallax on scroll
3. Simplify card animations
4. Remove shimmer effects

---

## 🎯 Best Practices

### DO:
✅ Use transform and opacity (GPU accelerated)
✅ Keep animations under 500ms for interactions
✅ Use easing functions for natural feel
✅ Test on mobile devices
✅ Respect user preferences (reduced motion)

### DON'T:
❌ Animate width/height (causes reflow)
❌ Use too many simultaneous animations
❌ Ignore mobile performance
❌ Overuse animations (less is more)
❌ Forget accessibility

---

## 📚 Resources

### Anime.js Documentation
- Website: https://animejs.com/
- GitHub: https://github.com/juliangarnier/anime
- Examples: https://animejs.com/documentation/

### CSS Animations
- MDN: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations
- Can I Use: https://caniuse.com/css-animation

### Performance
- Web.dev: https://web.dev/animations/
- Google Developers: https://developers.google.com/web/fundamentals/performance/rendering

---

## 🎉 Summary

Your e-shop now features:
- ✨ Custom cursor with smooth following
- 🎴 3D card tilt effects
- 💫 Smooth page transitions
- 🌊 Parallax scrolling
- ✨ Hover animations
- 💥 Click ripple effects
- 🎨 Gradient backgrounds
- 🎯 Floating elements
- ⚡ Fast and optimized
- 📱 Mobile responsive
- ♿ Accessible

**All animations are smooth, professional, and enhance user experience!** 🚀

---

## 🔄 Updates

To update animations:
1. Edit `static/js/animations.js` for behavior
2. Edit `static/css/animations.css` for styles
3. Refresh browser (Ctrl+F5)

To add new animations:
1. Add anime() call in `animations.js`
2. Add CSS class in `animations.css`
3. Apply class to HTML elements

**Enjoy your beautifully animated e-shop!** ✨
