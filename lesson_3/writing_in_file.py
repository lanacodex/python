#examples of writings of file

file = open("my_first_file.txt", "w", encoding="utf-8")
file.write("my_first_file čžš")
file.close()

#new way
with open("my_second_file.txt", 'w', encoding="utf-8") as file:

# način čitanja - novi / new way of reading
with open("my_first-file.txt", encoding="utf-8") as file_read:
    procitana_vrijednost = file_read-read()
    print("Pročitao sam" + procitana_vrijednost)
