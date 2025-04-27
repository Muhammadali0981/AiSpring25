class Product:
    def __init__(self, id, frequency, volume):
        self.id = id
        self.frequency = frequency
        self.volume = volume

class Slot:
    def __init__(self, id, distance):
        self.id = id
        self.distance = distance
        self.available_volume = 1  # Assuming each slot has volume 1
        self.products = []

def optimize_warehouse_layout(products, slots):
    # Sort products by frequency (descending) and volume (ascending)
    sorted_products = sorted(products, key=lambda x: (-x.frequency, x.volume))
    
    # Sort slots by distance (ascending)
    sorted_slots = sorted(slots, key=lambda x: x.distance)
    
    # Assign products to slots
    for product in sorted_products:
        assigned = False
        for slot in sorted_slots:
            if slot.available_volume >= product.volume:
                slot.products.append(product)
                slot.available_volume -= product.volume
                assigned = True
                break
        if not assigned:
            print(f"Warning: Product {product.id} could not be assigned due to space constraints")
    
    return sorted_slots

def calculate_total_walking_distance(slots):
    total_distance = 0
    for slot in slots:
        for product in slot.products:
            total_distance += product.frequency * slot.distance
    return total_distance

def print_layout(slots):
    print("\nWarehouse Layout:")
    for slot in slots:
        print(f"\nSlot {slot.id} (Distance: {slot.distance}):")
        for product in slot.products:
            print(f"  Product {product.id} (Frequency: {product.frequency}, Volume: {product.volume})")

# Sample input
products = [
    Product(1, 15, 2),
    Product(2, 8, 1),
    Product(3, 20, 3)
]

slots = [
    Slot(1, 1),
    Slot(2, 2),
    Slot(3, 3)
]

# Optimize layout
optimized_slots = optimize_warehouse_layout(products, slots)

# Print results
print_layout(optimized_slots)
total_distance = calculate_total_walking_distance(optimized_slots)
print(f"\nTotal walking distance: {total_distance}") 