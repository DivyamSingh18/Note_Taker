print("#################### Welcome to Note_Taker ####################")

print("\n              To write a note, enter keyword 'write' ")
print("              To read a note, enter keyword 'read' ")
print("              To append to a note, enter keyword 'append' ")

cmd = input("\n\nWhat operation do you want to perform: ")

if cmd == "write":
    n = int(input("Enter the number of notes you want to write:"))
    note_taker = open("Your Notes.txt","w")
    for i in range(1, n+1):
        note_inp = input("Enter your Note: ")
        note_taker.write("Note no. ")
        note_taker.write(str(i))
        note_taker.write("=>   ")
        note_taker.write(note_inp+"\n")
        record = open("record_file.txt", "w")
        record.write(str(i))
        record.close()
    print("Your notes have been saved successfully!")
    note_taker.close()

elif cmd == "read":
    note_taker = open("Your Notes.txt", "r")
    print("Your notes are as follows:")
    note_out = note_taker.read()
    print(note_out)
    note_taker.close()

elif cmd == "append":
    note_taker = open("Your Notes.txt", "a")
    m = int(input("Enter the number of notes you want to add:"))
    x =  open("record_file.txt","r")
    record = int(x.read())

    for i in range(record+1, record+1 +m):
        note_apd = input("Enter your Note: ")
        note_taker.write("Note no. ")
        note_taker.write(str(i))
        note_taker.write("=>   ")
        note_taker.write(note_apd+"\n")
    print("Your notes have been added successfully!")
    note_taker.close()

else:
    print("// Invalid Command //")


