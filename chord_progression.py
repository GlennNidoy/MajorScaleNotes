selecting = True
while selecting:
    chords = ["Ab", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G"]
    new_chords = [chord for chord in chords]
    major_scale_progression = [2, 2, 1, 2, 2, 2, 1]

    for item in chords:
        new_chords.append(item)

    selected_chord = ''
    while selected_chord not in new_chords:
        selected_chord = input("Please enter your chord to check the chords in Major Scale [press q to quit]: ").capitalize()
        if selected_chord.lower() == 'q':
            selecting = False
            break

    index = new_chords.index(selected_chord)
    collect_all_index = [index]
    print("MAJOR SCALE")
    print(f"Key of {selected_chord}")

    for counter in major_scale_progression:
        index += counter
        collect_all_index.append(index)

    for i in collect_all_index:
        print(f"{new_chords[i]}",end="  ")

    print("")
    selecting = input("Try again? [y or n]: ").lower()
    if selecting == 'y':
        continue
    else:
        selecting = False

