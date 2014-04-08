% 2014-04-07 22:22

\version "2.18.0"
\language "english"

\header {
	composer = \markup { Jonathan Marmor }
	subtitle = \markup { Cello }
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
								"Cello - Animal Play - 2014-04-08 02:19:51"
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
								"Cello - Animal Play - 2014-04-08 02:19:51"
							}
					}
			}
		}
}

\score {
	\context Staff = "Cello" {
		\clef "bass"
		\set Staff.instrumentName = \markup { Cello }
		\set Staff.shortInstrumentName = \markup { Vc }
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
			<g>2. \mf
			<d>4
		}
		{
			<d>4
			<a>2.
		}
		{
			<e'>4
			<b>4
			<gf>4
			<b>4
		}
		{
			<e'>4
			<ef'>4
			<gf'>2
		}
		{
			<b>2.
			<b>4 ~
		}
		{
			<b>4
			<ef'>2.
		}
		{
			<gf'>4
			<gf'>2.
		}
		{
			<b>1
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
			<e'>2. \mf
			<b>4
		}
		{
			<df'>4
			<g>2. ~
		}
		{
			<g>4
			<e>2.
		}
		{
			<gf>4
			<b>2.
		}
		{
			<e>1
		}
		{
			<b>4
			<gf>2. ~
		}
		{
			<gf>1
		}
		{
			<df'>2
			<af>2
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
			<c'>4 \mf
			<f>2.
		}
		{
			<gf>2.
			<df'>4
		}
		{
			<ef'>4
			<b>4
			<a>2
		}
		{
			<d>1
		}
		{
			<ef>2
			<d>2
		}
		{
			<ef>4
			<ef>2
			<a>4
		}
		{
			<af>4
			<ef>4
			<bf>2
		}
		{
			<e'>2
			<af'>2
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
			<d'>2 \mf
			<af>2
		}
		{
			<a>2
			<c'>4
			<g'>4
		}
		{
			<ef'>1
		}
		{
			<g'>2.
			<f'>4
		}
		{
			<c'>1 ~
		}
		{
			<c'>4
			<f'>2.
		}
		{
			<f'>4
			<af'>4
			<d'>2
		}
		{
			<gf'>4
			<af'>2.
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
			<d'>1 \mf ~
		}
		{
			<d'>1
		}
		{
			<d'>2.
			<a>4
		}
		{
			<d'>4
			<g>4
			<d>2
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
			<g>2.
		}
		{
			<af>1
		}
		{
			<e>2
			<g>2
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
			<df'>2 \mf
			<d'>2
		}
		{
			<g'>2
			<a'>4
			<gf'>4
		}
		{
			<a'>2.
			<g'>4
		}
		{
			<e'>2
			<e'>2
		}
		{
			<b>2
			<f'>2
		}
		{
			<a'>4
			<e'>2.
		}
		{
			<b>1
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
			<c' g'>4 \mf
			<ef' g'>2
			<b ef'>4 ~
		}
		{
			<b ef'>4
			<af c'>4
			<g c'>4
			<ef' g'>4
		}
		{
			<af ef'>2
			<ef' gf'>4
			<df' gf'>4
		}
		{
			<af df'>4
			<b ef'>2
			<g ef'>4
		}
		{
			<ef' bf'>1 ~
		}
		{
			<ef' bf'>4
			<b gf'>2.
		}
		{
			<ef' gf'>2.
			<bf ef'>4
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
			<bf ef'>2 ~
		}
		{
			<bf ef'>2.
			<af c'>4
		}
		{
			<bf gf'>4
			<ef' f'>2
			<ef' af'>4 ~
		}
		{
			<ef' af'>1
		}
		{
			<bf ef'>4
			<d' f'>2.
		}
		{
			<bf ef'>4
			<af c'>4
			<bf gf'>2
		}
		{
			<ef' bf'>2.
			<af b>4
		}
		{
			<gf df'>1
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
			<ef' bf'>2. \f
			<bf ef'>4
		}
		{
			<g bf>1
		}
		{
			<g bf>4
			<bf g'>4
			<f' af'>4
			<gf ef'>4 ~
		}
		{
			<gf ef'>1
		}
		{
			<c' ef'>4
			<gf ef'>2.
		}
		{
			<ef' af'>4
			<ef' gf'>4
			<af f'>4
			<bf f'>4
		}
		{
			<bf ef'>2
			<c' ef'>4
			<g ef'>4
		}
		{
			<bf ef'>4
			<bf f'>4
			<ef' bf'>2
		}
		{
			<c' g'>2.
			<df' bf'>4
		}
		{
			<ef' g'>2
			<bf ef'>2
		}
		{
			<g ef'>2
			<bf bf'>2
		}
		{
			<ef' bf'>2.
			<af' bf'>4
		}
		{
			<bf g'>2
			<ef' bf'>2
		}
		{
			<bf ef'>4
			<bf g'>2.
		}
		{
			<ef' bf'>2
			<bf d'>2
		}
		{
			<bf f'>1
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
			<d' g'>1 \f
		}
		{
			<d' g'>2
			<bf g'>4
			<df' e'>4
		}
		{
			<bf f'>2
			<f' af'>4
			<g bf>4
		}
		{
			<bf ef'>1 ~
		}
		{
			<bf ef'>4
			<g bf>4
			<bf df'>2
		}
		{
			<bf f'>1 ~
		}
		{
			<bf f'>4
			<af df'>4
			<bf ef'>2
		}
		{
			<bf ef'>2
			<g bf>4
			<gf df'>4
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
			r4 \ff ~
			r16
			r16
			r16
			r16
			r2 ~
		}
		{
			r1
		}
		{
			r4
			r4 ~
			r8.
			r16
			<df,>4 \< ~
		}
		{
			<df,>4
			<e,>4
			<ef,>2
		}
		{
			<af,>2
			<bf,>2 ~
		}
		{
			<bf,>1
		}
		{
			<af,>2
			<e,>4 ~
			<e,>8.
			<df, d,>16
		}
		{
			<e,>2.
			<a,>4 \!
			\bar "||"
		}
		\mark \default
		{
			<af,>2. \mp
			<ef,>4 ~
		}
		{
			<ef,>2. ~
			<ef,>8
			<f,>8 ~
		}
		{
			<f,>4 ~
			<f,>8
			<d,>16 ~
			<d,>16
			<f,>2
		}
		{
			<f, gf,>2.
			<c,>4
			\bar "||"
		}
		{
			<f,>2 \f
			<c,>4 ~
			<c,>8.
			<c,>16
		}
		{
			<g,>2.
			<c,>4 ~
		}
		{
			<c,>2.
			<ef,>4
		}
		{
			<f,>2
			<a,>4
			<bf,>4
		}
		{
			<a,>8
			<c>8 ~
			<c>4
			<ef>4
			<g>4
		}
		{
			<a>4
			<f>2. ~
		}
		{
			<f>2. ~
			<f>8
			<f>16
			<f>16
		}
		{
			<af>4
			<bf>16
			<gf>16
			<f>16
			<af>16
			<bf>2
			\bar "||"
		}
		{
			<a>4 \mp ~
			<a>8
			<f>16
			<d>16
			<bf,>4 ~
			<bf,>8.
			<c>16
		}
		{
			<df>1
		}
		{
			<f>2. ~
			<f>8
			<ef>8
		}
		{
			<f>4 ~
			<f>8.
			<c>16
			<bf,>2
		}
		{
			<af,>4
			<bf,>2
			<c>4 ~
		}
		{
			<c>4
			<f>8
			<c>8 ~
			<c>2
		}
		{
			<f>1
		}
		{
			<g>2.
			<bf>4
			\bar "||"
		}
		{
			<f>4 \f
			<e f>2.
		}
		{
			<f>4
			<f>4
			<d e>4
			<c d>4
		}
		{
			<a,>4
			<f,>2. ~
		}
		{
			<f,>2
			<d,>4
			<df,>4
		}
		{
			<ef,>2 ~
			<ef,>8
			<f,>8
			<e, gf,>8
			<f, gf,>8
		}
		{
			<ef,>2.
			<f,>4
		}
		{
			<ef,>4
			<f,>2
			<df,>16
			<f,>16
			<df,>16 ~
			<df,>16
		}
		{
			<b,, c,>2.
			<df,>4
			\bar "||"
		}
		\mark \default
		{
			<c, df,>2. \mp
			<g,>4
		}
		{
			<b,>8
			<g,>8 ~
			<g,>4
			<f, g,>2
		}
		{
			<df,>4
			<d,>4 ~
			<d,>4
			<e,>8
			<d,>8 ~
		}
		{
			<d,>2
			<g,>4 ~
			<g,>8
			<bf,>8
			\bar "||"
		}
		{
			<f>2. \f \>
			<f>4 ~
		}
		{
			<f>4
			<gf>2
			<d>4
		}
		{
			<f>2.
			<bf,>4
		}
		{
			<gf,>4
			<df>2. \!
		}
		{
			r2 ~
			r8.
			r16
			r4
		}
		{
			r4
			r2 ~
			r8
			r16
			r16
		}
		{
			r2
			r4
			r4 ~
		}
		{
			r8
			r8
			r2.
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
			<f'>2. \p
			<df'>4
		}
		{
			<df'>2.
			<c'>4
			\bar "|."
		}
	}
}