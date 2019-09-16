#!/usr/bin/env python
# encoding: utf-8
'''
@author: 10858
@license: (C) Copyright
@contact: xxx@qq.com
@software: PyCharm
@file: ACCO_GLOBALDATA_Chord.py
@time: 2019-08-18 14:38
@desc:
'''


from music21 import *


class CChord:
    class CChordEnum:
        C = 0
        DM = 1
        EM = 2
        F = 3
        G = 4
        AM = 5
        G7 = 6
        #E7 = 7


    C = chord.Chord([note.Note('C'), note.Note('F'), note.Note('G')], duration=duration.Duration(4.0))
    Dm = chord.Chord([2, 4, 6], duration=duration.Duration(4.0))
    Em = chord.Chord([3, 5, 7], duration=duration.Duration(4.0))
    F = chord.Chord([4, 6, 1], duration=duration.Duration(4.0))
    G = chord.Chord([5, 7, 2], duration=duration.Duration(4.0))
    G7 = chord.Chord([5, 7, 2, 4], duration=duration.Duration(4.0))
    Am = chord.Chord([6, 1, 3], duration=duration.Duration(4.0))
    #E7 = chord.Chord([])

    CChord_To_Enum = {C: CChordEnum.C, Dm: CChordEnum.DM, Em: CChordEnum.EM, F:CChordEnum.F,
                      G: CChordEnum.G, G7:CChordEnum.G7, Am: CChordEnum.AM}
    Enum_To_CChord = {CChordEnum.C: C, CChordEnum.DM: Dm, CChordEnum.EM: Em, CChordEnum.F: F,
                      CChordEnum.G: G, CChordEnum.G7: G7, CChordEnum.AM: Am}

    Enum_To_Column_weight = {CChordEnum.C: [0, 2, 8],
                             CChordEnum.F: [1, 3, 11],
                             CChordEnum.EM: [8, 13, 10],
                             CChordEnum.AM: [0, 3, 9],
                             CChordEnum.DM: [4, 6, 11],
                             CChordEnum.G: [5, 7, 13],
                             CChordEnum.G7: [4, 5, 7, 12, 13]}

    '''
    Enum_To_Column_weight = {CChordEnum.C: [0],
                             CChordEnum.F: [1],
                             CChordEnum.EM: [2],
                             CChordEnum.AM: [3],
                             CChordEnum.DM: [4],
                             CChordEnum.G: [5],
                             CChordEnum.G7: [6]}
    '''
    brokenChord_To_Enum = {'C3 G3 C4 G3 E4 G3 C4 G3': CChordEnum.C,
                           'A2 A3 C4 A3 E4 A3 C4 A3': CChordEnum.AM,
                           'E3 G3 B3 G3 E4 G3 B3 G3': CChordEnum.EM,
                           'D3 A3 D4 A3 F4 A3 D4 A3': CChordEnum.DM,
                           'G2 G3 B3 G3 G4 G3 B3 G3': CChordEnum.G,
                           'F3 A3 C4 A3 F4 A3 C4 A3': CChordEnum.F}

    Enum_To_brokenChord = {CChordEnum.C: 'C3 G3 C4 G3 E4 G3 C4 G3',
                           CChordEnum.AM: 'A2 A3 C4 A3 E4 A3 C4 A3',
                           CChordEnum.EM: 'E3 G3 B3 G3 E4 G3 B3 G3',
                           CChordEnum.DM: 'D3 A3 D4 A3 F4 A3 D4 A3',
                           CChordEnum.G: 'G2 G3 B3 G3 G4 G3 B3 G3',
                           CChordEnum.F: 'F3 A3 C4 A3 F4 A3 C4 A3'}

if __name__ == "__main__":
    #print(note.Note(0).pitch)
    CChord.C.show("text")
    print(CChord.C.pitches)
    print(CChord.CChordEnum.C * 8)

    out_stream = stream.Stream()
    out_stream.insert(0.0, key.Key('C'))
    out_stream.insert(0.0, CChord.C)
    out_stream.insert(4.0, note.Note('C'))
    out_stream.insert(5.0, note.Note('D'))
    out_stream.insert(6.0, note.Note('E'))
    out_stream.insert(7.0, note.Note('F'))
    out_stream.insert(8.0, note.Note('G'))
    out_stream.insert(9.0, note.Note('A'))
    out_stream.insert(10.0, note.Note('B'))
    out_stream.insert(11.0, note.Note(0))
    #out_stream.show("text")
    mf = midi.translate.streamToMidiFile(out_stream)
    mf.open("my_music_chord_test.midi", 'wb')
    mf.write()
    #print("Your generated music is saved in output/my_music.midi")
    mf.close()

    pingfan = converter.parse('../ACCO_DATASET/train/houlai.mid')
    pingfan.show('text')
    for n in pingfan[0]:
        if isinstance(n, note.Note):
            print(n.pitch)
            print(n.beatStrength)
    #pingfan.show("text")
