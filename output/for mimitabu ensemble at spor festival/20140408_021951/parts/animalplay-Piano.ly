% 2014-04-07 22:22

\version "2.18.0"
\language "english"

\header {
	composer = \markup { Jonathan Marmor }
	subtitle = \markup { Piano }
	title = \markup { Animal Play }
}

\paper {
	evenFooterMarkup = \markup {
		\column
			{
				\fill-line
					{
						\teeny
							{
								"Piano - Animal Play - 2014-04-08 02:19:51"
							}
					}
			}
		}
	oddFooterMarkup = \markup {
		\column
			{
				\fill-line
					{
						\teeny
							{
								"Piano - Animal Play - 2014-04-08 02:19:51"
							}
					}
			}
		}
}

\score {
	\context PianoStaff = "Piano" <<
		\set PianoStaff.instrumentName = \markup { Piano }
		\set PianoStaff.shortInstrumentName = \markup { Pno }
		\context Staff = "Piano upper" {
			\tempo 4=74-80
			{
				\time 4/4
				<b d' af'>4
				<b e' b'>2. ~
			}
			{
				<b e' b'>2
				<b>4
				<b d' e'>4
			}
			{
				<b df' d' gf' a'>2
				<b g'>2 ~
			}
			{
				<b g'>4
				<b>2.
			}
			{
				<b df' gf'>2
				<b d' g'>2 ~
			}
			{
				<b d' g'>4
				<b' ef''>2.
			}
			{
				<a' df'' d''>1 ~
			}
			{
				<a' df'' d''>4
				<gf'' b''>4
				<gf'' bf'' d'''>4
				<e'' b'' df'''>4
				\bar "||"
			}
			{
				<e'' g'' b'' c''' d'''>2.
				<e'' af'' d'''>4 ~
			}
			{
				<e'' af'' d'''>4
				<e'' gf'' a'' df''' d'''>2.
			}
			{
				<e'' g'' df'''>4
				<e'' gf'' af''>4
				<af'' b''>4
				<b' e'' b''>4 ~
			}
			{
				<b' e'' b''>4
				<b' ef''>4
				<b' e'' gf''>2
			}
			{
				<g'' b''>2.
				<gf'' b''>4 ~
			}
			{
				<gf'' b''>4
				<bf'' b''>2.
			}
			{
				<gf'' b''>4
				<gf'' b''>2. ~
			}
			{
				<gf'' b''>1
				\bar "||"
			}
			{
				<gf'' b''>1
			}
			{
				<ef'' b'' d'''>1
			}
			{
				<b'' e'''>2
				<b'' e'''>4
				<b'' e'''>4
			}
			{
				<e''' gf'''>1
				\bar "||"
			}
			{
				<g'' b'' e'''>2.
				<gf'' b'' e'''>4
			}
			{
				<a'' b'' df'''>4
				<g'' b''>2. ~
			}
			{
				<g'' b''>4
				<gf'' a'' b'' df'''>2.
			}
			{
				<gf'' af'' b''>4
				<b'' e'''>2. ~
			}
			{
				<b'' e'''>1
			}
			{
				<af'' b'' df'''>4
				<d''' gf'''>2. ~
			}
			{
				<d''' gf'''>1
			}
			{
				<af'' bf'' b'' ef''' gf'''>2
				<gf'' af'' bf'' df'''>2
				\bar "||"
			}
			\mark \default
			{
				<g'' c'''>2.
				<df'' f''>4
			}
			{
				<f' bf'>1
			}
			{
				<g' d''>2
				<af' bf'>2
			}
			{
				<d' f' bf'>4
				<df' ef' gf'>4
				<bf df' gf'>2
				\bar "||"
			}
			{
				<bf c' f'>4
				<bf df' gf'>2.
			}
			{
				<c' e' gf'>2.
				<df' ef' gf'>4
			}
			{
				<b ef' b'>4
				<b df' a'>4
				<c' f' a'>2
			}
			{
				<b d'>1
			}
			{
				<bf df' e' gf' af'>2
				<f' a'>2
			}
			{
				<gf' af'>4
				<f' af' ef''>2
				<a' df''>4
			}
			{
				<af' ef''>4
				<ef'' gf''>4
				<ef'' gf'' bf''>2
			}
			{
				<d'' e'' c'''>2
				<bf' df'' ef''>2
				\bar "||"
			}
			{
				<a' c'' e''>4
				<gf' ef''>4
				<c'' df'' e''>2 ~
			}
			{
				<c'' df'' e''>2.
				<a' b' ef''>4
			}
			{
				<f' g'>1 ~
			}
			{
				<f' g'>2
				<b g' b'>2
			}
			{
				<e' a' b'>1 ~
			}
			{
				<e' a' b'>1
			}
			{
				<a' b'>4
				<af' c''>2. ~
			}
			{
				<af' c''>2
				<ef' af' ef''>2
				\bar "||"
			}
			{
				<bf' ef''>2
				<ef' af' af''>2
			}
			{
				<gf' b' ef''>2
				<af' c''>4
				<e' g' c''>4
			}
			{
				<b' ef''>1
			}
			{
				<c'' d'' g''>2.
				<c'' f''>4
			}
			{
				<af' f'' af''>1 ~
			}
			{
				<af' f'' af''>4
				<c'' f''>2.
			}
			{
				<bf' df''>4
				<af' f''>4
				<b' d'' gf''>2 ~
			}
			{
				<b' d'' gf''>4
				<af' ef'' af''>2.
				\bar "||"
			}
			\mark \default
			{
				<b' d'' e''>1
			}
			{
				<a' d''>4
				<g' bf' c'' d''>2.
			}
			{
				<f' g' d''>4
				<d'' af''>2
				<c'' d'' f''>4 ~
			}
			{
				<c'' d'' f''>4
				<bf' c'' g''>4
				<d'' g''>4
				<b' gf''>4
				\bar "||"
			}
			{
				<d'' g'' bf''>1 ~
			}
			{
				<d'' g'' bf''>1
			}
			{
				<d''' f'''>2.
				<a'' b'' gf'''>4
			}
			{
				<f'' bf'' d'''>4
				<f'' bf'' c'''>4
				<a'' d'''>2
				\bar "||"
			}
			{
				<g'' bf'' c''' ef'''>2
				<a'' d'''>2 ~
			}
			{
				<a'' d'''>4
				<g'' b'' f'''>2.
			}
			{
				<e'' bf'' c'''>2
				<e'' a'' e'''>4
				<a'' c'''>4
			}
			{
				<f'' g'' bf'' c''' d'''>4
				<d'' e'' g''>2. ~
			}
			{
				<d'' e'' g''>2
				<d'' g'' b''>4
				<d'' f'' bf''>4
			}
			{
				<g'' a''>4
				<af'' bf'' d'''>2.
			}
			{
				<bf'' d'''>4
				<g'' bf'' d'''>4
				<d'' gf'' d'''>4
				<d'' g''>4 ~
			}
			{
				<d'' g''>2
				<g'' a'' b''>4
				<gf'' a''>4
				\bar "||"
			}
			{
				<d'' a'' d'''>1 ~
			}
			{
				<d'' a'' d'''>4
				<e'' g'' d'''>2.
			}
			{
				<f'' af'' d'''>1
			}
			{
				<a'' d'''>2
				<g'' b''>2
				\bar "||"
			}
			\mark \default
			{
				<df'' f'' df'''>2
				<d'' e'' d'''>2
			}
			{
				<ef'' e'' bf''>1
			}
			{
				<a' d''>2
				<af' ef'' f''>2
			}
			{
				<gf'' af''>2
				<c'' af'' c'''>2
			}
			{
				<e'' af''>4
				<c'' d'' a''>4
				<a' c'' a''>2
			}
			{
				<df'' af''>2.
				<bf' bf'' ef'''>4
			}
			{
				<ef'' f'' df'''>4
				<gf'' a'' df'''>4
				<ef'' f'' c'''>2
			}
			{
				<ef'' g'' af'' c'''>2
				<ef'' af'' bf'' c'''>4
				<ef'' g''>4
				\bar "||"
			}
			{
				<f'' b'' df'''>2
				<d'''>2 ~
			}
			{
				<d'''>2
				<a'' ef'''>4
				<gf'' bf'' df'''>4
			}
			{
				<gf'' a'' c''' df'''>2.
				<df''' e'''>4 ~
			}
			{
				<df''' e'''>2
				<a'' e'''>2
			}
			{
				<b'' d'''>2
				<bf'' c''' ef''' f'''>2
			}
			{
				<e'''>4
				<b'' e'''>2. ~
			}
			{
				<b'' e'''>1
			}
			{
				<g'' d''' f'''>1
				\bar "||"
			}
			{
				<b'' d''' e'''>2
				<af'' b''>2 ~
			}
			{
				<af'' b''>4
				<af'' c''' ef'''>2.
			}
			{
				<af'' df''' f'''>1 ~
			}
			{
				<af'' df''' f'''>1
			}
			{
				<gf'' bf'' ef'''>1 ~
			}
			{
				<gf'' bf'' ef'''>1
			}
			{
				<bf'' ef'''>4
				<af'' c''' ef'''>4
				<df''' ef''' f'''>2 ~
			}
			{
				<df''' ef''' f'''>4
				<af'' ef''' e''' gf'''>2.
				\bar "||"
			}
			{
				<c''' ef'''>4
				<ef'' g''>2
				<b' b'' ef'''>4 ~
			}
			{
				<b' b'' ef'''>4
				<ef'' af''>4
				<g'' bf'' c'''>4
				<g'' bf'' ef'''>4
			}
			{
				<ef'''>2
				<b'' ef''' gf'''>4
				<af'' bf'' df''' ef''' gf'''>4 ~
			}
			{
				<af'' bf'' df''' ef''' gf'''>4
				<ef''' gf'''>2
				<bf'' d''' ef''' f'''>4
			}
			{
				<bf'' c''' ef'''>1 ~
			}
			{
				<bf'' c''' ef'''>4
				<gf'' ef''' gf'''>2.
			}
			{
				<ef''' gf'''>2.
				<bf'' c''' ef'''>4 ~
			}
			{
				<bf'' c''' ef'''>1
				\bar "||"
			}
			\mark \default
			{
				<af'' c''' ef'''>2.
				<gf'' bf'' c'''>4
			}
			{
				<ef'' f'' g'' a'' bf''>2.
				<af'' bf''>4
			}
			{
				<gf'' af'' b'' ef'''>2.
				<af'' b'' ef'''>4
			}
			{
				<ef'' bf'' ef'''>2
				<ef'' af'' df'''>2
				\bar "||"
			}
			{
				<ef'' b'' ef'''>2
				<gf'' bf''>2 ~
			}
			{
				<gf'' bf''>2.
				<ef'' af'' c'''>4
			}
			{
				<gf'' bf'' df'''>4
				<f'' bf''>2
				<ef'' af''>4 ~
			}
			{
				<ef'' af''>1
			}
			{
				<ef'' gf'' bf''>4
				<d'' af'' bf''>2. ~
			}
			{
				<d'' af'' bf''>4
				<gf'' af'' bf'' c'''>4
				<gf'' bf''>2
			}
			{
				<bf' ef'' g''>2.
				<bf' gf'' af''>4 ~
			}
			{
				<bf' gf'' af''>1
				\bar "||"
			}
			{
				<bf'' ef'''>2
				<af'' df''' f'''>2 ~
			}
			{
				<af'' df''' f'''>4
				<af'' ef''' gf'''>4
				<gf'' bf'' ef'''>2
				\bar "||"
			}
			{
				<ef'' af'' bf''>2.
				<bf' ef''>4
			}
			{
				<g' g'' bf''>1
			}
			{
				<ef'' g''>4
				<df'' ef''>4
				<bf' ef''>4
				<bf' gf'' bf''>4 ~
			}
			{
				<bf' gf'' bf''>1
			}
			{
				<c'' ef'' f''>4
				<bf' ef''>2.
			}
			{
				<af' ef'' f''>4
				<gf' bf'>4
				<ef' f' bf'>4
				<bf ef' bf'>4 ~
			}
			{
				<bf ef' bf'>2
				<bf c' bf'>4
				<bf c' g'>4
			}
			{
				<bf bf' ef''>4
				<ef' bf' c''>4
				<ef' g'>2
			}
			{
				<ef' g'>2.
				<ef' f' bf'>4
			}
			{
				<bf ef' df''>2
				<c' ef' c''>2
			}
			{
				<bf ef' g'>2
				<bf df' ef'>2
			}
			{
				<c' f'>2.
				<gf' af'>4
			}
			{
				<ef' g'>2
				<c' ef' bf'>2
			}
			{
				<df' ef'>4
				<ef' g'>2.
			}
			{
				<c' df' ef' f'>2
				<d' ef' f'>2 ~
			}
			{
				<d' ef' f'>1
				\bar "||"
			}
			\mark \default
			{
				<bf ef'>1
			}
			{
				<bf ef' g'>4
				<f' bf' ef''>2.
			}
			{
				<bf' ef''>2.
				<bf' c'' ef''>4 ~
			}
			{
				<bf' c'' ef''>2
				<g' bf'>2
			}
			{
				<ef' g'>4
				<bf ef' f'>2.
			}
			{
				<bf ef' f'>4
				<bf c' bf'>4
				<bf' ef''>2
			}
			{
				<gf'' bf''>2
				<ef'' bf''>2
			}
			{
				<df'' bf'' ef'''>2.
				<g'' bf''>4
				\bar "||"
			}
			{
				<g'' a'' f'''>1 ~
			}
			{
				<g'' a'' f'''>2
				<f'' g''>4
				<df'' e'' bf''>4
			}
			{
				<df'' d'' af''>2
				<f'' af''>4
				<d'' f'' c'''>4
			}
			{
				<ef'' g''>1 ~
			}
			{
				<ef'' g''>4
				<bf' bf'' ef'''>4
				<df'' f'' df'''>2
			}
			{
				<bf' bf'' df'''>1 ~
			}
			{
				<bf' bf'' df'''>4
				<df'' e'' gf'' af'' bf''>4
				<bf' ef'' f''>2
			}
			{
				<g' bf' ef''>2
				<g' bf' b'>4
				<bf' df'' e''>4
				\bar "||"
			}
			{
				<bf' c'' ef''>2
				<g' a' d'' f''>4
				<g' bf' e''>4
			}
			{
				<bf' df'' f''>2
				<ef'' f''>4
				<bf' d'' f'' g''>4
			}
			{
				<a' d'' f''>1
			}
			{
				<d'' f''>4
				<d'' af''>2.
			}
			{
				<af' df''>1 ~
			}
			{
				<af' df''>1
			}
			{
				<bf' c'' e''>2
				<af' df'' af''>2
			}
			{
				<df'' e''>2.
				<a' c''>4
				\bar "||"
			}
			{
				<g' a' d''>2
				<gf' af' c''>2 ~
			}
			{
				<gf' af' c''>1
			}
			{
				<e' f' c'' d''>4
				<gf' a' c''>2
				<df' e'>4 ~
			}
			{
				<df' e'>4
				<g' c''>4
				<ef' g' ef''>2
			}
			{
				<af' b'>2
				<df' f' f''>2 ~
			}
			{
				<df' f' f''>1
			}
			{
				<af' df''>2
				<e' gf'>2 ~
			}
			{
				<e' gf'>2.
				<g' a'>4
				\bar "||"
			}
			\mark \default
			{
				<c'' f''>2.
				<c'' f'' a''>4 ~
			}
			{
				<c'' f'' a''>1
			}
			{
				<a' d''>2
				<bf' c'' ef''>2 ~
			}
			{
				<bf' c'' ef''>2.
				<f' c'' f''>4
				\bar "||"
			}
			{
				<g' c'' f''>2
				<g' a' f''>2
			}
			{
				<bf' c'' f''>2.
				<bf' f''>4
			}
			{
				<bf' g'' bf''>1 ~
			}
			{
				<bf' g'' bf''>2
				<a' f'' a''>4
				<bf' d'' f''>4
			}
			{
				<c'' f'' a''>2
				<a' c'' a''>4
				<a' c'' d'' f''>4
			}
			{
				<f' c'' d''>4
				<df' f'>2. ~
			}
			{
				<df' f'>1
			}
			{
				<bf df' ef'>2
				<c' f' g'>2
				\bar "||"
			}
			{
				<d' f'>2
				<f' g' a'>2
			}
			{
				<df' f'>1
			}
			{
				<df' f' af'>1
			}
			{
				<c' c'' f''>2
				<f' c'' d''>2 ~
			}
			{
				<f' c'' d''>4
				<f' df'' ef''>2
				<a' c''>4
			}
			{
				<bf' d'' f''>4
				<f' a' c''>2.
			}
			{
				<f' g' d''>1
			}
			{
				<f' a' d''>2.
				<f' bf' f''>4
				\bar "||"
			}
			{
				<f' f'' bf''>4
				<a' d'' f''>2. ~
			}
			{
				<a' d'' f''>4
				<f' bf' f''>4
				<f' af' d''>4
				<g' c'' ef''>4
			}
			{
				<f' a' f''>4
				<f' a' f''>2. ~
			}
			{
				<f' a' f''>2
				<d' a' b'>4
				<f' bf'>4
			}
			{
				<gf' af' df''>1 ~
			}
			{
				<gf' af' df''>2.
				<df'' f''>4
			}
			{
				<c'' f'' bf''>4
				<df'' f'' df'''>2. ~
			}
			{
				<df'' f'' df'''>2.
				<df'' f'' df'''>4
				\bar "||"
			}
			\mark \default
			{
				<df'' f''>2.
				<g' b' b''>4 ~
			}
			{
				<g' b' b''>2
				<b' d'' f''>2
			}
			{
				<e'' gf''>4
				<a' d'' a''>4
				<b' d'' af''>2 ~
			}
			{
				<b' d'' af''>2
				<d'' g'' bf''>2
				\bar "||"
			}
			{
				<c''' f'''>2.
				<f'' bf'' f'''>4 ~
			}
			{
				<f'' bf'' f'''>4
				<gf'' a''>2.
			}
			{
				<ef'' af'' ef'''>2.
				<gf'' df''' gf'''>4 ~
			}
			{
				<gf'' df''' gf'''>4
				<af'' df'''>2.
			}
			{
				<gf'' af'' ef'''>2.
				<f'' af'' bf''>4 ~
			}
			{
				<f'' af'' bf''>4
				<d'' bf''>2.
			}
			{
				<f'' a''>2.
				<e'' df'''>4 ~
			}
			{
				<e'' df'''>4
				<a'' d'''>2.
				\bar "||"
			}
			{
				<af'' b'' gf'''>2
				<gf'' a''>2
			}
			{
				<c'' e'' e'''>2
				<gf'' a'' b''>4
				<ef'' f'' c'''>4
			}
			{
				<e'' g'' c'''>4
				<c'' d'' c'''>2. ~
			}
			{
				<c'' d'' c'''>4
				<c'' f'' bf''>2.
				\bar "||"
			}
			{
				<c'' ef'' f''>2.
				<bf' df'' ef''>4
			}
			{
				<a' df''>2.
				<c'' e''>4
				\bar "|."
			}
		}
		\context Staff = "Piano lower" {
			\clef "bass"
			\tempo 4=74-80
			{
				\time 4/4
				<e>4 \p
				<b>2. ~
			}
			{
				<b>2
				<b>4
				<g>4
			}
			{
				<e>2
				<e>2 ~
			}
			{
				<e>4
				<g>2.
			}
			{
				<gf>2
				<g>2 ~
			}
			{
				<g>4
				<b>2.
			}
			{
				<b>1 ~
			}
			{
				<b>4
				<b>4
				<b>4
				<gf>4
				\bar "||"
			}
			{
				<a>2. \mf
				<b>4 ~
			}
			{
				<b>4
				<b>2.
			}
			{
				<b>4
				<b>4
				<gf>4
				<e>4 ~
			}
			{
				<e>4
				<b>4
				<e>2
			}
			{
				<b>2.
				<gf>4 ~
			}
			{
				<gf>4
				<ef>2.
			}
			{
				<d>4
				<e>2. ~
			}
			{
				<e>1
				\bar "||"
			}
			{
				<gf>1 \p
			}
			{
				<gf>1
			}
			{
				<e>2
				<e>4
				<a,>4
			}
			{
				<b,>1
				\bar "||"
			}
			{
				<e>2. \mf
				<d>4
			}
			{
				<ef>4
				<b,>2. ~
			}
			{
				<b,>4
				<e,>2.
			}
			{
				<d,>4
				<e,>2. ~
			}
			{
				<e,>1
			}
			{
				<e,>4
				<d,>2. ~
			}
			{
				<d,>1
			}
			{
				<df,>2
				<ef,>2
				\bar "||"
			}
			{
				<c,>2. \p
				<f,>4
			}
			{
				<f,>1
			}
			{
				<c,>2
				<ef,>2
			}
			{
				<bf,>4
				<af,>4
				<bf,>2
				\bar "||"
			}
			{
				<bf,>4 \mf
				<af,>2.
			}
			{
				<gf,>2.
				<af,>4
			}
			{
				<gf,>4
				<d,>4
				<d,>2
			}
			{
				<d,>1
			}
			{
				<ef,>2
				<f,>2
			}
			{
				<ef,>4
				<c,>2
				<df,>4
			}
			{
				<df,>4
				<gf,>4
				<ef,>2
			}
			{
				<g,>2
				<af,>2
				\bar "||"
			}
			{
				<a,>4 \p
				<bf,>4
				<a,>2 ~
			}
			{
				<a,>2.
				<df>4
			}
			{
				<g>1 ~
			}
			{
				<g>2
				<g>2
			}
			{
				<e>1 ~
			}
			{
				<e>1
			}
			{
				<a,>4
				<af,>2. ~
			}
			{
				<af,>2
				<ef,>2
				\bar "||"
			}
			{
				<f,>2 \mf
				<ef,>2
			}
			{
				<df,>2
				<ef,>4
				<a,>4
			}
			{
				<gf,>1
			}
			{
				<g,>2.
				<f,>4
			}
			{
				<c,>1 ~
			}
			{
				<c,>4
				<f,>2.
			}
			{
				<f,>4
				<df,>4
				<d,>2 ~
			}
			{
				<d,>4
				<ef,>2.
				\bar "||"
			}
			{
				<a,>1 \p
			}
			{
				<d,>4
				<f,>2.
			}
			{
				<c>4
				<bf,>2
				<f,>4 ~
			}
			{
				<f,>4
				<f,>4
				<g,>4
				<d>4
				\bar "||"
			}
			{
				<g>1 \mf ~
			}
			{
				<g>1
			}
			{
				<d>2.
				<d>4
			}
			{
				<bf,>4
				<g,>4
				<d>2
				\bar "||"
			}
			{
				<f>2 \p
				<d>2 ~
			}
			{
				<d>4
				<d>2.
			}
			{
				<g>2
				<d>4
				<d>4
			}
			{
				<ef>4
				<d>2. ~
			}
			{
				<d>2
				<b,>4
				<c>4
			}
			{
				<d>4
				<d>2.
			}
			{
				<c>4
				<g,>4
				<d,>4
				<c,>4 ~
			}
			{
				<c,>2
				<d,>4
				<d,>4
				\bar "||"
			}
			{
				<d,>1 \mf ~
			}
			{
				<d,>4
				<d,>2.
			}
			{
				<c,>1
			}
			{
				<e,>2
				<g,>2
				\bar "||"
			}
			{
				<df>2 \p
				<d>2
			}
			{
				<df>1
			}
			{
				<a,>2
				<df>2
			}
			{
				<df>2
				<af,>2
			}
			{
				<e,>4
				<g,>4
				<f,>2
			}
			{
				<e,>2.
				<ef,>4
			}
			{
				<af,>4
				<gf,>4
				<bf,>2
			}
			{
				<b,>2
				<f,>4
				<ef,>4
				\bar "||"
			}
			{
				<af,>2 \mf
				<g,>2 ~
			}
			{
				<g,>2
				<f,>4
				<gf,>4
			}
			{
				<e,>2.
				<e,>4 ~
			}
			{
				<e,>2
				<b,>2
			}
			{
				<e>2
				<af>2
			}
			{
				<a>4
				<g>2. ~
			}
			{
				<g>1
			}
			{
				<g>1
				\bar "||"
			}
			{
				<g>2 \p
				<e>2 ~
			}
			{
				<e>4
				<f>2.
			}
			{
				<ef>1 ~
			}
			{
				<ef>1
			}
			{
				<gf>1 ~
			}
			{
				<gf>1
			}
			{
				<af>4
				<gf>4
				<af>2 ~
			}
			{
				<af>4
				<b>2.
				\bar "||"
			}
			{
				<g>4 \mf
				<ef>2
				<ef>4 ~
			}
			{
				<ef>4
				<c>4
				<ef>4
				<f>4
			}
			{
				<af>2
				<b>4
				<b>4 ~
			}
			{
				<b>4
				<b>2
				<g>4
			}
			{
				<f>1 ~
			}
			{
				<f>4
				<b,>2.
			}
			{
				<b,>2.
				<f,>4 ~
			}
			{
				<f,>1
				\bar "||"
			}
			{
				<c,>2. \mp
				<ef,>4
			}
			{
				<c,>2.
				<ef,>4
			}
			{
				<df,>2.
				<gf,>4
			}
			{
				<bf,>2
				<af,>2
				\bar "||"
			}
			{
				<gf,>2 \f
				<ef,>2 ~
			}
			{
				<ef,>2.
				<ef,>4
			}
			{
				<df,>4
				<ef,>2
				<af,>4 ~
			}
			{
				<af,>1
			}
			{
				<ef>4
				<f>2. ~
			}
			{
				<f>4
				<ef>4
				<ef>2
			}
			{
				<bf,>2.
				<b,>4 ~
			}
			{
				<b,>1
				\bar "||"
			}
			{
				<bf,>2 \mp
				<df>2 ~
			}
			{
				<df>4
				<df>4
				<ef>2
				\bar "||"
			}
			{
				<ef>2. \f
				<ef>4
			}
			{
				<bf,>1
			}
			{
				<ef>4
				<bf>4
				<af>4
				<bf>4 ~
			}
			{
				<bf>1
			}
			{
				<bf>4
				<bf>2.
			}
			{
				<bf>4
				<ef>4
				<af>4
				<bf>4 ~
			}
			{
				<bf>2
				<ef>4
				<ef>4
			}
			{
				<bf,>4
				<f>4
				<bf>2
			}
			{
				<bf>2.
				<af>4
			}
			{
				<bf>2
				<bf>2
			}
			{
				<bf>2
				<af>2
			}
			{
				<bf>2.
				<bf>4
			}
			{
				<bf>2
				<af>2
			}
			{
				<bf>4
				<bf>2.
			}
			{
				<af>2
				<bf>2 ~
			}
			{
				<bf>1
				\bar "||"
			}
			{
				<bf>1 \mp
			}
			{
				<g>4
				<bf>2.
			}
			{
				<g>2.
				<g>4 ~
			}
			{
				<g>2
				<f>2
			}
			{
				<ef>4
				<bf,>2.
			}
			{
				<bf,>4
				<af,>4
				<g,>2
			}
			{
				<bf,>2
				<c>2
			}
			{
				<gf>2.
				<g>4
				\bar "||"
			}
			{
				<bf>1 \f ~
			}
			{
				<bf>2
				<bf>4
				<gf>4
			}
			{
				<bf>2
				<bf>4
				<bf>4
			}
			{
				<f>1 ~
			}
			{
				<f>4
				<ef>4
				<bf,>2
			}
			{
				<f,>1 ~
			}
			{
				<f,>4
				<ef,>4
				<f,>2
			}
			{
				<ef,>2
				<ef,>4
				<gf,>4
				\bar "||"
			}
			{
				<bf,>2 \mp
				<c>4
				<c>4
			}
			{
				<bf,>2
				<f,>4
				<c,>4
			}
			{
				<d,>1
			}
			{
				<a,>4
				<e,>2.
			}
			{
				<df,>1 ~
			}
			{
				<df,>1
			}
			{
				<c,>2
				<df,>2
			}
			{
				<df,>2.
				<e,>4
				\bar "||"
			}
			{
				<e,>2 \f
				<ef,>2 ~
			}
			{
				<ef,>1
			}
			{
				<a,>4
				<d>2
				<gf>4 ~
			}
			{
				<gf>4
				<c>4
				<ef>2
			}
			{
				<b,>2
				<df>2 ~
			}
			{
				<df>1
			}
			{
				<af>2
				<b>2 ~
			}
			{
				<b>2.
				<g>4
				\bar "||"
			}
			{
				<f>2. \p
				<ef>4 ~
			}
			{
				<ef>1
			}
			{
				<a>2
				<bf>2 ~
			}
			{
				<bf>2.
				<bf>4
				\bar "||"
			}
			{
				<bf>2 \mp
				<a>2
			}
			{
				<g>2.
				<af>4
			}
			{
				<f>1 ~
			}
			{
				<f>2
				<f>4
				<f>4
			}
			{
				<a>2
				<f>4
				<g>4
			}
			{
				<f>4
				<df>2. ~
			}
			{
				<df>1
			}
			{
				<af,>2
				<d,>2
				\bar "||"
			}
			{
				<d,>2 \p
				<d,>2
			}
			{
				<df,>1
			}
			{
				<ef,>1
			}
			{
				<f,>2
				<af,>2 ~
			}
			{
				<af,>4
				<bf,>2
				<f,>4
			}
			{
				<g,>4
				<c>2.
			}
			{
				<bf,>1
			}
			{
				<c>2.
				<bf,>4
				\bar "||"
			}
			{
				<bf,>4 \mp
				<f>2. ~
			}
			{
				<f>4
				<bf>4
				<bf>4
				<f>4
			}
			{
				<f>4
				<f>2. ~
			}
			{
				<f>2
				<f>4
				<bf>4
			}
			{
				<bf>1 ~
			}
			{
				<bf>2.
				<af>4
			}
			{
				<bf>4
				<f>2. ~
			}
			{
				<f>2.
				<df>4
				\bar "||"
			}
			{
				<df>2. \p
				<g>4 ~
			}
			{
				<g>2
				<g>2
			}
			{
				<a>4
				<a>4
				<b>2 ~
			}
			{
				<b>2
				<bf>2
				\bar "||"
			}
			{
				<f>2. \mp
				<f>4 ~
			}
			{
				<f>4
				<d>2.
			}
			{
				<bf,>2.
				<gf,>4 ~
			}
			{
				<gf,>4
				<af,>2.
			}
			{
				<df>2.
				<c>4 ~
			}
			{
				<c>4
				<g,>2.
			}
			{
				<d>2.
				<a,>4 ~
			}
			{
				<a,>4
				<gf,>2.
				\bar "||"
			}
			{
				<e,>2 \p
				<df,>2
			}
			{
				<c,>2
				<ef,>4
				<af,>4
			}
			{
				<g,>4
				<g,>2. ~
			}
			{
				<g,>4
				<af,>2.
				\bar "||"
			}
			{
				<g,>2. \mp
				<af,>4
			}
			{
				<a,>2.
				<g,>4
				\bar "|."
			}
		}
	>>
}