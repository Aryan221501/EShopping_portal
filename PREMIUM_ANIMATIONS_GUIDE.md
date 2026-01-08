# Premium Anime.js Animations Guide

## Overview
This e-shop features premium, optimized animations using the anime.js library. All animations are responsive, performance-optimized, and respect user preferences.

## Features

### 🎨 Animation Categories

#### 1. **Page Entrance Animations**
- Hero sections fade in with smooth transitions
- Cards stagger in with scale and opacity effects
- Navbar slides down from top
- Buttons pop in with elastic easing

#### 2. **Hover Animations**
- Cards lift with 3D tilt effect based on mouse position
- Parallax tilt follows cursor movement
- Buttons scale up on hover with elastic bounce
- Glow effects on hover

#### 3. **Scroll Animations**
- Elements fade in as they enter viewport
- Intersection Observer for performance
- Smooth transitions with cubic easing

#### 4. **Click Effects**
- Ripple effect on every click
- Particle burst on special actions
- Button press animations

#### 5. **Cart Animations**
- Badge bounce when items added
- Quantity change pulse effect
- Item removal slide-out animation
- Total update color transition

#### 6. **Product Animations**
- Category filter with fade in/out
- Load more with stagger effect
- Add to cart success animation
- Recommendation fade-in

#### 7. **Special Effects**
- Floating badges
- Price tag pulse
- Navbar gradient animation
- Search bar focus glow

## Performance Optimizations

### ✅ Desktop Only
Animations only run on screens wider than 768px to preserve mobile performance.

### ✅ Reduced Motion Support
Respects `prefers-reduced-motion` media query for accessibility.

### ✅ Hardware Acceleration
Uses `will-change` and `transform` properties for GPU acceleration.

### ✅ Efficient Selectors
Targets specific elements to minimize reflows and repaints.

## Animation Functions

### Available Global Functions

```javascript
// Shake an element (for errors)
window.animeEffects.shake(element);

// Show success notification
window.animeEffects.success(element);

// Create particle burst
window.animeEffects.particles(x, y);

// Animate cart badge
window.animeEffects.cartBadge();
```

## Usage Examples

### Add Custom Animation

```javascript
if (typeof anime !== 'undefined') {
  anime({
    targets: '.my-element',
    translateY: [20, 0],
    opacity: [0, 1],
    duration: 600,
    easing: 'easeOutCubic'
  });
}
```

### Stagger Animation

```javascript
anime({
  targets: '.card',
  opacity: [0, 1],
  translateY: [40, 0],
  delay: anime.stagger(60),
  duration: 600,
  easing: 'easeOutCubic'
});
```

### Elastic Bounce

```javascript
anime({
  targets: '.button',
  scale: [0, 1],
  duration: 500,
  easing: 'easeOutElastic(1, .6)'
});
```

## Easing Functions

- `easeOutCubic` - Smooth deceleration
- `easeOutExpo` - Dramatic deceleration
- `easeOutElastic(1, .6)` - Bouncy effect
- `easeInOutSine` - Smooth acceleration/deceleration
- `linear` - Constant speed

## CSS Classes

### Animation Helpers

```css
.hover-lift        /* Lift on hover */
.scale-hover       /* Scale on hover */
.rotate-hover      /* Rotate on hover */
.bounce            /* Continuous bounce */
.shake             /* Shake animation */
.gradient-text     /* Animated gradient text */
.neon-glow         /* Neon glow effect */
```

### Stagger Classes

```css
.stagger-1 through .stagger-5
/* Add delays for sequential animations */
```

## Best Practices

1. **Always check if anime.js is loaded**
   ```javascript
   if (typeof anime !== 'undefined') {
     // Your animation code
   }
   ```

2. **Use appropriate durations**
   - Quick interactions: 200-400ms
   - Page transitions: 500-800ms
   - Attention-grabbing: 600-1000ms

3. **Choose the right easing**
   - Entrances: `easeOutCubic`, `easeOutExpo`
   - Exits: `easeInCubic`
   - Bouncy: `easeOutElastic`
   - Smooth: `easeInOutSine`

4. **Optimize for performance**
   - Use `transform` and `opacity` when possible
   - Avoid animating `width`, `height`, `top`, `left`
   - Add `will-change` for frequently animated properties

5. **Respect user preferences**
   - Check for `prefers-reduced-motion`
   - Provide fallbacks for non-animated states

## Animation Timeline

### Page Load Sequence
1. Navbar slides down (0ms)
2. Hero text fades in (100ms delay)
3. Cards stagger in (200ms delay, 60ms between each)
4. Buttons pop in (400ms delay, 50ms between each)

### Cart Operations
1. Button press animation (immediate)
2. API call
3. Success animation (on response)
4. Badge bounce
5. Particle effect

## Troubleshooting

### Animations not working?
1. Check if anime.js CDN is loaded
2. Verify screen width > 768px
3. Check browser console for errors
4. Ensure elements exist in DOM

### Performance issues?
1. Reduce number of animated elements
2. Increase stagger delay
3. Simplify animation properties
4. Check for conflicting CSS transitions

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Files

- `/static/js/smooth-animations.js` - Main animation logic
- `/static/css/animations.css` - Animation styles and keyframes
- `/templates/base.html` - Base template with anime.js CDN

## Credits

Powered by [anime.js](https://animejs.com/) - A lightweight JavaScript animation library.
