from django.core.management.base import BaseCommand
from store.models import Category, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate database with 100+ comprehensive product catalog'

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
            {'name': 'Appliances', 'slug': 'appliances'},
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
        
        self.stdout.write('Creating comprehensive product catalog...')
        
        # Comprehensive product data
        products_data = [
            # ELECTRONICS - Phones
            {'title': 'Samsung Galaxy S23 5G', 'description': 'Latest flagship smartphone with 5G, 128GB storage, triple camera system, and stunning AMOLED display', 'price': '74999.00', 'category': 'electronics'},
            {'title': 'iPhone 14 Pro Max', 'description': 'Apple iPhone with A16 Bionic chip, 256GB storage, ProMotion display, and advanced camera', 'price': '129999.00', 'category': 'electronics'},
            {'title': 'OnePlus 11R 5G', 'description': 'Fast charging smartphone with Snapdragon 8+ Gen 1, 8GB RAM, and 120Hz AMOLED display', 'price': '39999.00', 'category': 'electronics'},
            {'title': 'Xiaomi Redmi Note 12 Pro', 'description': 'Budget-friendly phone with 50MP camera, 5000mAh battery, and 67W fast charging', 'price': '18999.00', 'category': 'electronics'},
            {'title': 'Google Pixel 7 Pro', 'description': 'Pure Android experience with excellent camera, Google Tensor G2 chip, and clean software', 'price': '84999.00', 'category': 'electronics'},
            {'title': 'Realme GT Neo 3', 'description': 'Gaming phone with MediaTek Dimensity 8100, 150W fast charging, and RGB lighting', 'price': '36999.00', 'category': 'electronics'},
            
            # ELECTRONICS - Laptops
            {'title': 'Dell XPS 13 Laptop', 'description': 'Ultra-portable laptop with Intel Core i7 12th Gen, 16GB RAM, 512GB SSD, and InfinityEdge display', 'price': '94999.00', 'category': 'electronics'},
            {'title': 'MacBook Air M2', 'description': 'Apple silicon laptop with M2 chip, incredible battery life, 8GB RAM, and Liquid Retina display', 'price': '114900.00', 'category': 'electronics'},
            {'title': 'HP Pavilion Gaming Laptop', 'description': 'Gaming laptop with NVIDIA RTX 3050, Intel i5 12th Gen, 8GB RAM, and 144Hz display', 'price': '64999.00', 'category': 'electronics'},
            {'title': 'Lenovo ThinkPad E14', 'description': 'Business laptop with Intel i5, 8GB RAM, 256GB SSD, and military-grade durability', 'price': '54999.00', 'category': 'electronics'},
            {'title': 'ASUS VivoBook 15', 'description': 'Everyday laptop with AMD Ryzen 5, 8GB RAM, 512GB SSD, and lightweight design', 'price': '42999.00', 'category': 'electronics'},
            {'title': 'Acer Aspire 5', 'description': 'Student laptop with Intel i3, 8GB RAM, 256GB SSD, and full HD display', 'price': '34999.00', 'category': 'electronics'},
            
            # ELECTRONICS - Headphones & Audio
            {'title': 'Sony WH-1000XM5 Headphones', 'description': 'Premium noise-cancelling wireless headphones with 30-hour battery and industry-leading sound', 'price': '29999.00', 'category': 'electronics'},
            {'title': 'Apple AirPods Pro 2nd Gen', 'description': 'True wireless earbuds with active noise cancellation, spatial audio, and MagSafe charging', 'price': '26900.00', 'category': 'electronics'},
            {'title': 'JBL Tune 510BT Wireless', 'description': 'Wireless on-ear headphones with powerful JBL Pure Bass and 40-hour battery life', 'price': '2999.00', 'category': 'electronics'},
            {'title': 'boAt Rockerz 450 Bluetooth', 'description': 'Budget wireless headphones with 15-hour playback, comfortable ear cushions, and bass boost', 'price': '1499.00', 'category': 'electronics'},
            {'title': 'Bose QuietComfort 45', 'description': 'Legendary noise cancellation with premium comfort, 24-hour battery, and TriPort technology', 'price': '32999.00', 'category': 'electronics'},
            {'title': 'Samsung Galaxy Buds2 Pro', 'description': 'Premium earbuds with intelligent ANC, 360 audio, and IPX7 water resistance', 'price': '17999.00', 'category': 'electronics'},
            
            # ELECTRONICS - Accessories
            {'title': 'Anker 65W USB-C Charger', 'description': 'Fast charging adapter with GaN technology, compatible with laptops, tablets, and phones', 'price': '2499.00', 'category': 'electronics'},
            {'title': 'Logitech MX Master 3S Mouse', 'description': 'Ergonomic wireless mouse with 8K DPI sensor, quiet clicks, and multi-device support', 'price': '8999.00', 'category': 'electronics'},
            {'title': 'Logitech C920 HD Webcam', 'description': 'Full HD 1080p webcam with auto-focus, stereo audio, and wide-angle lens', 'price': '5999.00', 'category': 'electronics'},
            {'title': 'Ambrane 20000mAh Power Bank', 'description': 'High-capacity power bank with 18W fast charging, dual USB ports, and LED display', 'price': '1899.00', 'category': 'electronics'},
            {'title': 'Cosmic Byte CB-GK-16 Keyboard', 'description': 'RGB mechanical gaming keyboard with blue switches, anti-ghosting, and metal body', 'price': '2499.00', 'category': 'electronics'},
            
            # FASHION - Shirts
            {'title': 'Levi\'s Men\'s Casual Shirt', 'description': 'Classic denim shirt with button-down collar, chest pockets, and regular fit', 'price': '1999.00', 'category': 'fashion'},
            {'title': 'Allen Solly Formal Shirt', 'description': 'Premium cotton formal shirt with slim fit, wrinkle-free fabric, and elegant design', 'price': '1499.00', 'category': 'fashion'},
            {'title': 'US Polo Assn T-Shirt Pack', 'description': 'Set of 3 premium cotton t-shirts in assorted colors with brand logo', 'price': '1299.00', 'category': 'fashion'},
            {'title': 'Peter England Checkered Shirt', 'description': 'Casual checkered shirt with spread collar and comfortable cotton fabric', 'price': '899.00', 'category': 'fashion'},
            
            # FASHION - Sweaters & Winter Wear
            {'title': 'Monte Carlo Wool Sweater', 'description': 'Warm wool blend sweater with V-neck design, perfect for winter', 'price': '1799.00', 'category': 'fashion'},
            {'title': 'Wrangler Hooded Sweatshirt', 'description': 'Comfortable cotton hoodie with kangaroo pocket and adjustable drawstring', 'price': '1299.00', 'category': 'fashion'},
            {'title': 'Puma Winter Jacket', 'description': 'Insulated winter jacket with hood, multiple pockets, and water-resistant fabric', 'price': '3999.00', 'category': 'fashion'},
            {'title': 'Adidas Fleece Pullover', 'description': 'Soft fleece pullover with half-zip design and ribbed cuffs', 'price': '2499.00', 'category': 'fashion'},
            
            # FASHION - Shoes
            {'title': 'Nike Air Max Running Shoes', 'description': 'Lightweight running shoes with Air Max cushioning, breathable mesh, and durable sole', 'price': '5999.00', 'category': 'fashion'},
            {'title': 'Adidas Ultraboost Sneakers', 'description': 'Premium sneakers with Boost technology, Primeknit upper, and responsive cushioning', 'price': '12999.00', 'category': 'fashion'},
            {'title': 'Puma Casual Sneakers', 'description': 'Stylish casual sneakers with comfortable insole and trendy design', 'price': '2999.00', 'category': 'fashion'},
            {'title': 'Red Tape Formal Shoes', 'description': 'Genuine leather formal shoes with cushioned insole and elegant finish', 'price': '2499.00', 'category': 'fashion'},
            {'title': 'Crocs Classic Clogs', 'description': 'Comfortable clogs with Croslite foam, ventilation ports, and easy to clean', 'price': '1999.00', 'category': 'fashion'},
            
            # FASHION - Accessories
            {'title': 'Fastrack Analog Watch', 'description': 'Stylish analog watch with leather strap, water resistance, and date display', 'price': '1499.00', 'category': 'fashion'},
            {'title': 'Titan Raga Women\'s Watch', 'description': 'Elegant women\'s watch with rose gold finish and slim design', 'price': '4999.00', 'category': 'fashion'},
            {'title': 'Wildcraft Backpack 35L', 'description': 'Durable backpack with laptop compartment, rain cover, and ergonomic straps', 'price': '1899.00', 'category': 'fashion'},
            {'title': 'Ray-Ban Aviator Sunglasses', 'description': 'Classic aviator sunglasses with UV400 protection and metal frame', 'price': '4999.00', 'category': 'fashion'},
            
            # BEAUTY & MAKEUP
            {'title': 'Lakme Absolute Foundation', 'description': 'Long-lasting liquid foundation with SPF 20, natural finish, and buildable coverage', 'price': '899.00', 'category': 'beauty'},
            {'title': 'Maybelline Fit Me Concealer', 'description': 'Lightweight concealer that hides dark circles and blemishes naturally', 'price': '499.00', 'category': 'beauty'},
            {'title': 'MAC Ruby Woo Lipstick', 'description': 'Iconic matte red lipstick with rich color payoff and long-lasting formula', 'price': '1900.00', 'category': 'beauty'},
            {'title': 'Nykaa Matte Nail Polish Set', 'description': 'Set of 5 trendy matte nail polishes in vibrant colors', 'price': '699.00', 'category': 'beauty'},
            {'title': 'Plum Vitamin C Face Serum', 'description': 'Brightening face serum with 15% Vitamin C, reduces dark spots and pigmentation', 'price': '1099.00', 'category': 'beauty'},
            {'title': 'Biotique Bio Kelp Shampoo', 'description': 'Natural protein shampoo for falling hair with kelp and mint extracts', 'price': '299.00', 'category': 'beauty'},
            {'title': 'Philips Hair Dryer', 'description': 'Professional hair dryer with 1200W power, cool shot button, and concentrator nozzle', 'price': '1299.00', 'category': 'beauty'},
            {'title': 'Vega Makeup Brush Set', 'description': 'Complete 12-piece makeup brush set with storage case and soft bristles', 'price': '899.00', 'category': 'beauty'},
            
            # SPORTS & FITNESS
            {'title': 'Nivia Storm Football', 'description': 'Professional football with rubber bladder, machine-stitched, size 5', 'price': '599.00', 'category': 'sports'},
            {'title': 'Yonex Badminton Racket', 'description': 'Lightweight badminton racket with isometric head shape and graphite frame', 'price': '1999.00', 'category': 'sports'},
            {'title': 'Cosco Cricket Bat', 'description': 'Kashmir willow cricket bat with comfortable grip and balanced weight', 'price': '1299.00', 'category': 'sports'},
            {'title': 'Strauss Yoga Mat 6mm', 'description': 'Non-slip yoga mat with carrying strap, eco-friendly material, and cushioned support', 'price': '699.00', 'category': 'sports'},
            {'title': 'Kore Adjustable Dumbbells', 'description': 'Set of 2 adjustable dumbbells with weight plates, total 20kg', 'price': '2999.00', 'category': 'sports'},
            {'title': 'Boldfit Resistance Bands Set', 'description': 'Set of 5 resistance bands with different resistance levels and door anchor', 'price': '599.00', 'category': 'sports'},
            {'title': 'Nivia Gym Gloves', 'description': 'Breathable gym gloves with wrist support, anti-slip palm, and adjustable strap', 'price': '399.00', 'category': 'sports'},
            {'title': 'Skipping Rope with Counter', 'description': 'Adjustable speed jump rope with digital counter and comfortable handles', 'price': '299.00', 'category': 'sports'},
            
            # SPORTS - Bottles & Accessories
            {'title': 'Milton Thermosteel Bottle 1L', 'description': 'Insulated stainless steel water bottle, keeps hot for 24hrs, cold for 24hrs', 'price': '699.00', 'category': 'sports'},
            {'title': 'Cello Puro Bottle 1L', 'description': 'BPA-free plastic water bottle with leak-proof cap and easy grip', 'price': '299.00', 'category': 'sports'},
            {'title': 'Tupperware Water Bottle', 'description': 'Durable water bottle with flip-top lid and measurement markings', 'price': '399.00', 'category': 'sports'},
            
            # HOME & KITCHEN - Appliances
            {'title': 'Philips Air Fryer', 'description': 'Healthy air fryer with rapid air technology, 4.1L capacity, and digital display', 'price': '8999.00', 'category': 'appliances'},
            {'title': 'Prestige Electric Kettle 1.5L', 'description': 'Stainless steel electric kettle with auto shut-off and boil-dry protection', 'price': '1099.00', 'category': 'appliances'},
            {'title': 'Bajaj Mixer Grinder 750W', 'description': 'Powerful mixer grinder with 3 jars, stainless steel blades, and overload protection', 'price': '3499.00', 'category': 'appliances'},
            {'title': 'Pigeon Induction Cooktop', 'description': 'Energy-efficient induction cooktop with touch controls and auto shut-off', 'price': '2299.00', 'category': 'appliances'},
            {'title': 'Havells Room Heater', 'description': 'Fan heater with adjustable thermostat, overheat protection, and 2000W power', 'price': '1899.00', 'category': 'appliances'},
            {'title': 'Usha Table Fan 400mm', 'description': 'High-speed table fan with 3-speed control, aerodynamic blades, and stable base', 'price': '1499.00', 'category': 'appliances'},
            {'title': 'Orient Wall Fan 400mm', 'description': 'Wall-mounted fan with remote control, timer function, and powerful air delivery', 'price': '2299.00', 'category': 'appliances'},
            {'title': 'Crompton Ceiling Fan 1200mm', 'description': 'Energy-efficient ceiling fan with high air delivery and elegant design', 'price': '1799.00', 'category': 'appliances'},
            
            # HOME & KITCHEN - Utensils & Cookware
            {'title': 'Prestige Non-Stick Cookware Set', 'description': '5-piece non-stick cookware set with glass lids and induction base', 'price': '2999.00', 'category': 'home-kitchen'},
            {'title': 'Hawkins Pressure Cooker 5L', 'description': 'Aluminum pressure cooker with safety valve and comfortable handles', 'price': '1899.00', 'category': 'home-kitchen'},
            {'title': 'Cello Opalware Dinner Set', 'description': '27-piece dinner set with plates, bowls, and serving dishes', 'price': '2499.00', 'category': 'home-kitchen'},
            {'title': 'Milton Casserole Set', 'description': 'Set of 3 insulated casseroles for keeping food hot, stainless steel', 'price': '1799.00', 'category': 'home-kitchen'},
            {'title': 'Pigeon Stainless Steel Kadai', 'description': 'Deep frying kadai with helper handle and induction compatible base', 'price': '899.00', 'category': 'home-kitchen'},
            {'title': 'Wonderchef Knife Set', 'description': '6-piece knife set with wooden block, stainless steel blades, and ergonomic handles', 'price': '1499.00', 'category': 'home-kitchen'},
            
            # HOME & KITCHEN - Storage & Organization
            {'title': 'Tupperware Storage Container Set', 'description': 'Set of 6 airtight food storage containers in various sizes', 'price': '1299.00', 'category': 'home-kitchen'},
            {'title': 'Solimo Vacuum Cleaner', 'description': 'Bagless vacuum cleaner with HEPA filter, 1000W power, and multiple attachments', 'price': '3999.00', 'category': 'home-kitchen'},
            {'title': 'Amazon Basics Bedsheet Set', 'description': 'Premium cotton bedsheet set with 2 pillow covers, king size', 'price': '1299.00', 'category': 'home-kitchen'},
            
            # BOOKS
            {'title': 'Python Crash Course Book', 'description': 'Comprehensive guide to Python programming for beginners with hands-on projects', 'price': '599.00', 'category': 'books'},
            {'title': 'The Alchemist by Paulo Coelho', 'description': 'Inspiring tale about following your dreams and finding your destiny', 'price': '299.00', 'category': 'books'},
            {'title': 'Atomic Habits by James Clear', 'description': 'Proven framework for improving every day with tiny changes', 'price': '449.00', 'category': 'books'},
            {'title': 'Think and Grow Rich', 'description': 'Timeless principles for personal achievement and financial success', 'price': '199.00', 'category': 'books'},
            {'title': 'Data Science Handbook', 'description': 'Complete guide to data science, machine learning, and AI with Python', 'price': '799.00', 'category': 'books'},
            {'title': 'The Psychology of Money', 'description': 'Timeless lessons on wealth, greed, and happiness', 'price': '349.00', 'category': 'books'},
            {'title': 'Rich Dad Poor Dad', 'description': 'What the rich teach their kids about money that the poor and middle class do not', 'price': '399.00', 'category': 'books'},
            
            # TOYS
            {'title': 'LEGO Classic Building Blocks', 'description': '500-piece building blocks set for creative play and imagination', 'price': '1999.00', 'category': 'toys'},
            {'title': 'Hot Wheels RC Car', 'description': 'High-speed remote control car with rechargeable battery and LED lights', 'price': '2499.00', 'category': 'toys'},
            {'title': 'Ravensburger Puzzle 1000 Pieces', 'description': 'Challenging jigsaw puzzle with beautiful landscape artwork', 'price': '899.00', 'category': 'toys'},
            {'title': 'Monopoly Board Game', 'description': 'Classic family board game for 2-6 players with Indian edition', 'price': '1299.00', 'category': 'toys'},
            {'title': 'Funskool Teddy Bear 50cm', 'description': 'Soft and cuddly teddy bear with adorable design', 'price': '999.00', 'category': 'toys'},
            {'title': 'Crayola Art Supplies Set', 'description': 'Complete art set with crayons, markers, colored pencils, and paper', 'price': '1199.00', 'category': 'toys'},
            
            # FASHION - Jewelry & Accessories
            {'title': 'Gold Plated Pendant Necklace', 'description': 'Elegant gold-plated pendant with chain, perfect for daily wear', 'price': '1299.00', 'category': 'fashion'},
            {'title': 'Silver Heart Pendant', 'description': 'Sterling silver heart pendant with delicate chain', 'price': '899.00', 'category': 'fashion'},
            {'title': 'Diamond Studded Pendant', 'description': 'Beautiful pendant with cubic zirconia stones and gold plating', 'price': '2499.00', 'category': 'fashion'},
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
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully created {created_count} products!'))
        self.stdout.write(self.style.SUCCESS(f'📊 Total products in database: {Product.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'📁 Categories: {Category.objects.count()}'))
