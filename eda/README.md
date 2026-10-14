# Exploratory Data Analysis

Ten folder zawiera kod służący do wstępnej analizy, czyszczenia i walidacji danych finansowych (ETF-ów i akcji).

Generowanie wskaźników technicznych (Feature Engineering):
- Trend: Średnie kroczące (np. SMA 20, SMA 50, SMA 200).
- Oscylatory: RSI (Relative Strength Index), MACD.
- Zmienność: Wstęgi Bollingera (Bollinger Bands).
- Wskaźniki oparte o wolumen:
    - Średnia krocząca wolumenu (Volume_SMA).
    - Wskaźnik OBV (On-Balance Volume), pokazujący presję kupna/sprzedaży.

Cechy czasowe (Temporal Features):
    - Dni tygodnia, miesięcy, kwartałów (dają modelowi kontekst sezonowości).
