# all lilypond pitch names from midi 12 to midi 131
def lyNames(andere={}):
    """gibt die lilypond namen von midi 12 (subkontra) bis midi 131 (sechsgestrichen) raus.
    standardmäßig sind die akzidentien als cis, es, fis, gis und b bezeichnet.
    eine oder mehrere änderungen können über ein dictionary eingegeben werden,
    zum beispiel lyNames({'es':'dis', 'gis':'as'})"""
    lynames = ["c","cis","d","es","e","f","fis","g","gis","a","b","h"]
    names = [andere.get(n,n) for n in lynames]
    out = []
    for oct in range(-3,6):
        if oct < 0: [out.append("%s%s" % (x,","*abs(oct))) for x in names]
        elif oct == 0: out += names
        else: [out.append("%s%s" % (x,"'"*oct)) for x in names]
    return out

def getLyname(midi,lynames,midistart=12):
    """gibt einen tonnamen von lilypond aus der eingabe einer midinote zurück.
    lynames ist eine liste (default=ALLENOTEN) die den tasten ab midistart (default=12) entspricht."""
    return lynames[midi-midistart]

def toNextMidi(midinote):
    """rounds the midi note number to the next integer and 
    returns a tuple with this integer and the cent difference.
    example: 60.23 -> (60,23)
    60.73 -> (61,-27)"""
    nextnote = round(midinote)
    diff = midinote-nextnote
    cent = round(diff*100)
    return (nextnote,cent)

def ftom(f):
    """converts freq to midi"""
    from math import log2
    return log2(f/440)*12 + 69

def midiToLy(midi,subs={}):
    """converts a list of midi numbers to german lilypond names and 
    applies possible substitutions like ({'es':'dis', 'gis':'as'}).
    returns a tupel with two strings: 
    the lilypond names and the cent deviations.
    """
    ly = ""
    cents = ''
    tonnamen = lyNames(subs)
    for i in range(len(midi)):
        midicent = toNextMidi(midi[i])
        ly += ' ' + getLyname(midicent[0],tonnamen)
        cents += '"%+d" ' % midicent[1]
    return (ly,cents)

def toSingleStrings(lis):
    """converts a list to a string in which each list element 
    is enclosed in double quotes followed by a space:
    [1,2] -> '"1" "2"'"""
    out = ''
    for x in lis:
        out += '"%d" ' % x
    return out

def partialsToMidi(basfreq=55,last=16,first=1):
    """converts a number of partials to midi notes.
    requires the ftom function from midi2ly.
    INPUT:
    basfreq = frequency of partial 1
    last = last partial to calculate (default=16)
    first partial to calculate (default=1)
    OUTPUT is a tuple with two elements:
    1. list of midi pitches as floats
    2. list with the partial numbers
    """
    partialNumbers = [x for x in range(first,last+1)]
    partialMidi = [ftom(x*basfreq) for x in partialNumbers]
    return (partialMidi, partialNumbers)

def writeFile(str,filnam):
    with open(filnam,'w') as outfile:
        outfile.write(str)

def fillLilyTemplate(noten="",oben='',unten='',titeloben='',titelunten='',titel='',autor=''):
    """füllt das in midi2ly liegende TEMPLATE und gibt den gesamtstring zurück"""
    return TEMPLATE % (titel,autor,noten,titeloben,oben,titelunten,unten)

#template mit platz für 
#1.titel 2.autor 3.noten 4.titel für drüber 5. zusätze drüber 6. titel für drunter 7. zusätze drunter
TEMPLATE = """
\\version "2.18.2"
\language "deutsch"

\paper {
top-margin = 20
markup-system-spacing = #'((padding . 10))
system-system-spacing = #'((padding . 10))
}

\header {
  title = \markup { \" %s \" }
  composer = \" %s \"
}

toene = {
\\time 16/4
\\accidentalStyle Score.dodecaphonic
%s
}

above = \lyricmode {
\\notemode {\set stanza = \" %s \" }
%s
}

below = \lyricmode {
\\notemode {\set stanza = \" %s \" }
%s
}


\score {
 \\new Staff = "alles" <<
 \\new Voice = "a" \\toene
 \\new Lyrics \with { alignAboveContext = #"alles" }
  \lyricsto "a" \\above
 \\new Lyrics \with { alignBelowContext = #"alles" }
  \lyricsto "a" \\below
 >>

 \layout {
  indent = 0
  \context {
   \Score
   \\remove "Bar_number_engraver"
   }
  \context {
   \Staff
   \\remove "Time_signature_engraver"
   \hide Stem
   \hide BarLine
  }
 }
}
"""
