source("Graphs.R")

### Look at loss
charles_loss_ts = read.csv("data/results_chareles.csv", header=F)
charles_loss_ts
s_loss_ts_1 = ts(charles_loss_ts[1])
c_loss_ts = ts(charles_loss_ts[2])

Graphs.ts_double(s_loss_ts_1, c_loss_ts, "Shakespeare" ,"Charles Dickens")

