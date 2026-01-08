from django.core.management.base import BaseCommand
from store.models import Category, Product
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Populate database with 40-50 sample products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating categories...')
        
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Fashion', 'slug': 'fashion'},
            {'name': 'Home & Kitchen', 'slug': 'home-kitchen'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Sports', 'slug': 'sports'},
            {'name': 'Beauty', 'slug': 'beauty'},
            {'name': 'Toys', 'slug': 'toys'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
            categories[cat_data['slug']] = cat
            if created:
                self.stdout.write(f'  Created category: {cat.name}')

        
        self.stdout.write('Creating products...')
        
        # Product data
        products_data = [
            # Electronics
            {'title': 'Wireless Bluetooth Headphones',
             'description': 'Premium noise-cancelling wireless headphones with 30-hour battery life and superior sound quality. Advanced active noise cancellation technology blocks out ambient noise, allowing you to focus on your music, podcasts, or calls. Features include touch controls, voice assistant compatibility, and a comfortable over-ear design perfect for long listening sessions.',
             'price': '2999.00', 'category': 'electronics'},
            {'title': 'Smart Watch Pro',
             'description': 'Advanced fitness tracker with heart rate monitor, GPS, and waterproof design. Tracks your steps, calories burned, sleep patterns, and heart rate throughout the day. Includes multiple sports modes, music storage, and smartphone notifications. Water-resistant up to 50 meters, making it perfect for swimming and all-weather use.',
             'price': '4999.00', 'category': 'electronics'},
            {'title': 'USB-C Fast Charger',
             'description': '65W fast charging adapter compatible with laptops, tablets, and smartphones. GaN technology provides ultra-fast charging while staying cool. Features multiple ports for simultaneous charging of multiple devices. Compact design perfect for travel with safety protections against overheating, overcurrent, and short circuits.',
             'price': '1299.00', 'category': 'electronics'},
            {'title': 'Wireless Mouse',
             'description': 'Ergonomic wireless mouse with adjustable DPI and long battery life. Features include 1600-2400 DPI sensitivity options, silent button clicks, and a comfortable contoured shape that reduces wrist strain. Works with multiple devices via USB receiver and Bluetooth.',
             'price': '799.00', 'category': 'electronics'},
            {'title': '4K Webcam',
             'description': 'Ultra HD webcam with auto-focus and built-in microphone for video calls. 4K resolution with smooth 30fps recording, perfect for streaming, conferencing, and content creation. Includes privacy cover, adjustable stand, and ring light for better lighting.',
             'price': '3499.00', 'category': 'electronics'},
            {'title': 'Portable Power Bank 20000mAh',
             'description': 'High-capacity power bank with dual USB ports and fast charging. Features include Power Delivery, Quick Charge 3.0, and multiple safety protections. LED display shows remaining charge. Compatible with smartphones, tablets, and laptops.',
             'price': '1899.00', 'category': 'electronics'},
            {'title': 'Mechanical Gaming Keyboard',
             'description': 'RGB backlit mechanical keyboard with customizable keys. Features tactile blue switches, anti-ghosting technology, and programmable macro keys. Customizable RGB lighting with multiple effects. Durable construction with 80-million keystroke lifespan.',
             'price': '5499.00', 'category': 'electronics'},

            # Fashion
            {'title': 'Cotton T-Shirt Pack',
             'description': 'Set of 3 premium cotton t-shirts in assorted colors. Made from 100% organic cotton with a comfortable fit. Pre-shrunk fabric that maintains its shape after washing. Available in sizes S-XXL. Machine washable with colorfast dyes.',
             'price': '999.00', 'category': 'fashion'},
            {'title': 'Denim Jeans',
             'description': 'Classic fit denim jeans with stretch fabric for comfort. Made from premium denim with 2% elastane for flexibility. Features include five pockets, button-fly closure, and reinforced stress points. Available in various washes from light to dark.',
             'price': '1799.00', 'category': 'fashion'},
            {'title': 'Leather Wallet',
             'description': 'Genuine leather wallet with multiple card slots and coin pocket. Handcrafted from full-grain leather that ages beautifully. Features 12 card slots, 2 bill compartments, and a zip coin pocket. Dimensions: 4.3" x 3.1" x 0.8".',
             'price': '899.00', 'category': 'fashion'},
            {'title': 'Running Shoes',
             'description': 'Lightweight running shoes with cushioned sole and breathable mesh. Features include shock absorption, arch support, and moisture-wicking fabric. Perfect for both running and everyday wear. Reflective details for low-light visibility.',
             'price': '2499.00', 'category': 'fashion'},
            {'title': 'Casual Backpack',
             'description': 'Water-resistant backpack with laptop compartment and USB charging port. Features padded laptop sleeve for up to 15.6" laptops, multiple organizational pockets, and USB charging cable inside. Made from durable polyester with padded straps.',
             'price': '1599.00', 'category': 'fashion'},
            {'title': 'Sunglasses UV Protection',
             'description': 'Polarized sunglasses with UV400 protection and stylish frame. Lenses block 100% of UVA and UVB radiation. Features include polarized lenses to reduce glare, lightweight frame, and anti-scratch coating. Comes with protective case.',
             'price': '699.00', 'category': 'fashion'},
            {'title': 'Winter Jacket',
             'description': 'Warm winter jacket with hood and multiple pockets. Features include water-resistant fabric, insulated filling, adjustable hood and cuffs, and multiple zippered pockets. Available in black, navy, and olive green.',
             'price': '3999.00', 'category': 'fashion'},

            # Home & Kitchen
            {'title': 'Non-Stick Cookware Set',
             'description': '5-piece non-stick cookware set with glass lids. Features PFOA-free non-stick coating, aluminum construction for even heating, and stainless steel handles. Includes 2 saucepans, 2 frying pans, and a stockpot. Oven safe up to 180°C.',
             'price': '2999.00', 'category': 'home-kitchen'},
            {'title': 'Electric Kettle',
             'description': '1.8L electric kettle with auto shut-off and boil-dry protection. Boils water in under 5 minutes with 3000W heating element. Features include cordless design, 360° swivel base, water level window, and concealed heating element.',
             'price': '1299.00', 'category': 'home-kitchen'},
            {'title': 'Vacuum Cleaner',
             'description': 'Powerful bagless vacuum cleaner with HEPA filter. Features include 20kPa suction power, LED headlights, multiple attachments for different surfaces, and washable filters. Cyclonic technology maintains suction power. 2.5L dust cup capacity.',
             'price': '4999.00', 'category': 'home-kitchen'},
            {'title': 'Bed Sheet Set',
             'description': 'Premium cotton bed sheet set with pillow covers. Features 400-thread count, 100% cotton sateen weave, and deep pockets to fit mattresses up to 16 inches. Includes fitted sheet, flat sheet, and 2 pillowcases. Available in multiple colors.',
             'price': '1499.00', 'category': 'home-kitchen'},
            {'title': 'LED Desk Lamp',
             'description': 'Adjustable LED desk lamp with touch control and USB charging. Features include 5 brightness levels, adjustable color temperature (3000K-6000K), flexible gooseneck, and built-in wireless charging pad. Energy-efficient with 50,000-hour LED lifespan.',
             'price': '899.00', 'category': 'home-kitchen'},
            {'title': 'Storage Containers Set',
             'description': 'Airtight food storage containers in various sizes. Features include leak-proof design, stackable construction, and clear bodies for easy identification. Made from BPA-free materials. 10-piece set with 5 different sizes.',
             'price': '799.00', 'category': 'home-kitchen'},
            {'title': 'Wall Clock',
             'description': 'Modern silent wall clock with large numbers. Features include quiet sweeping movement, non-ticking mechanism, and elegant design. Diameter: 30cm. Requires 1 AA battery. Easy to hang with pre-attached mounting hardware.',
             'price': '599.00', 'category': 'home-kitchen'},

            # Books
            {'title': 'Python Programming Guide',
             'description': 'Comprehensive guide to Python programming for beginners and experts. Covers basic syntax, data structures, object-oriented programming, and advanced topics like web development and data science. Includes practical examples and exercises. 500 pages with clear explanations.',
             'price': '599.00', 'category': 'books'},
            {'title': 'The Art of War',
             'description': 'Classic strategy book with modern commentary. Ancient Chinese military treatise attributed to Sun Tzu. Translated with annotations connecting ancient strategies to modern business and life. Includes practical applications and case studies.',
             'price': '299.00', 'category': 'books'},
            {'title': 'Atomic Habits',
             'description': 'Proven framework for improving every day. Learn how tiny changes can transform your life, career, and relationships. Evidence-based approach to habit formation with practical strategies. #1 New York Times bestseller with over 4 million copies sold.',
             'price': '449.00', 'category': 'books'},
            {'title': 'Think and Grow Rich',
             'description': 'Timeless principles for personal achievement. Classic book on success principles and the psychology of achievement. Based on Napoleon Hill\'s study of successful individuals. Includes 13 steps to success and powerful mindset techniques.',
             'price': '349.00', 'category': 'books'},
            {'title': 'Data Science Handbook',
             'description': 'Complete guide to data science and machine learning. Covers statistics, Python, SQL, visualization, and machine learning algorithms. Practical examples with real datasets and case studies. Perfect for beginners and intermediate learners.',
             'price': '799.00', 'category': 'books'},
            {'title': 'The Alchemist',
             'description': 'Inspiring tale about following your dreams. International bestseller about a shepherd boy who travels from Spain to Egypt seeking treasure. Themes include destiny, dreams, and the pursuit of one\'s Personal Legend. Translated into 80 languages.',
             'price': '399.00', 'category': 'books'},

            # Sports
            {'title': 'Yoga Mat',
             'description': 'Non-slip yoga mat with carrying strap. Features 6mm thickness for cushioning and support, eco-friendly materials, and texture for grip. Dimensions: 72" x 24". Includes carrying strap and online yoga class access. Machine washable.',
             'price': '899.00', 'category': 'sports'},
            {'title': 'Dumbbell Set',
             'description': 'Adjustable dumbbell set with storage rack. Features 5-50 lbs adjustment in 2.5 lb increments, space-saving design, and quick-lock mechanism. Includes workout guide and storage rack. Perfect for home gyms with limited space.',
             'price': '3999.00', 'category': 'sports'},
            {'title': 'Resistance Bands',
             'description': 'Set of 5 resistance bands for home workout. Features different resistance levels (light, medium, heavy, extra heavy, ultra heavy), door anchor, and accessories. Includes exercise guide with 100+ workouts. Perfect for strength training and rehabilitation.',
             'price': '699.00', 'category': 'sports'},
            {'title': 'Sports Water Bottle',
             'description': 'Insulated stainless steel water bottle 1L. Keeps drinks cold for 24 hours or hot for 12 hours. Features wide mouth for easy filling and cleaning, leak-proof design, and sweat-free exterior. BPA-free with ergonomic loop cap.',
             'price': '499.00', 'category': 'sports'},
            {'title': 'Badminton Racket',
             'description': 'Professional badminton racket with cover. Features lightweight graphite frame, shock absorber, and comfortable grip. Includes protective cover and shuttlecocks. Perfect for beginners and intermediate players.',
             'price': '1299.00', 'category': 'sports'},
            {'title': 'Gym Gloves',
             'description': 'Breathable gym gloves with wrist support. Features neoprene wrist wrap, anti-slip padding, and breathable mesh. Gel padding in high-pressure areas for comfort. Improves grip and prevents calluses during workouts.',
             'price': '399.00', 'category': 'sports'},
            {'title': 'Jump Rope',
             'description': 'Adjustable speed jump rope for cardio workout. Features ball bearings for smooth rotation, adjustable length (7-9 feet), and foam handles for comfort. Perfect for HIIT workouts and improving coordination and agility.',
             'price': '299.00', 'category': 'sports'},

            # Beauty
            {'title': 'Face Serum Vitamin C',
             'description': 'Brightening face serum with natural ingredients. Features 20% vitamin C, hyaluronic acid, and vitamin E for anti-aging benefits. Reduces hyperpigmentation, fine lines, and brightens complexion. Paraben and sulfate-free. 30ml bottle.',
             'price': '899.00', 'category': 'beauty'},
            {'title': 'Hair Dryer',
             'description': 'Professional hair dryer with multiple heat settings. Features ionic technology, ceramic coating, and 6 heat/speed settings. Reduces frizz and drying time by 50%. Includes concentrator and diffuser attachments.',
             'price': '1799.00', 'category': 'beauty'},
            {'title': 'Makeup Brush Set',
             'description': 'Complete makeup brush set with storage case. Features 15 professional brushes made with synthetic bristles. Includes brushes for foundation, eyes, and lips. Travel-friendly storage case with mirror. Cruelty-free materials.',
             'price': '1299.00', 'category': 'beauty'},
            {'title': 'Moisturizing Cream',
             'description': 'Hydrating face cream for all skin types. Features hyaluronic acid, ceramides, and SPF 15. Provides 24-hour hydration, strengthens skin barrier, and protects from environmental damage. Fragrance-free and non-comedogenic.',
             'price': '699.00', 'category': 'beauty'},
            {'title': 'Perfume Gift Set',
             'description': 'Luxury perfume gift set with 3 fragrances. Contains 3 x 100ml bottles of popular scents: floral, woody, and fresh. Suitable for gifting with elegant packaging. Includes notes of jasmine, sandalwood, and citrus.',
             'price': '2499.00', 'category': 'beauty'},
            {'title': 'Nail Care Kit',
             'description': 'Professional nail care kit with tools. Features nail clippers, cuticle pusher, nail file, and buffer. Includes cuticle oil and hand cream. All tools in a convenient storage case. Stainless steel construction for durability.',
             'price': '599.00', 'category': 'beauty'},

            # Toys
            {'title': 'Building Blocks Set',
             'description': '500-piece building blocks for creative play. Features colorful, durable ABS plastic blocks that connect easily. Encourages creativity, problem-solving, and fine motor skills. Compatible with other major building block brands. Ages 4+.',
             'price': '1499.00', 'category': 'toys'},
            {'title': 'Remote Control Car',
             'description': 'High-speed RC car with rechargeable battery. Features 2.4GHz remote control, 360° rotation, LED lights, and high-speed motor. Full-range control up to 50 meters. Rechargeable battery provides 20-30 minutes of playtime.',
             'price': '1999.00', 'category': 'toys'},
            {'title': 'Puzzle Game 1000 Pieces',
             'description': 'Challenging jigsaw puzzle with beautiful artwork. Features high-quality cardboard pieces with anti-glare surface. Completed puzzle measures 26.6" x 19.3". Perfect for family bonding and relaxation. Ages 10+.',
             'price': '699.00', 'category': 'toys'},
            {'title': 'Board Game Family Pack',
             'description': 'Collection of classic board games for family fun. Includes 4 different games: checkers, chess, backgammon, and Ludo. Compact folding board with built-in piece storage. Perfect for game nights and travel.',
             'price': '1299.00', 'category': 'toys'},
            {'title': 'Stuffed Teddy Bear',
             'description': 'Soft and cuddly teddy bear 50cm. Features ultra-soft plush material, embroidered face, and polyester filling. Machine washable. Perfect gift for children and adults alike. Ages 3+.',
             'price': '899.00', 'category': 'toys'},
            {'title': 'Art Supplies Set',
             'description': 'Complete art supplies set with colors and brushes. Features 24 colored pencils, 12 watercolor cakes, 3 brushes, and drawing pad. High-quality materials safe for children. Perfect for developing artistic skills and creativity.',
             'price': '1199.00', 'category': 'toys'},
            {'title': 'Educational Robot Kit',
             'description': 'STEM learning robot kit for kids. Features programmable robot, sensors, and mobile app control. Teaches coding, electronics, and engineering concepts. Includes 20+ building projects and step-by-step instructions. Ages 8+.',
             'price': '2999.00', 'category': 'toys'},
        ]
        
        created_count = 0
        for prod_data in products_data:
            product, created = Product.objects.get_or_create(
                title=prod_data['title'],
                defaults={
                    'description': prod_data['description'],
                    'price': Decimal(prod_data['price']),
                    'category': categories[prod_data['category']]
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'  Created: {product.title}')
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} products!'))
        self.stdout.write(self.style.SUCCESS(f'Total products in database: {Product.objects.count()}'))
