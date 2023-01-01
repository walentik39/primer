#!/usr/bin/env python3

file = open("devices.txt","a")
while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
        print("All Done!")
        break
    file.write(newItem + "\n")
file.close()
