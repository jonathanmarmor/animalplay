% 2014-04-07 22:21

\version "2.18.0"
\language "english"

\header {
	composer = \markup { Jonathan Marmor }
	subtitle = \markup { Violin }
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
								"Violin - Animal Play - 2014-04-08 02:19:51"
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
								"Violin - Animal Play - 2014-04-08 02:19:51"
							}
					}
			}
		}
}

\score {
	\context Staff = "Violin" {
		\set Staff.instrumentName = \markup { Violin }
		\set Staff.shortInstrumentName = \markup { Vn }
		\tempo 4=74-80
		{
			\time 4/4
			<g'' af''>4 \mp
			<e''>2 ~
			<e''>8
			<b'>8
		}
		{
			<e''>4
			<e'' gf''>8
			<b'>8
			<gf'>4
			<g'>4
		}
		{
			<f' gf'>2
			<e'>2
		}
		{
			<f' g'>4
			<g'>2.
		}
		{
			<df''>4
			<gf''>8
			<e'' f''>8
			<g''>2
		}
		{
			<g'' a''>4
			<ef''>2.
		}
		{
			<df'' d''>1
		}
		{
			<gf''>4
			<d''>4
			<c'' d''>4 ~
			<c'' d''>4
			\bar "||"
		}
		{
			<a' bf'>2. \f
			<a' bf'>4 ~
		}
		{
			<a' bf'>4
			<af' bf'>2.
		}
		{
			<a' b'>4
			<df''>4
			<gf''>4
			<gf'' af''>4 ~
		}
		{
			<gf'' af''>16
			<b'>16
			<b'>16
			<bf' b'>16
			<b'>4
			<a' b'>2
		}
		{
			<b'>2.
			<b'>4
		}
		{
			<gf'>4
			<ef'>2 ~
			<ef'>8
			<af'>16
			<gf'>16
		}
		{
			<gf' g'>4
			<b'>2.
		}
		{
			<e''>1
			\bar "||"
		}
		{
			<ef''>1 \mp ~
		}
		{
			<ef''>1
		}
		{
			<e'' gf''>2
			<df'' ef''>4
			<b'>4
		}
		{
			<df''>1
			\bar "||"
		}
		{
			<b'>2 \f
			<g'>4
			<a'>4
		}
		{
			<gf'>4
			<gf' g'>2. ~
		}
		{
			<gf' g'>4
			<g' af'>2.
		}
		{
			<gf'>4
			<e'>16
			<d' e'>8. ~
			<d' e'>2
		}
		{
			<e'>2. ~
			<e'>8. ~
			<e'>16
		}
		{
			<f' g'>4
			<gf'>2.
		}
		{
			<b'>1
		}
		{
			<b' df''>4 ~
			<b' df''>8.
			<c'' d''>16
			<b'>8
			<af' bf'>8 ~
			<af' bf'>4
			\bar "||"
		}
		\mark \default
		{
			<g'>2. \mp
			<df'>4
		}
		{
			<f'>1
		}
		{
			<a'>2
			<g' a'>4
			<af'>16
			<c''>16
			<ef''>16
			<af''>16
		}
		{
			<d''>4
			<af'>4
			<bf'>2
			\bar "||"
		}
		{
			<d''>4 \f
			<f''>8
			<gf''>8 ~
			<gf''>2
		}
		{
			<a''>2.
			<af''>4
		}
		{
			<gf''>4 ~
			<gf''>4
			<a''>2
		}
		{
			<d''>2.
			<b'>16
			<d''>16 ~
			<d''>16
			<b'>16
		}
		{
			<ef''>2
			<b'>4 ~
			<b'>8
			<f''>16
			<d''>16
		}
		{
			<c''>4
			<af'>4
			<f'>16
			<ef'>16
			<f'>16
			<af'>16
			<a'>4
		}
		{
			<df''>4
			<df''>4
			<gf''>2
		}
		{
			<g''>4 ~
			<g''>8. ~
			<g''>16
			<af''>16
			<bf''>8. ~
			<bf''>4
			\bar "||"
		}
		{
			<e''>4 \mp
			<df''>4
			<a'>2
		}
		{
			<gf'>2. ~
			<gf'>4
		}
		{
			<g'>1 ~
		}
		{
			<g'>4
			<f'>16
			<g'>16
			<c''>16
			<c''>16
			<d''>2
		}
		{
			<b'>2.
			<g'>4
		}
		{
			<a'>1
		}
		{
			<gf'>4
			<f'>2. ~
		}
		{
			<f'>2
			<ef'>4
			<ef'>8
			<ef'>8
			\bar "||"
		}
		{
			<d'>4 \f ~
			<d'>8.
			<g'>16
			<ef'>4
			<af'>16
			<gf' g'>16
			<af'>16
			<af'>16
		}
		{
			<a'>2
			<af'>4
			<g' af'>4
		}
		{
			<e' f'>2. ~
			<e' f'>16
			<gf'>16
			<ef'>16
			<gf'>16
		}
		{
			<g'>2.
			<c''>4
		}
		{
			<bf' c''>1 ~
		}
		{
			<bf' c''>8
			<c''>16
			<b' c''>16
			<a'>2.
		}
		{
			<bf'>4
			<a'>4
			<b'>2 ~
		}
		{
			<b'>4
			<c'' df''>2.
			\bar "||"
		}
		\mark \default
		{
			<b'>2. \mp
			<bf' b'>16
			<d''>16
			<e''>16
			<d''>16
		}
		{
			<gf''>4
			<e'' gf''>2.
		}
		{
			<d'' e''>4
			<af''>4 ~
			<af''>8.
			<gf''>16
			<c'''>4 ~
		}
		{
			<c'''>4
			<d'''>4
			<b''>4
			<a''>4
			\bar "||"
		}
		{
			<g''>2 \f ~
			<g''>8
			<g'' a''>8
			<bf''>8
			<d'''>8
		}
		{
			<bf''>8
			<g''>8 ~
			<g''>2.
		}
		{
			<d''>8
			<f''>8 ~
			<f''>2
			<gf''>4
		}
		{
			<f''>4
			<d''>4
			<gf''>4 ~
			<gf''>16
			<e''>16
			<d''>16
			<gf''>16
			\bar "||"
		}
		{
			<d''>2 \mp ~
			<d''>2
		}
		{
			<a'>4
			<b'>2
			<f''>8
			<d''>8
		}
		{
			<g''>4
			<d''>16
			<e''>16
			<g''>16
			<g''>16
			<c''>4
			<gf''>4
		}
		{
			<ef''>4
			<g''>2. ~
		}
		{
			<g''>4
			<a''>8
			<d''>8
			<g'>4
			<c''>4
		}
		{
			<b'>4
			<bf'>2
			<f''>16
			<d''>16
			<f''>16
			<d''>16
		}
		{
			<g''>4
			<bf''>4
			<d'''>4
			<c'''>4 ~
		}
		{
			<c'''>4
			<d'''>8
			<c'''>8
			<d'''>4
			<c'''>4
			\bar "||"
		}
		{
			<d'''>1 \f ~
		}
		{
			<d'''>4
			<a''>16
			<e''>8. ~
			<e''>2
		}
		{
			<f''>2. ~
			<f''>8.
			<f'' g''>16
		}
		{
			<gf''>4 ~
			<gf''>8.
			<a''>16
			<d'''>2
			\bar "||"
		}
		\mark \default
		{
			<df'''>4 \mp ~
			<df'''>16 ~
			<df'''>16
			<af''>16
			<f''>16
			<bf'>4 ~
			<bf'>8.
			<g'>16
		}
		{
			<af'>2.
			<df''>4
		}
		{
			<d''>4 ~
			<d''>8
			<d'' ef''>8
			<b'>2
		}
		{
			<bf' b'>4
			<a' bf'>8
			<af'>8
			<af' a'>2
		}
		{
			<af'>4
			<gf' af'>4
			<a'>2
		}
		{
			<b'>2
			<e''>4
			<ef''>4
		}
		{
			<af''>4
			<a''>4
			<bf''>16
			<c'''>16
			<g''>8 ~
			<g''>4
		}
		{
			<b''>4 ~
			<b''>8.
			<e'''>16
			<ef''' f'''>4
			<ef'''>4
			\bar "||"
		}
		{
			<df'''>2 \f \>
			<g''>2 ~
		}
		{
			<g''>2
			<c'''>4
			<df'''>4
		}
		{
			<c''' df'''>2.
			<a''>4 ~
		}
		{
			<a''>4
			<g''>16 ~
			<g''>16
			<a''>16
			<e'''>16
			<d'''>2
		}
		{
			<a''>4 ~
			<a''>8
			<b''>16
			<gf''>16
			<af''>2
		}
		{
			<a''>4
			<g''>2 ~
			<g''>8 \!
			r8
		}
		{
			r1
		}
		{
			r2. ~
			r16
			r16
			r16
			r16
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
			<c' ef'>4 \mf
			<g g'>2
			<ef' b'>4 ~
		}
		{
			<ef' b'>4
			<c' af'>4
			<c' g'>4
			<bf f'>4
		}
		{
			<ef' af'>2
			<b ef'>4
			<af ef'>4
		}
		{
			<af df'>4
			<b gf'>2
			<bf g'>4
		}
		{
			<c' ef'>1 ~
		}
		{
			<c' ef'>4
			<b ef'>2.
		}
		{
			<ef' gf'>2.
			<c' ef'>4
		}
		{
			<c' f'>1
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
			<ef' gf'>2 \f
			<bf gf'>2 ~
		}
		{
			<bf gf'>2.
			<c' ef'>4
		}
		{
			<df' gf'>4
			<bf f'>2
			<df' bf'>4 ~
		}
		{
			<df' bf'>1
		}
		{
			<gf' bf'>4
			<bf ef'>2.
		}
		{
			<bf d'>4
			<df' gf'>4
			<bf ef'>2
		}
		{
			<ef' g'>2.
			<bf df'>4
		}
		{
			<b df'>1
			\bar "||"
		}
		{
			r1
		}
		{
			r1
			\bar "||"
		}
		{
			<af bf>2. \f
			<bf ef'>4
		}
		{
			<bf g'>1
		}
		{
			<bf g'>4
			<ef' bf'>4
			<ef' f'>4
			<bf ef'>4 ~
		}
		{
			<bf ef'>1
		}
		{
			<bf f'>4
			<ef' bf'>2.
		}
		{
			<af ef'>4
			<bf gf'>4
			<bf ef'>4
			<bf f'>4
		}
		{
			<f' bf'>2
			<bf c'>4
			<c' ef'>4
		}
		{
			<bf ef'>4
			<c' f'>4
			<bf g'>2
		}
		{
			<g' bf'>2.
			<df' af'>4
		}
		{
			<g' bf'>2
			<ef' gf'>2
		}
		{
			<g g'>2
			<bf' df''>2
		}
		{
			<bf f'>2.
			<gf' bf'>4
		}
		{
			<bf df'>2
			<af c'>2
		}
		{
			<g bf>4
			<ef' g'>2.
		}
		{
			<bf f'>2
			<d' f'>2
		}
		{
			<ef' g'>1
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
			<bf f'>1 \f
		}
		{
			<bf g'>2
			<f' bf'>4
			<df' gf'>4
		}
		{
			<af f'>2
			<f' bf'>4
			<d' g'>4
		}
		{
			<c' g'>1 ~
		}
		{
			<c' g'>4
			<ef' g'>4
			<bf f'>2
		}
		{
			<df' f'>1 ~
		}
		{
			<df' f'>4
			<e' af'>4
			<bf f'>2
		}
		{
			<ef' bf'>2
			<bf gf'>4
			<df' gf'>4
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
			<g>2 \f
			<c'>2 ~
		}
		{
			<c'>1
		}
		{
			<d'>4
			<a>2
			<df'>4 ~
		}
		{
			<df'>4
			<g'>4
			<ef'>2
		}
		{
			<b>2
			<bf>2 ~
		}
		{
			<bf>1
		}
		{
			<af>2
			<b>2 ~
		}
		{
			<b>2.
			<a>4
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
			<f'>2 \p
			<f'>2
		}
		{
			<f'>2.
			<af'>4
		}
		{
			<bf'>1 ~
		}
		{
			<bf'>2
			<f''>4
			<bf'>4
		}
		{
			<f''>2
			<f''>4
			<d''>4
		}
		{
			<d''>4
			<df''>2. ~
		}
		{
			<df''>1
		}
		{
			<gf''>2
			<c''>2
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
			<f'>4 \p
			<d'>2. ~
		}
		{
			<d'>4
			<f'>4
			<d'>4
			<g'>4
		}
		{
			<f'>4
			<a'>2. ~
		}
		{
			<a'>2
			<f'>4
			<bf'>4
		}
		{
			<ef'>1 ~
		}
		{
			<ef'>2.
			<df'>4
		}
		{
			<c'>4
			<f'>2.
		}
		{
			<f'>2.
			<f'>4
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
			<c'>2. \p
			<f'>4
		}
		{
			<f'>4
			<a'>2.
		}
		{
			<ef'>2.
			<bf'>4
		}
		{
			<gf'>4
			<df'>2.
		}
		{
			<af'>2.
			<f'>4 ~
		}
		{
			<f'>4
			<d'>2.
		}
		{
			<a'>2.
			<df''>4 ~
		}
		{
			<df''>4
			<gf''>2.
			\bar "||"
		}
		{
			r1
		}
		{
			r1
		}
		{
			r1 \mp
		}
		{
			r1
			\bar "||"
		}
		{
			r2 \f ~
			r8
			r16
			r16
			r4
		}
		{
			<g' a'>2. \<
			<g'>4 \!
			\bar "|."
		}
	}
}