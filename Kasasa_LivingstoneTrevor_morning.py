import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget

class ReceiptPrintingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kasasa's Printing Program")
        self.setGeometry(100, 100, 400, 400)
        
        self.items = []

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        
        item_name_label = QLabel("Item Name:")
        self.item_name_entry = QLineEdit()
        quantity_label = QLabel("Quantity:")
        self.quantity_entry = QLineEdit()
        price_label = QLabel("Price per Item:")
        self.price_entry = QLineEdit()

        input_layout = QVBoxLayout()
        input_layout.addWidget(item_name_label)
        input_layout.addWidget(self.item_name_entry)
        input_layout.addWidget(quantity_label)
        input_layout.addWidget(self.quantity_entry)
        input_layout.addWidget(price_label)
        input_layout.addWidget(self.price_entry)

        
        add_button = QPushButton("Add Item")
        add_button.clicked.connect(self.add_item)
        finish_button = QPushButton("Finish Order")
        finish_button.clicked.connect(self.finish_order)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(finish_button)

        
        self.receipt_label = QLabel("", wordWrap=True)

        
        self.items_listbox = QListWidget()

        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.receipt_label)
        main_layout.addWidget(self.items_listbox)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def print_receipt(self):
        receipt_text = "--------- Receipt ---------\n"
        for item in self.items:
            receipt_text += f"{item['name']}: {item['quantity']} x ${item['price']:.2f} = ${item['price']*item['quantity']:.2f}\n"
        receipt_text += "---------------------------\n"
        receipt_text += f"Total: ${self.calculate_total():.2f}"
        self.receipt_label.setText(receipt_text)

    def add_item(self):
        item_name = self.item_name_entry.text()
        quantity = int(self.quantity_entry.text())
        price = float(self.price_entry.text())

        item = {'name': item_name, 'quantity': quantity, 'price': price}
        self.items.append(item)

        self.item_name_entry.clear()
        self.quantity_entry.clear()
        self.price_entry.clear()

       
        self.items_listbox.addItem(f"{item['name']} ({item['quantity']} x ${item['price']:.2f})")

    def finish_order(self):
        self.print_receipt()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReceiptPrintingApp()
    window.show()
    sys.exit(app.exec_())
