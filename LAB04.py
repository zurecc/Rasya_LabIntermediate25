class inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            print(f"{item} ditambahkan ke inventory")
        else:
            print(f"{item} sudah ada di inventory")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} dihapus dari inventory")
        else:
            print(f"{item} tidak ada di inventory")

    def find_item(self, item):
        return item in self.items

inv = inventory()
inv.add_item("Pedang")
inv.add_item("Pisang")
inv.remove_item("Pedang")

print(inv.items)

print(inv.find_item("Pisang"))
print(inv.find_item("Pedang"))