library(ggplot2)

Graphs.ts_double<-function(ts1,ts2,author1,author2){
  plot(ts1, main = paste(author1," VS ", author2, " Loss Over Time"), ylab = "Loss", xlab = "Epoch", col = "blue")
  lines(ts2,col = "red")
  legend(x = "topright",legend=c(author2,author1),col = c("red", "blue"),lty = c(1,2))
}

Graphs.ts.ggplot<-function(ts1, main = "Loss Over Time"){
  ggplot(as.data.frame(ts1), aes(1:length(ts1),V1)) + geom_line() +
    xlab("Epoch") + ylab("Loss") + ggtitle(main) + theme(plot.title = element_text(lineheight=.8, face="bold"))
}

Graphs.ts.hist.ggplot<-function(all_loss, shakes_loss, main = "Loss Over Time"){
  qplot(all_loss,
        geom="histogram",
        binwidth = 0.05,  
        main = "Histogram for Age", 
        xlab = "Age",  
        fill=I("blue"), 
        col=I("red"), 
        alpha=I(.2),
        xlim=c(1.6,3.5)) + qplot(all_loss,
                                 geom="histogram",
                                 binwidth = 0.05,  
                                 main = "Histogram for Age", 
                                 xlab = "Age",  
                                 fill=I("blue"), 
                                 col=I("red"), 
                                 alpha=I(.2),
                                 xlim=c(1.6,3.5)) +
    geom_vline(xintercept = shakes_loss)
  all_loss = as.data.frame(all_loss)
  names(all_loss) = "loss"
  shakes_loss = as.data.frame(shakes_loss)
  names(shakes_loss) = "loss"
  all_loss$type = "Random"
  shakes_loss$type = "Shakespeare"
  vegLengths = rbind(all_loss,shakes_loss)
  ggplot(vegLengths, aes(loss, fill = type)) + geom_density(alpha = 0.2) + ggtitle("Histogram For Loss After Validating On Shakespeare Model") + theme(plot.title = element_text(lineheight=.8, face="bold"))
  
}


Graphs.ts.double.ggplot<-function(ts1,ts2,author1,author2){
  if(length(ts1) > length(ts2))
    index = 1:length(ts2)
  else
    index = 1:length(ts1)
  ts1 = ts1[1:length(index)]
  ts2 = ts2[1:length(index)]
  print(ts1)
  ggplot(as.data.frame(cbind(ts1,ts2)), aes(x=index)) + geom_line(aes( y=ts2, colour = "blue")) + geom_line(aes( y=ts1, colour = "red")) +
    scale_color_manual(labels = c(author2, author1), values = c("red","blue")) +
    xlab("Epoch") + ylab("Loss") + ggtitle(main) + theme(plot.title = element_text(lineheight=.8, face="bold"))
}
