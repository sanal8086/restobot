import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from firebase_client import get_db

def migrate_menu():
    db_ref = get_db()
    restaurants = db_ref.child('restaurants').get()
    if not restaurants:
        print("No restaurants found.")
        return
    res_id = list(restaurants.keys())[0]
    print(f"Migrating menu for restaurant ID: {res_id}")

    # 1. Clear existing data
    db_ref.child(f'restaurants/{res_id}/main_categories').delete()
    db_ref.child(f'restaurants/{res_id}/categories').delete()
    db_ref.child(f'restaurants/{res_id}/items').delete()

    main_cats_ref = db_ref.child(f'restaurants/{res_id}/main_categories')
    cats_ref = db_ref.child(f'restaurants/{res_id}/categories')
    items_ref = db_ref.child(f'restaurants/{res_id}/items')

    def add_item(name, desc, price, main_id, cat_id, image_url, veg=True):
        items_ref.push({
            'name': name,
            'description': desc,
            'price': price,
            'image_url': image_url,
            'main_category_id': main_id,
            'category_id': cat_id,
            'item_type': 'veg' if veg else 'non-veg',
            'taste': 'spicy',
            'spice_level': 3,
            'heaviness': 'medium',
            'is_enabled': True
        })

    # Image URLs
    IMG_STARTER = "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=400&q=80"
    IMG_CURRY = "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400&q=80"
    IMG_NAAN = "https://images.unsplash.com/photo-1626200419188-f1a16b4a37a6?w=400&q=80"
    IMG_BIRYANI = "https://images.unsplash.com/photo-1563379091339-03b21bc4a4f8?w=400&q=80"
    IMG_CHINESE = "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=400&q=80"
    IMG_ARABIC = "https://images.unsplash.com/photo-1541518763669-27fef04b14ea?w=400&q=80"
    IMG_DESSERT = "https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?w=400&q=80"
    IMG_BEV = "https://images.unsplash.com/photo-1544787210-2213d84ad96b?w=400&q=80"
    IMG_PIZZA = "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&q=80"
    IMG_PASTA = "https://images.unsplash.com/photo-1473093226795-af9932fe5856?w=400&q=80"

    # --- MAIN CATEGORIES ---
    m_indian = main_cats_ref.push({'name': 'Indian', 'display_order': 1}).key
    m_chinese = main_cats_ref.push({'name': 'Chinese', 'display_order': 2}).key
    m_arabic = main_cats_ref.push({'name': 'Arabic', 'display_order': 3}).key
    m_continental = main_cats_ref.push({'name': 'Continental', 'display_order': 4}).key

    # --- 1. INDIAN ---
    # 1.1 Starters / Appetizers
    c_ind_v_star = cats_ref.push({'name': 'Vegetarian Starters', 'display_order': 1, 'main_category_id': m_indian, 'course_type': 'Starters / Appetizers'}).key
    c_ind_nv_star = cats_ref.push({'name': 'Non-Vegetarian Starters', 'display_order': 2, 'main_category_id': m_indian, 'course_type': 'Starters / Appetizers'}).key
    add_item('Paneer Tikka', 'Grilled cottage cheese', 220, m_indian, c_ind_v_star, IMG_STARTER)
    add_item('Chicken Tikka', 'Spicy grilled chicken', 280, m_indian, c_ind_nv_star, IMG_STARTER, False)

    # 1.2 Main Course -> North Indian
    c_ind_ni_bread = cats_ref.push({'name': 'Breads', 'display_order': 3, 'main_category_id': m_indian, 'course_type': 'Main Course - North Indian'}).key
    c_ind_ni_cv = cats_ref.push({'name': 'Curries (Veg)', 'display_order': 5, 'main_category_id': m_indian, 'course_type': 'Main Course - North Indian'}).key
    add_item('Butter Naan', 'Soft Indian bread', 40, m_indian, c_ind_ni_bread, IMG_NAAN)
    add_item('Dal Makhani', 'Slow cooked lentils', 200, m_indian, c_ind_ni_cv, IMG_CURRY)

    # 1.2 Main Course -> South Indian
    c_ind_si_tiffin = cats_ref.push({'name': 'Breakfast', 'display_order': 7, 'main_category_id': m_indian, 'course_type': 'Main Course - South Indian'}).key
    add_item('Masala Dosa', 'South Indian crepe', 120, m_indian, c_ind_si_tiffin, "https://images.unsplash.com/photo-1630383249896-424e482df921?w=400&q=80")

    # 1.3 Biryani & Rice Specials
    c_ind_biryani = cats_ref.push({'name': 'Chicken Biryani', 'display_order': 17, 'main_category_id': m_indian, 'course_type': 'Biryani & Rice Specials'}).key
    add_item('Chicken Biryani', 'Aromatic rice', 320, m_indian, c_ind_biryani, IMG_BIRYANI, False)

    # --- 2. CHINESE ---
    c_chi_noodle = cats_ref.push({'name': 'Noodles', 'display_order': 1, 'main_category_id': m_chinese, 'course_type': 'Main Course'}).key
    add_item('Hakka Noodles', 'Stir fried noodles', 180, m_chinese, c_chi_noodle, IMG_CHINESE)

    # --- ARABIC ---
    c_ara_mandi = cats_ref.push({'name': 'Rice & Mandi', 'display_order': 1, 'main_category_id': m_arabic, 'course_type': 'Main Course'}).key
    add_item('Chicken Mandi', 'Traditional rice', 380, m_arabic, c_ara_mandi, IMG_ARABIC, False)

    # --- CONTINENTAL ---
    c_con_pasta = cats_ref.push({'name': 'Pasta', 'display_order': 1, 'main_category_id': m_continental, 'course_type': 'Main Course'}).key
    add_item('Pasta Alfredo', 'White sauce pasta', 250, m_continental, c_con_pasta, IMG_PASTA)

    # --- DESSERTS ---
    m_dessert_cat = cats_ref.push({'name': 'Ice Creams', 'display_order': 1, 'main_category_id': m_indian, 'course_type': 'Desserts'}).key
    add_item('Vanilla Scoop', 'Classic ice cream', 70, m_indian, m_dessert_cat, IMG_DESSERT)

    # --- BEVERAGES ---
    m_bev_cat = cats_ref.push({'name': 'Cold', 'display_order': 1, 'main_category_id': m_indian, 'course_type': 'Beverages'}).key
    add_item('Cold Coffee', 'With ice cream', 120, m_indian, m_bev_cat, IMG_BEV)

    print("SUCCESS: Menu structure migrated with diverse images!")

if __name__ == '__main__':
    migrate_menu()
