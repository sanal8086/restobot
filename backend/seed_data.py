import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from firebase_client import get_db

def seed_data():
    db_ref = get_db()
    restaurants = db_ref.child('restaurants').get()
    if not restaurants:
        print("No restaurants found.")
        return
    res_id = list(restaurants.keys())[0]
    print(f"Re-seeding for restaurant ID: {res_id}")

    db_ref.child(f'restaurants/{res_id}/main_categories').delete()
    db_ref.child(f'restaurants/{res_id}/categories').delete()
    db_ref.child(f'restaurants/{res_id}/items').delete()

    # Main Categories
    main_cats_ref = db_ref.child(f'restaurants/{res_id}/main_categories')
    indian_main = main_cats_ref.push({'name': 'Indian', 'display_order': 1})
    chinese_main = main_cats_ref.push({'name': 'Chinese', 'display_order': 2})

    # Sub Categories with course_type
    cats_ref = db_ref.child(f'restaurants/{res_id}/categories')

    # Indian sub-categories
    ind_starter = cats_ref.push({'name': 'Starters', 'display_order': 1, 'main_category_id': indian_main.key, 'course_type': 'starter'})
    ind_curry   = cats_ref.push({'name': 'Curries',  'display_order': 2, 'main_category_id': indian_main.key, 'course_type': 'main'})
    ind_bread   = cats_ref.push({'name': 'Breads',   'display_order': 3, 'main_category_id': indian_main.key, 'course_type': 'bread'})
    ind_rice    = cats_ref.push({'name': 'Rice',     'display_order': 4, 'main_category_id': indian_main.key, 'course_type': 'rice'})
    ind_dessert = cats_ref.push({'name': 'Desserts', 'display_order': 5, 'main_category_id': indian_main.key, 'course_type': 'dessert'})

    # Chinese sub-categories
    chi_starter = cats_ref.push({'name': 'Appetizers', 'display_order': 1, 'main_category_id': chinese_main.key, 'course_type': 'starter'})
    chi_main    = cats_ref.push({'name': 'Noodles',    'display_order': 2, 'main_category_id': chinese_main.key, 'course_type': 'main'})
    chi_rice    = cats_ref.push({'name': 'Fried Rice', 'display_order': 3, 'main_category_id': chinese_main.key, 'course_type': 'rice'})
    chi_dessert = cats_ref.push({'name': 'Desserts',   'display_order': 4, 'main_category_id': chinese_main.key, 'course_type': 'dessert'})

    # Items
    items_ref = db_ref.child(f'restaurants/{res_id}/items')

    # Indian Starters
    items_ref.push({'name': 'Paneer Tikka', 'description': 'Grilled cottage cheese in spicy marinade', 'price': 220, 'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_starter.key, 'item_type': 'veg', 'taste': 'spicy', 'spice_level': 3, 'heaviness': 'light', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Chicken Tikka', 'description': 'Tandoor grilled chicken, mint chutney', 'price': 280, 'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b6ae398?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_starter.key, 'item_type': 'non-veg', 'taste': 'spicy', 'spice_level': 3, 'heaviness': 'light', 'is_enabled': True})

    # Indian Curries (Main)
    items_ref.push({'name': 'Butter Chicken', 'description': 'Tender chicken in rich creamy tomato gravy', 'price': 350, 'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b6ae398?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_curry.key, 'item_type': 'non-veg', 'taste': 'creamy', 'spice_level': 2, 'heaviness': 'heavy', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Paneer Butter Masala', 'description': 'Cottage cheese in rich tomato cashew gravy', 'price': 280, 'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_curry.key, 'item_type': 'veg', 'taste': 'creamy', 'spice_level': 2, 'heaviness': 'heavy', 'is_enabled': True})
    items_ref.push({'name': 'Dal Makhani', 'description': 'Slow cooked black lentils, butter cream', 'price': 240, 'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_curry.key, 'item_type': 'veg', 'taste': 'creamy', 'spice_level': 1, 'heaviness': 'heavy', 'is_enabled': True})

    # Indian Bread
    items_ref.push({'name': 'Butter Naan', 'description': 'Soft tandoor naan with melted butter', 'price': 50, 'image_url': 'https://images.unsplash.com/photo-1626200419188-f1a16b4a37a6?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_bread.key, 'item_type': 'veg', 'taste': 'salty', 'spice_level': 1, 'heaviness': 'medium', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Garlic Naan', 'description': 'Naan topped with garlic and fresh coriander', 'price': 60, 'image_url': 'https://images.unsplash.com/photo-1626200419188-f1a16b4a37a6?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_bread.key, 'item_type': 'veg', 'taste': 'salty', 'spice_level': 1, 'heaviness': 'medium', 'is_enabled': True})
    items_ref.push({'name': 'Laccha Paratha', 'description': 'Multi-layered crispy whole wheat flatbread', 'price': 55, 'image_url': 'https://images.unsplash.com/photo-1626200419188-f1a16b4a37a6?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_bread.key, 'item_type': 'veg', 'taste': 'salty', 'spice_level': 1, 'heaviness': 'medium', 'is_enabled': True})

    # Indian Rice
    items_ref.push({'name': 'Chicken Biryani', 'description': 'Dum-cooked spiced basmati rice with tender chicken', 'price': 320, 'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_rice.key, 'item_type': 'non-veg', 'taste': 'spicy', 'spice_level': 3, 'heaviness': 'heavy', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Veg Biryani', 'description': 'Aromatic basmati with seasonal vegetables', 'price': 240, 'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_rice.key, 'item_type': 'veg', 'taste': 'spicy', 'spice_level': 2, 'heaviness': 'heavy', 'is_enabled': True})
    items_ref.push({'name': 'Jeera Rice', 'description': 'Cumin tempered basmati rice', 'price': 120, 'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_rice.key, 'item_type': 'veg', 'taste': 'salty', 'spice_level': 1, 'heaviness': 'medium', 'is_enabled': True})

    # Indian Desserts
    items_ref.push({'name': 'Gulab Jamun', 'description': 'Soft milk dumplings soaked in rose syrup', 'price': 90, 'image_url': 'https://images.unsplash.com/photo-1593701460337-1284de3dfbb2?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_dessert.key, 'item_type': 'veg', 'taste': 'sweet', 'spice_level': 1, 'heaviness': 'light', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Kheer', 'description': 'Creamy rice pudding with cardamom and saffron', 'price': 80, 'image_url': 'https://images.unsplash.com/photo-1593701460337-1284de3dfbb2?auto=format&fit=crop&w=300&q=80', 'main_category_id': indian_main.key, 'category_id': ind_dessert.key, 'item_type': 'veg', 'taste': 'sweet', 'spice_level': 1, 'heaviness': 'light', 'is_enabled': True})

    # Chinese Starters
    items_ref.push({'name': 'Chilli Paneer Dry', 'description': 'Crispy paneer tossed with peppers and soy sauce', 'price': 200, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_starter.key, 'item_type': 'veg', 'taste': 'spicy', 'spice_level': 4, 'heaviness': 'light', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Chicken Lollipop', 'description': 'Crispy drumlets with hot garlic sauce', 'price': 260, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_starter.key, 'item_type': 'non-veg', 'taste': 'spicy', 'spice_level': 4, 'heaviness': 'light', 'is_enabled': True})
    items_ref.push({'name': 'Veg Spring Rolls', 'description': 'Crispy rolls with sweet chilli dipping sauce', 'price': 160, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_starter.key, 'item_type': 'veg', 'taste': 'spicy', 'spice_level': 2, 'heaviness': 'light', 'is_enabled': True})

    # Chinese Noodles (Main)
    items_ref.push({'name': 'Veg Hakka Noodles', 'description': 'Wok tossed noodles with crunchy vegetables', 'price': 220, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_main.key, 'item_type': 'veg', 'taste': 'spicy', 'spice_level': 2, 'heaviness': 'medium', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Chicken Noodles', 'description': 'Wok-fried egg noodles with juicy chicken pieces', 'price': 280, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_main.key, 'item_type': 'non-veg', 'taste': 'spicy', 'spice_level': 3, 'heaviness': 'medium', 'is_enabled': True})

    # Chinese Fried Rice
    items_ref.push({'name': 'Veg Fried Rice', 'description': 'Classic wok rice with seasonal greens and soy', 'price': 200, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_rice.key, 'item_type': 'veg', 'taste': 'salty', 'spice_level': 1, 'heaviness': 'medium', 'is_enabled': True, 'is_bestseller': True})
    items_ref.push({'name': 'Chicken Fried Rice', 'description': 'Egg, spring onion, soy and wok char', 'price': 260, 'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_rice.key, 'item_type': 'non-veg', 'taste': 'salty', 'spice_level': 2, 'heaviness': 'medium', 'is_enabled': True})

    # Chinese Desserts
    items_ref.push({'name': 'Mango Sorbet', 'description': 'Fresh Alphonso mango, tangy and sweet', 'price': 100, 'image_url': 'https://images.unsplash.com/photo-1593701460337-1284de3dfbb2?auto=format&fit=crop&w=300&q=80', 'main_category_id': chinese_main.key, 'category_id': chi_dessert.key, 'item_type': 'veg', 'taste': 'sweet', 'spice_level': 1, 'heaviness': 'light', 'is_enabled': True})

    print("SUCCESS: Full multi-course seed data created!")

if __name__ == '__main__':
    seed_data()
