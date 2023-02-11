import numpy as np
import pandas as pd
from datetime import datetime
from tabulate import tabulate
from dataclasses import dataclass
import os


class Transaction:
    item: str
    price: int
    qty: int
    list_item = []

    def __init__(self):
        #         self.item = item
        #         self.price = price
        #         self.qty = qty
        #         trx = [self.item, self.price, self.qty]
        #         self.list_item = [trx]
        self.list_item = []

    def add_item(self, item, price, qty):
        """ Add item data into list transaction.
            Args:
                item: item name:str
                price: item price per pieces:int
                qty : number of item to buy:int
        """
        self.list_item.append([item, price, qty])

    def update_item_name(self, prev_name, new_name):
        """ Change item name from previous name to new name, if previous name exist in list transaction.
            Args:
                prev_name: previous name of item will changed:str
                new_name: new name of item:str
        """
        for i in range(0, len(self.list_item)):
            if self.list_item[i][0] == prev_name:
                self.list_item[i][0] = new_name

    def update_item_price(self, name, new_price):
        """ Change item price into new price, if item name exist in list transaction.
            Args:
                name: item name:str
                new_price: new item price per pieces:int
        """
        for i in range(0, len(self.list_item)):
            if self.list_item[i][0] == name:
                self.list_item[i][1] = new_price

    def update_item_qty(self, name, new_qty):
        """ Change item price into new price, if item name exist in list transaction.
            Args:
                name: item name:str
                new_price: new item price per pieces:int
        """
        for i in range(0, len(self.list_item)):
            if self.list_item[i][0] == name:
                self.list_item[i][2] = new_qty

    def delete_item(self, name):
        """ Delete item from list transaction, if item name exist in list transaction.
            Args:
                name: item name:str
        """
        for i in range(0, len(self.list_item)):
            if self.list_item[i][0] == name:
                del self.list_item[i]

    def reset_transaction(self):
        """ Delete all item from list transaction.
        """
        self.list_item = [[]]

    def check_order(self):
        """ Print all item from list transaction.
        """
        print(tabulate(self.list_item, headers=['nama barang', 'harga', 'jumlah barang']))

    def total_price(self):
        """ Calculate total amount (price) that user must pay.
            return:
                total_price:int
        """
        total_price = 0
        diskon_str = 'Tidak Mendapat Diskon'
        for i in range(0, len(self.list_item)):
            total_price = total_price + (self.list_item[i][1] * self.list_item[i][2])
        if total_price > 500000:
            total_price = total_price *0.9
            diskon_str = "Mendapat diskon 10%"
        elif total_price > 300000:
            total_price = total_price * 0.92
            diskon_str = "Mendapat diskon 8%"
        elif total_price > 200000:
            total_price = total_price * 0.95
            diskon_str = "Mendapat diskon 5%"

        print(f"{diskon_str}. Sehingga Total Belanja: Rp{total_price:,}")


def print_menu():
    print("**Menu Utama Toko Jaya Baru -Self Service**")
    print("1 : Menambahkan Item")
    print("2 : Update Nama Item")
    print("3 : Update Harga Item")
    print("4 : Update Jumlah Item")
    print("5 : Hapus Item Berdasarkan Nama Item")
    print("6 : Hapus Seluruh Item")
    print("7 : Total Harga")
    print("Q : Keluar Kasir")

def delay_press():
    input("Tekan Enter untuk melanjutkan...")

print("**Selamat Datang di Toko Jaya Baru*")
run_app = True
menu_key = ["1", "2", "3", "4", "5", "6", "7", "Q"]

while (run_app):
    try:
        os.system("cls")
        menu = input("Pilih menu {Q:Keluar, Y:Melakukan Transaksi}? ")
        if menu.upper() == 'Y':
            start_transaction = True
            trans = Transaction()
            while start_transaction:
                os.system("cls")
                print_menu()
                print("\n--- Detail Pesanan ---")
                trans.check_order()
                action = input("\nInput Angka/Huruf sesuai menu yang ingin dilakukan: ")
                if action.upper() == "Q":
                    start_transaction = False
                elif action.upper() not in menu_key:
                    print("menu tidak tersedia!")
                elif len(trans.list_item) == 0 and action != "1":
                    print("Menu belum tersedia karena barang di transaksi masih kosong. Input terlebih dahulu barang "
                          "menggunakan Menu 1")
                else:
                    if action == "1":
                        print("--- 1 : Menambahkan Item ---")
                        name, price, qty = (input(
                            "Input nama barang, harga, dan jumlah barang. Pisahkan dengan koma (cth: Kamper,11000,1) : ")).split(
                            ',')
                        price = int(price)
                        qty = int(qty)
                        trans.add_item(name, price, qty)
                    elif action == "2":
                        print("--- 2 : Update Nama Item ---")
                        name, new_name = (input(
                            "Input nama barang lama dan nama barang baru. Pisahkan dengan koma cth: Kamper,Kapur Barus")).split(
                            ',')
                        trans.update_item_name(name, new_name)
                    elif action == "3":
                        print("--- 3 : Update Harga Item ---")
                        name, new_price = (
                            input("Input nama barang, harga baru. Pisahkan dengan koma cth: Kamper,12000")).split(',')
                        new_price = int(new_price)
                        trans.update_item_price(name, new_price)
                    elif action == "4":
                        print("--- 4 : Update Jumlah Item ---")
                        name, qty = (
                            input("Input nama barang, jumlah barang terbaru. Pisahkan dengan koma cth: Kamper,4")).split(
                            ',')
                        qty = int(qty)
                        trans.update_item_qty(name, qty)
                    elif action == "5":
                        print("--- 5 : Hapus Item Berdasarkan Nama Item ---")
                        name = (input("Input satu nama barang yang akan dihapus.")).split(',')
                        trans.delete_item(name)
                    elif action == "6":
                        print("Seluruh Item telah dihapus dari transaksi.")
                        trans.reset_transaction()
                    elif action == "7":
                        print("--- 7 : Total Harga ---")
                        trans.total_price()
                delay_press()
        elif menu.upper() == 'Q':
            print("Sampai Jumpa Lagi! Semoga senang dengan Pelayanan Kami.")
            run_app = False
        else:
            print("Menu yang kamu input tidak ada pada sistem, silahkan pilih menu yang sesuai!")
    except ValueError:
        print("Data yang kamu input tidak sesuai dengan format yang ada")

    except IndexError:
        print("Nama Item/Perintah yang kamu cari tidak tersedia")
