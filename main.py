from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

 
app = FastAPI()
    
class Category(BaseModel):
    CategoryId: int
    CategoryName: str


class Item(BaseModel):
    ItemId: int
    ItemName: str
    ItemCategory: Category
    ItemImage: str
    ItemPrice: float
    ItemAvailability: bool

categories = {
    1: "Computer Accessories",
    2: "Electronics",
    3: "Home Decor"
}

# Define items list with 5 items under each category, each item has image, price, and availability
items = []

# Computer Accessories
items.append({
    "ItemId": 1,
    "ItemName": "Wireless Mouse",
    "ItemImage": "mouse.jpg",
    "ItemPrice": 19.99,
    "ItemAvailability": True,
    "ItemCategory": categories[1]
})
items.append({
    "ItemId": 2,
    "ItemName": "Mechanical Keyboard",
    "ItemImage": "keyboard.jpg",
    "ItemPrice": 49.99,
    "ItemAvailability": True,
    "ItemCategory": categories[1]
})
items.append({
    "ItemId": 3,
    "ItemName": "USB-C Hub",
    "ItemImage": "usbc_hub.jpg",
    "ItemPrice": 29.99,
    "ItemAvailability": False,
    "ItemCategory": categories[1]
})
items.append({
    "ItemId": 4,
    "ItemName": "Webcam",
    "ItemImage": "webcam.jpg",
    "ItemPrice": 39.99,
    "ItemAvailability": True,
    "ItemCategory": categories[1]
})
items.append({
    "ItemId": 5,
    "ItemName": "Laptop Stand",
    "ItemImage": "laptop_stand.jpg",
    "ItemPrice": 24.99,
    "ItemAvailability": True,
    "ItemCategory": categories[1]
})

# Electronics
items.append({
    "ItemId": 6,
    "ItemName": "Bluetooth Speaker",
    "ItemImage": "speaker.jpg",
    "ItemPrice": 59.99,
    "ItemAvailability": True,
    "ItemCategory": categories[2]
})
items.append({
    "ItemId": 7,
    "ItemName": "Smart Watch",
    "ItemImage": "smart_watch.jpg",
    "ItemPrice": 129.99,
    "ItemAvailability": True,
    "ItemCategory": categories[2]
})
items.append({
    "ItemId": 8,
    "ItemName": "Portable Charger",
    "ItemImage": "charger.jpg",
    "ItemPrice": 34.99,
    "ItemAvailability": False,
    "ItemCategory": categories[2]
})
items.append({
    "ItemId": 9,
    "ItemName": "Noise Cancelling Headphones",
    "ItemImage": "headphones.jpg",
    "ItemPrice": 89.99,
    "ItemAvailability": True,
    "ItemCategory": categories[2]
})
items.append({
    "ItemId": 10,
    "ItemName": "Action Camera",
    "ItemImage": "action_camera.jpg",
    "ItemPrice": 199.99,
    "ItemAvailability": True,
    "ItemCategory": categories[2]
})

# Home Decor
items.append({
    "ItemId": 11,
    "ItemName": "LED Table Lamp",
    "ItemImage": "table_lamp.jpg",
    "ItemPrice": 22.99,
    "ItemAvailability": True,
    "ItemCategory": categories[3]
})
items.append({
    "ItemId": 12,
    "ItemName": "Wall Art Painting",
    "ItemImage": "wall_art.jpg",
    "ItemPrice": 45.00,
    "ItemAvailability": True,
    "ItemCategory": categories[3]
})
items.append({
    "ItemId": 13,
    "ItemName": "Decorative Vase",
    "ItemImage": "vase.jpg",
    "ItemPrice": 18.50,
    "ItemAvailability": False,
    "ItemCategory": categories[3]
})
items.append({
    "ItemId": 14,
    "ItemName": "Throw Pillow",
    "ItemImage": "pillow.jpg",
    "ItemPrice": 12.99,
    "ItemAvailability": True,
    "ItemCategory": categories[3]
})
items.append({
    "ItemId": 15,
    "ItemName": "Aroma Diffuser",
    "ItemImage": "diffuser.jpg",
    "ItemPrice": 27.99,
    "ItemAvailability": True,
    "ItemCategory": categories[3]
})


@app.get("/items/")
def get_all_items():
    """
    Returns all items.
    """
    return items

@app.get("/items/category/{category_name}")
def get_items_by_category(category_name: str):
    """
    Returns a list of items belonging to the specified category name.
    """
    return [item for item in items if item["ItemCategory"] == category_name]

   

@app.post("/items/")
def add_item(ItemName: str, ItemImage: str, ItemPrice: float, ItemAvailability: bool, ItemCategory: str):
    # Find the next available ItemId
    next_id = max([i["ItemId"] for i in items], default=0) + 1
    # Validate category
    if ItemCategory not in categories.values():
        raise HTTPException(status_code=400, detail="Invalid category name.")
    new_item = {
        "ItemId": next_id,
        "ItemName": ItemName,
        "ItemImage": ItemImage,
        "ItemPrice": ItemPrice,
        "ItemAvailability": ItemAvailability,
        "ItemCategory": ItemCategory
    }
    items.append(new_item)
    return {"message": "Item added successfully", "item": new_item}

