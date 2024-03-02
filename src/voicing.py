#make a class of voicing
from midiutil import MIDIFile
import tqdm as tqdm
import random

class Voicing:
    #define the class
    def __init__(self):
        #define the natures of the chords
        self.natures = {'maj', 'maj6', 'maj7', 'm', 'm6', 'm7', 'm_maj7', 'dom7', 'sus', 'sus2', 'sus7', 'sus4', 'o7', 'o', 'ø7', 'power', 'aug', 'o_maj7', 'N.C.'}
        
        #alterations and add
        self.alter = {'add b2', 'add 2', 'add b5', 'add 5', 'add #5', 'add b6', 'add 6' 'add 7', 'add #7', 'add 8', 'add b9', 'add 9', 'add #9', 'add #11', 'add 13', 'add b13', 'alter #11', 'alter #5', 'alter #7', 'alter #9', 'alter b5', 'alter b9'}        
        
        #Structural elements
        self.structural_elements = {'.', '|', '||', ':|', '|:', 'b||', 'e||', '/'} #to add the maj token 
        
        #element in the chord frontiers
        self.after_chords = {'.', '|', '||', ':|', '|:', 'b||', 'e||'} 
        
        #Voicing
        self.voicing = ['v_0', 'v_1', 'v_2', 'v_3']
        
        #All notes
        self.all_notes = {
            'C': 48, 'C#': 49, 'Db': 49, 'D': 50, 'D#': 51, 'Eb': 51, 'E': 52, 'Fb': 52, 'F': 53, 'E#': 53, 'F#': 54, 'Gb': 42, 'G': 43, 'G#': 44, 'Ab':44, 'A': 45, 'A#': 46, 'Bb': 46, 'B': 47, 
            'A##': 47, 'Abb': 43, 'Abbb': 42, 'B#': 48, 'B##': 49, 'Bbb': 45, 'Bbbb': 44,
            'C##': 50, 'C###': 51, 'Cb': 47, 'Cbb': 46, 'D##': 52, 'Dbb': 48, 'Dbbb': 47, 'E##': 54, 'Ebb': 50, 'Ebbb': 49, 
            'F##': 55, 'F###': 56, 'Fbb': 51, 'G##': 45, 'Gbb': 41
            }
        
        #define voicing for natures for piano
        self.maj = {'v_0':[0, 7, 12, 16], 'v_1':[0, 7, 16, 19], 'v_2':[0, 12, 16, 19], 'v_3':[0, 7, 12, 16]}
        self.m6 = {'v_0':[0, 7, 9, 16], 'v_1':[0, 9, 16, 19], 'v_2':[0, 9, 12, 16], 'v_3':[0, 9, 12, 16, 19]}
        self.maj7 = {'v_0':[0, 11, 14, 16, 19], 'v_1':[0, 11, 16, 19], 'v_2':[0, 11, 14, 16], 'v_3':[0, 11, 14, 16, 19]}
        self.maj6 = {'v_0':[0, 7, 9, 12, 16], 'v_1':[0, 7, 9, 16], 'v_2':[0, 7, 14, 16, 21], 'v_3':[0, 4, 7, 9, 12, 14]}
        self.power = {'v_0':[0, 7, 12, 19], 'v_1':[0, 7, 12, 19], 'v_2':[0, 7, 12, 24], 'v_3':[0, 7, 12, 24]}
        self.m = {'v_0':[0, 12, 15, 19], 'v_1':[0, 7, 12, 15], 'v_2':[0, 7, 12, 15, 19], 'v_3':[0, 7, 14, 15, 19]}
        self.m7 = {'v_0':[0, 10, 15, 19], 'v_1':[0, 7, 10, 15], 'v_2':[0, 10, 14, 15], 'v_3':[0, 10, 14, 15]}
        self.m_maj7 = {'v_0':[0, 11, 15, 19], 'v_1':[0, 7, 11, 12, 15], 'v_2':[0, 7, 11, 14, 15], 'v_3':[0, 11, 15, 19]}
        self.dom7 = {'v_0':[0, 10, 14, 16, 19], 'v_1':[0, 10, 16, 19], 'v_2':[0, 10, 14, 16], 'v_3':[0, 10, 14, 16, 19]}
        self.ø7 =  {'v_0':[0, 15, 18, 22], 'v_1':[0, 10, 15, 18], 'v_2':[0, 12, 15, 18, 22], 'v_3':[0, 6, 10, 15, 18]}
        self.o7 = {'v_0':[0, 6, 10, 14, 15], 'v_1':[0, 15, 18, 21, 24], 'v_2':[0, 15, 18, 21, 24], 'v_3':[0, 12, 15, 18, 21]}
        self.o = {'v_0':[0, 3, 6, 12], 'v_1':[0, 6, 12, 15], 'v_2':[0, 15, 18, 21], 'v_3':[0, 12, 15, 18, 21]}
        self.sus = {'v_0':[0, 12, 17, 19], 'v_1':[0, 17, 19, 24], 'v_2':[0, 10, 14, 17], 'v_3':[0, 7, 14, 17, 19]} 
        self.sus7 = {'v_0':[0, 10, 17, 19], 'v_1':[0, 10, 14, 17, 19], 'v_2':[0, 10, 14, 17], 'v_3':[0, 10, 14, 17, 19]}
        self.sus2 = {'v_0':[0, 10, 17, 19], 'v_1':[0, 10, 14, 17, 19], 'v_2':[0, 10, 14, 17], 'v_3':[0, 10, 14, 17, 19]}
        self.sus4 = {'v_0':[0, 5, 7, 12, 14], 'v_1':[0, 7, 14, 17], 'v_2':[0, 7, 12, 17, 19], 'v_3':[0, 14, 12, 17, 10]}
        self.aug = {'v_0':[0, 4, 8, 12, 16], 'v_1':[0, 8, 12, 16, 20], 'v_2':[0, 12, 16, 20, 24], 'v_3':[0, 8, 12, 16]}
        self.o_maj7 = {'v_0':[0, 11, 15, 18], 'v_1':[0, 6, 11, 15], 'v_2':[0, 6, 11, 15, 18], 'v_3':[0, 11, 12, 15, 18]}
        self.noChord = {'v_0':[0, 0, 0, 0], 'v_1':[0, 0, 0, 0], 'v_2':[0, 0, 0, 0], 'v_3':[0, 0, 0, 0]}
               
        #TODO: define voicing for guitar
        
        #Define the voicing dictionaries for the chords
        self.chord_voicing = {'maj': self.maj, 'maj7': self.maj7, 'm': self.m, 'm7': self.m7, 'dom7': self.dom7, 
                              'ø7': self.ø7, 'o7': self.o7, 'o': self.o, 'sus': self.sus, 'sus7': self.sus7, 
                              'sus2': self.sus2, 'sus4': self.sus4, 'm6': self.m6, 'power': self.power, 'o': self.o, 
                              'm_maj7': self.m_maj7, 'maj6': self.maj6, 'aug': self.aug, 'o_maj7': self.o_maj7, 'N.C.': self.noChord}
    
    #-----------------------------------------------------------------------
    def getStructuralElements(self):
        return self.structural_elements
    
    #-----------------------------------------------------------------------
    # Add the maj token
    def add_maj_token(self, sequence):
        new_sequence = []
        for song in sequence:
            new_song = []
            for i in range(len(song)):
                element = song[i]
                new_song.append(element)
                if element in self.all_notes.keys() and (i == len(song) - 1 or song[i + 1] in self.structural_elements 
                                                         or song[i + 1].startswith('Form_')) and song[i-1] != '/':
                    new_song.append('maj')
            new_sequence.append(new_song)
        
        return new_sequence
    
    #-----------------------------------------------------------------------
    # Add the voicing to the sequence
    def convert_chords_to_voicing(self, sequence):
        midi_sequence = []
        root = 0
        mod = 4
        status = True
        # Create a dictionary for the alter section
        add_dict = {
            'add b13': 8 + 12,
            'add 13': 9 + 12, 
            'add #11': 6 + 12,
            'add #9': 3 + 12,
            'add 9': 2 + 12,
            'add b9': 1 + 12,
            'add 8': 12,
            'add 7': 11,
            'add #7': 11,
            'add 6': 9,
            'add b6': 8 + 12,
            'add 5': 7,
            'add b5': 6,
            'add 2': 2 + 12,
            'add b2': 1
        }
        # Create a dictionary for the alter section
        alter_dict = {
            'alter b9': 2,
            'alter #9': 2,
            'alter b5': 7,
            'alter #5': 7,
            'alter #7': 11,
            'alter #11': 5
        }
        
        midi = [0, 0, 0, 0, 0, 0, 0, 0]
        #check the chord info
        for i, item in enumerate(sequence):
            element = item[0]
            duration = item[1]
            
            #check notes
            if element in self.all_notes and sequence[i-1][0] != '/':
                root = self.all_notes[element]
                midi = [root, 0, 0, 0, 0, 0, 0, 0]
                couple = (midi, duration, element)
                midi_sequence.append(couple)
                #print(element, sequence[i-1][0]) 
            
            # Nature section --------------------------------------------------------
            elif element in self.natures:
                n = i % mod
                midi = [x + root for x in self.chord_voicing[element][self.voicing[n]]]
                #print('chord:', element, midi)
                infoMidi = midi.copy()
                couple = (infoMidi, duration, element)
                midi_sequence.append(couple)
            
            # Slash section --------------------------------------------------------    
            elif element == '/':
                midi_for_slash = [0, 0, 0, 0, 0, 0, 0, 127]
                couple = (midi_for_slash, duration, element)
                midi_sequence.append(couple)
                
            # New root after slash section -----------------------------------------  
            elif sequence[i-1][0] == '/' and element in self.all_notes:
                midiInfo = midi.copy()
                slash_root = self.all_notes[element]
                midiInfo[0] = midiInfo[0] + 12
                midiInfo.insert(0, slash_root)
                couple = (midiInfo, duration, element)
                midi_sequence.append(couple)
            
            # Add section --------------------------------------------------------      
            elif element in add_dict:
                #print('original', midi)
                new_note = root + add_dict[element]
                midiInfo = midi.copy()    
                if new_note not in midiInfo:
                    midiInfo.append(new_note)
                      
                if element == 'add b9' or element == 'add #9':
                    #check if the 9 is in the chord
                    if (root + 14) in midiInfo:
                        index = midiInfo.index(root + 14)
                        midiInfo.pop(index)
                    elif (root + 26) in midiInfo:
                        index = midiInfo.index(root + 26)
                        midiInfo.pop(index)
                        
                couple = (midiInfo, duration, element)
                midi_sequence.append(couple)
                
            # Alter section --------------------------------------------------------            
            elif element in alter_dict:
                #print('original', element, midi)
                my_ref = [x for x in midi if (x - root) % 12 == alter_dict[element]]
                
                if len(my_ref) == 1:
                    loc = midi.index(my_ref[0])
                    if element.find('b') != -1:
                        midi[loc] = my_ref[0] - 1
                    elif element.find('#') != -1:
                        midi[loc] = my_ref[0] + 1
                        
                elif len(my_ref) > 1:
                    for i, n in enumerate(my_ref):
                        loc = midi.index(n)
                        if element.find('b') != -1 and (n - root) % 12 == alter_dict[element]:
                            midi[loc] = n - 1
                        elif element.find('#') != -1 and (n - root) % 12 == alter_dict[element]:
                            midi[loc] = n + 1 
                
                elif len(my_ref) == 0:
                    new_note = root + alter_dict[element]
                    if element.find('b') != -1:
                        new_note -= 1
                    elif element.find('#') != -1:
                        new_note += 1
                    midi.append(new_note)
                
                midiInfo = midi.copy()     
                couple = (midiInfo, duration, element)
                midi_sequence.append(couple)
                #print('result', element, midi)
            
            # Structural elements section ---------------------------------------------
            elif element in self.structural_elements and element != '/':
                midi = [0, 0, 0, 0, 0, 0, 0, 0]
                couple = (midi, duration, element)
                midi_sequence.append(couple)
                
            # Form section -------------------------------------------------------------
            elif element not in self.all_notes and element not in self.natures and element not in self.structural_elements:
                midi = [0, 0, 0, 0, 0, 0, 0, 0]
                couple = (midi, duration, element)
                midi_sequence.append(couple)
        
            #Normalize the length of the MIDI sequence to 8 ----------------------------
            current_midi = midi_sequence[-1][0]
            if len(current_midi) < 8:
                for i in range(8 - len(current_midi)):
                    current_midi.append(0)
                midi_sequence[-1] = (current_midi, duration, element)
              
        return midi_sequence, status
    
    
    #--------------------------------------------------------------------------------
    #Export the file to MIDI
    def export_to_midi(self, sequence, filename, path = "/workspace/data/midi_files/"):
        #Capture the information
        midi_capture = []
        
        for i, element in enumerate(sequence):
            chord = element[2]
            #print('chord:', chord)
            if chord == '.':
                ref = i+1 
                counter = 0
                doIt = True
                next = sequence[ref][2]  
                while doIt:
                    next = sequence[ref][2]    
                    ref += 1
                    counter += 1
                    if next in self.after_chords or next.startswith('Form_') or ref == len(sequence)-1:
                        doIt = False
                        counter -= 1
                    
                #print(counter)
                
                if counter > 0:
                    midi = (sequence[i+counter][0], sequence[i+counter][1])
                    if midi[0] == [0, 0, 0, 0, 0, 0, 0, 0]:
                        assert False, 'Error: Empty MIDI, ce pa cool Raul'
                    if midi[0] == [48, 48, 48, 48, 0, 0, 0, 0]: #this is No Chord!
                        midi = ([0, 0, 0, 0, 0, 0, 0, 0], sequence[i+counter][1])
                    #print('\nmidi:', midi)
                    midi_capture.append(midi)
                    
        # Create a MIDI file
        track    = 0
        channel  = 0
        time     = 0    # In beats
        tempo    = 200   # In BPM
        volume   = 80  # 0-127, as per the MIDI standard

        MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
        MyMIDI.addTempo(track, time, tempo)

        time = 0
        
        for item in midi_capture:
            m = item[0]
            d = item[1]
  
            for i, pitch in enumerate(m):
                volume = int(random.uniform(55, 85))
                MyMIDI.addNote(track, channel, pitch, time, d, volume)
            time += d
  
        fullname = path + filename + '.mid'
        
        with open(fullname, "wb") as output_file:
            MyMIDI.writeFile(output_file)

        print('song:', filename) 
        print("MIDI file created!", '\n---------------------------------')
        
        
    #--------------------------------------------------------------------------------
    #Get the chords from the sequence
    def get_chords(self, sequence):
        strings_array = [item[0] for item in sequence if item[0] != '']
        return strings_array
    
    
   
        
    
      