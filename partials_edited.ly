
\version "2.18.2"
\language "deutsch"

\paper {
top-margin = 20
markup-system-spacing = #'((padding . 10))
system-system-spacing = #'((padding . 10))
}

\header {
  title = \markup { " Teiltöne 1-64 über A=55Hz " }
  composer = " jh 2020 "
}

toene = {
\time 16/4
\accidentalStyle Score.dodecaphonic
\clef "bass"
 a,, a, e a 
\clef "treble" 
cis' e' g' a' h' cis'' dis'' e'' f'' g'' gis'' a'' 
\clef "treble^8"
b'' h'' c''' cis''' d''' dis''' dis''' e''' f''' f''' fis''' g''' 
\clef "treble^15"
g''' gis''' gis''' a''' b''' b''' h''' h''' c'''' c'''' c'''' cis'''' cis'''' d'''' d'''' dis'''' dis'''' dis'''' e'''' e'''' e'''' f'''' f'''' f'''' fis'''' fis'''' fis'''' g'''' g'''' g'''' gis'''' gis'''' gis'''' gis'''' a'''' a''''
}

above = \lyricmode {
\notemode {\set stanza = " Cents: " }
"0" "0" "+2" "0" "-14" "+2" "-31" "0" "+4" "-14" "-49" "+2" "+41" "-31" "-12" "0" "+5" "+4" "-2" "-14" "-29" "-49" "+28" "+2" "-27" "+41" "+6" "-31" "+30" "-12" "+45" "0" "-47" "+5" "-45" "+4" "-49" "-2" "+42" "-14" "+29" "-29" "+12" "-49" "-10" "+28" "-34" "+2" "+38" "-27" "+7" "+41" "-26" "+6" "+38" "-31" "-1" "+30" "-41" "-12" "+17" "+45" "-27" "0" 
}

below = \lyricmode {
\notemode {\set stanza = " Partials: " }
"1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" "21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31" "32" "33" "34" "35" "36" "37" "38" "39" "40" "41" "42" "43" "44" "45" "46" "47" "48" "49" "50" "51" "52" "53" "54" "55" "56" "57" "58" "59" "60" "61" "62" "63" "64" 
}


\score {
 \new Staff = "alles" <<
 \new Voice = "a" \toene
 \new Lyrics \with { alignAboveContext = #"alles" }
  \lyricsto "a" \above
 \new Lyrics \with { alignBelowContext = #"alles" }
  \lyricsto "a" \below
 >>

 \layout {
  indent = 0
  \context {
   \Score
   \remove "Bar_number_engraver"
   }
  \context {
   \Staff
   \remove "Time_signature_engraver"
   \hide Stem
   \hide BarLine
  }
 }
}
