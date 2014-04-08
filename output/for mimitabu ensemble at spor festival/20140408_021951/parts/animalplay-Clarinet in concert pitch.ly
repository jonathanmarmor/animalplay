% 2014-04-07 22:22

\version "2.18.0"
\language "english"

\header {
	composer = \markup { Jonathan Marmor }
	subtitle = \markup { Clarinet in concert pitch }
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
								"Clarinet in concert pitch - Animal Play - 2014-04-08 02:19:51"
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
								"Clarinet in concert pitch - Animal Play - 2014-04-08 02:19:51"
							}
					}
			}
		}
}

\score {
	\context Staff = "Bb Clarinet" {
		\set Staff.instrumentName = \markup { Bb Clarinet }
		\set Staff.shortInstrumentName = \markup { Cl }
		\tempo 4=74-80
		{
			\time 4/4
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<e>2. \mf
			<e>4
		}
		{
			<b>4
			<df'>2.
		}
		{
			<b>4
			<af>4
			<b>4
			<e>4
		}
		{
			<e>4
			<ef>4
			<e>2
		}
		{
			<g>2.
			<gf>4 ~
		}
		{
			<gf>4
			<bf>2.
		}
		{
			<d'>4
			<gf'>2.
		}
		{
			<e'>1
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<g>2. \mf
			<gf>4
		}
		{
			<b>4
			<b>2. ~
		}
		{
			<b>4
			<gf'>2.
		}
		{
			<gf'>4
			<e'>2.
		}
		{
			<b>1
		}
		{
			<e'>4
			<gf'>2. ~
		}
		{
			<gf'>1
		}
		{
			<bf'>2
			<gf'>2
			\bar "||"
		}
		\mark \default
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<f'>4 \mf
			<df'>2.
		}
		{
			<e'>2.
			<gf'>4
		}
		{
			<b>4
			<a>4
			<f>2
		}
		{
			<b>1
		}
		{
			<bf>2
			<b>2
		}
		{
			<gf>4
			<c'>2
			<df'>4
		}
		{
			<ef'>4
			<df'>4
			<gf>2
		}
		{
			<d>2
			<ef>2
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<bf'>2 \mf
			<af'>2
		}
		{
			<df'>2
			<ef'>4
			<c'>4
		}
		{
			<gf>1
		}
		{
			<g>2.
			<c'>4
		}
		{
			<f>1 ~
		}
		{
			<f>4
			<c'>2.
		}
		{
			<f>4
			<f>4
			<d>2
		}
		{
			<gf>4
			<af>2.
			\bar "||"
		}
		\mark \default
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<g'>1 \mf ~
		}
		{
			<g'>1
		}
		{
			<f'>2.
			<d'>4
		}
		{
			<f'>4
			<bf>4
			<gf>2
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<d'>1 \mf ~
		}
		{
			<d'>4
			<g'>2.
		}
		{
			<d'>1
		}
		{
			<a'>2
			<d'>2
			\bar "||"
		}
		\mark \default
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<f'>2 \mf
			<g'>2
		}
		{
			<d'>2
			<f'>4
			<bf>4
		}
		{
			<c'>2.
			<a>4
		}
		{
			<a>2
			<d'>2
		}
		{
			<d'>2
			<ef'>2
		}
		{
			<e'>4
			<e'>2.
		}
		{
			<e'>1
		}
		{
			<d'>1
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1 \f
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		\mark \default
		{
			r2 \mf ~
			r8.
			r16
			r4
		}
		{
			r2.
			r4
		}
		{
			r16
			r8. ~
			r2
			r4
		}
		{
			<bf'>4 \< ~
			<bf'>8. ~
			<bf'>16
			<af'>4 ~
			<af'>8
			<df'>8 \!
			\bar "||"
		}
		{
			<ef'>4 \ff ~
			<ef'>8.
			<df'>16
			<ef'>2 ~
		}
		{
			<ef'>4 ~
			<ef'>8.
			<ef'>16
			<ef'>16
			<gf'>16
			<gf'>16
			<gf'>16
			<ef'>4
		}
		{
			<ef'>4
			<ef'>4
			<ef'>8
			<ef'>8
			<f'>4
		}
		{
			<bf'>2.
			<df''>4
		}
		{
			<bf'>4
			<c''>2 ~
			<c''>8
			<f''>8
		}
		{
			<ef''>4
			<df''>4
			<b'>16
			<gf'>16
			<ef'>16
			<gf'>16 ~
			<gf'>4
		}
		{
			<f'>4 ~
			<f'>8.
			<g'>16
			<bf'>16
			<f'>16
			<f'>16
			<f'>16
			<bf'>4
		}
		{
			<ef''>2. ~
			<ef''>8
			<df''>8
			\bar "||"
		}
		{
			<ef''>4 \mf ~
			<ef''>8
			<bf'>8 ~
			<bf'>4 ~
			<bf'>8.
			<ef''>16
		}
		{
			<gf''>16
			<af''>16
			<bf''>16
			<gf''>16
			<bf''>4
			<gf''>4 ~
			<gf''>8
			<ef''>16
			<gf''>16
			\bar "||"
		}
		{
			<ef''>2 \ff ~
			<ef''>8
			<bf'>8 ~
			<bf'>4
		}
		{
			<ef''>2. ~
			<ef''>8
			<bf'>8 ~
		}
		{
			<bf'>4
			<g'>4
			<f'>4
			<gf'>4 ~
		}
		{
			<gf'>2.
			<bf'>16
			<ef'>16
			<bf>16
			<ef'>16
		}
		{
			<bf'>4
			<gf'>2
			<bf'>16
			<ef''>16
			<gf''>16
			<ef''>16
		}
		{
			<af''>4
			<gf''>4
			<af''>4
			<bf''>4 ~
		}
		{
			<bf''>4 ~
			<bf''>8
			<f''>16
			<bf''>16
			<c'''>4
			<af''>4
		}
		{
			<ef''>4
			<af''>4
			<bf''>2
		}
		{
			<c'''>2 ~
			<c'''>8
			<c'''>16
			<c'''>16
			<df'''>4
		}
		{
			<bf''>4 ~
			<bf''>16
			<g''>16
			<bf''>16
			<df'''>16
			<bf''>4 ~
			<bf''>8
			<gf''>16
			<c''>16
		}
		{
			<bf'>4 ~
			<bf'>8
			<bf'>16
			<ef''>16
			<af'>4 ~
			<af'>8.
			<gf'>16
		}
		{
			<ef'>2
			<f'>4
			<ef'>4
		}
		{
			<df'>8
			<ef'>8 ~
			<ef'>4
			<f'>4 ~
			<f'>16 ~
			<f'>16
			<af'>16
			<f'>16
		}
		{
			<g'>4
			<bf'>2
			<ef''>16
			<g''>16
			<bf''>16
			<g''>16
		}
		{
			<bf''>4 ~
			<bf''>8
			<af''>8
			<g''>2 ~
		}
		{
			<g''>2 ~
			<g''>4
			<bf''>8
			<g''>8
			\bar "||"
		}
		\mark \default
		{
			<bf''>2. \mf ~
			<bf''>8
			<gf''>8
		}
		{
			<ef''>4
			<f''>2
			<ef''>4
		}
		{
			<df''>2 ~
			<df''>8
			<bf'>8
			<g'>4 ~
		}
		{
			<g'>4 ~
			<g'>16
			<bf'>16
			<g'>16
			<ef'>16 ~
			<ef'>4 ~
			<ef'>8
			<c'>8
		}
		{
			<bf>4
			<ef'>2 ~
			<ef'>8
			<df'>8
		}
		{
			<ef'>4
			<ef'>4
			<ef'>4 ~
			<ef'>16
			<c'>16
			<bf>16
			<g>16
		}
		{
			<bf>4 ~
			<bf>8
			<ef'>16
			<bf'>16
			<g'>4 ~
			<g'>8 ~
			<g'>8
		}
		{
			<ef'>2 ~
			<ef'>8
			<bf'>16
			<df''>16
			<bf'>4
			\bar "||"
		}
		{
			<d''>1 \ff ~
		}
		{
			<d''>4
			<f''>16 ~
			<f''>16
			<d''>16
			<f''>16
			<g''>4
			<gf''>4
		}
		{
			<f''>4 ~
			<f''>8
			<af''>8
			<f''>4
			<g''>4
		}
		{
			<f''>1
		}
		{
			<c''>16
			<bf'>16
			<bf'>16
			<c''>16
			<g'>4
			<df'>4 ~
			<df'>8.
			<f'>16
		}
		{
			<df'>16 ~
			<df'>16
			<ef'>16
			<df'>16
			<bf>2. ~
		}
		{
			<bf>4
			<ef'>4
			<bf'>4
			<ef'>16
			<f'>16
			<ef'>16
			<bf'>16
		}
		{
			<g'>4
			<bf'>16
			<ef''>16
			<f''>16
			<ef''>16
			<gf''>4
			<e''>4
			\bar "||"
		}
		{
			<f''>4 \mf \> ~
			<f''>8
			<g''>8
			<bf''>4
			<c'''>4
		}
		{
			<bf''>4 ~
			<bf''>16
			<df'''>16
			<bf''>16
			<df'''>16
			<bf''>4
			<a''>4
		}
		{
			<f''>2.
			<d''>16
			<d''>16
			<f''>16
			<d''>16
		}
		{
			<f''>4
			<c''>2
			<d''>4
		}
		{
			<df''>1 ~
		}
		{
			<df''>2. ~
			<df''>16
			<af'>16
			<e'>16
			<df'>16
		}
		{
			<bf>4 ~
			<bf>8
			<bf>16
			<g>16
			<af>2
		}
		{
			<df'>2 ~
			<df'>16
			<e'>16
			<df'>16 \!
			r16
			r4
			\bar "||"
		}
		{
			<d'>2 \f
			<c'>2 ~
		}
		{
			<c'>1
		}
		{
			<e'>4
			<c'>2
			<e'>4 ~
		}
		{
			<e'>4
			<c'>4
			<g'>2
		}
		{
			<af'>2
			<f'>2 ~
		}
		{
			<f'>1
		}
		{
			<df'>2
			<gf'>2 ~
		}
		{
			<gf'>2.
			<g'>4
			\bar "||"
		}
		\mark \default
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<c'>2 \p
			<c'>2
		}
		{
			<f'>2.
			<f'>4
		}
		{
			<g'>1 ~
		}
		{
			<g'>2
			<a'>4
			<f'>4
		}
		{
			<c'>2
			<ef'>4
			<g'>4
		}
		{
			<c''>4
			<f'>2. ~
		}
		{
			<f'>1
		}
		{
			<bf'>2
			<bf'>2
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<bf'>4 \p
			<a'>2. ~
		}
		{
			<a'>4
			<bf'>4
			<bf'>4
			<ef''>4
		}
		{
			<f''>4
			<a''>2. ~
		}
		{
			<a''>2
			<d''>4
			<f''>4
		}
		{
			<bf''>1 ~
		}
		{
			<bf''>2.
			<af''>4
		}
		{
			<ef''>4
			<df''>2.
		}
		{
			<f''>2.
			<df''>4
			\bar "||"
		}
		\mark \default
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<c'''>2. \p
			<bf''>4
		}
		{
			<bf''>4
			<gf''>2.
		}
		{
			<ef''>2.
			<gf''>4
		}
		{
			<df''>4
			<af'>2.
		}
		{
			<ef'>2.
			<bf'>4 ~
		}
		{
			<bf'>4
			<g'>2.
		}
		{
			<f'>2.
			<a'>4 ~
		}
		{
			<a'>4
			<gf'>2.
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<g'>2. \p
			<df''>4
		}
		{
			<a'>2.
			<g'>4
			\bar "|."
		}
	}
}