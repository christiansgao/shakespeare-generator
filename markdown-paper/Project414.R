source("Graphs.R")

### Look at loss
charles_loss_ts = read.csv("data/results_chareles.csv", header=F)
charles_loss_ts
s_loss_ts_1 = ts(charles_loss_ts[1])
c_loss_ts = ts(charles_loss_ts[2])

Graphs.ts.double.ggplot(s_loss_ts_1, c_loss_ts, "Shakespeare" ,"Charles Dickens")

total_loss = read.csv("intervals", header = F)
all_loss = as.numeric(unlist(total_loss[substring(total_loss$V1,1,4) == "test",][2]))
shakes_loss = as.numeric(unlist(total_loss[substring(total_loss$V1,1,4) != "test",][2]))

hemming_no_boot = ts(read.csv("data/montecarlo_hemming_no_boot.csv", header = F)[1])
hemming_with_boot = ts(read.csv("data/montecarlo_hemming_with_boot.csv", header = F)[1])
hemming_with_boot2 = hemming_with_boot[seq(from=1,to=length(hemming_with_boot),length.out=length(hemming_no_boot))]
Graphs.ts.double.ggplot(hemming_no_boot, hemming_with_boot2, "Hemmingway No Bootstrap" ,"Hemmingway With Bootstrap")


intervals = readLines("intervals")
intervals2 = intervals[seq(2,112,2),]

write.csv(as.data.frame(intervals2), "interval2.txt", row.names = F)
