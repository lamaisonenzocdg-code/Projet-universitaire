# Packages
library(yfR)
library(dplyr)
library(writexl)

# Paramètres
tickers <- c("AAPL", "^GSPC")
first_date <- seq(last_date, length.out = 2, by = "-5 years")[2]
last_date  <- Sys.Date()

# Téléchargement quotidien
df_yf <- yf_get(
  tickers    = tickers,
  first_date = first_date,
  last_date  = last_date,
  freq_data  = "monthly",       # mensuel
  type_return = "log"         # ajoute ret_adjusted_prices (log)
)

# Colonnes utiles: date + cours ajusté
df_sel <- df_yf %>%
  select(ticker, ref_date, price_adjusted) %>%
  rename(Date = ref_date, Cloture_Ajustee = price_adjusted)

# Séparer Apple et S&P 500
df_aapl <- df_sel %>% filter(ticker == "AAPL") %>% select(Date, Cloture_Ajustee)
df_gspc <- df_sel %>% filter(ticker == "^GSPC") %>% select(Date, Cloture_Ajustee)

# Export Excel (2 feuilles) + fichiers séparés
write_xlsx(list(AAPL = df_aapl, GSPC = df_gspc), "AAPL_GSPC_journalier.xlsx")
write_xlsx(df_aapl, "AAPL_journalier.xlsx")
write_xlsx(df_gspc, "GSPC_journalier.xlsx")

# Aperçu
print(head(df_aapl))
print(head(df_gspc))


