
Graphs.ts_double<-function(ts1,ts2,author1,author2){
  plot(ts1, main = paste(author1," VS ", author2, " Loss Over Time"), ylab = "Loss", col = "blue")
  lines(ts2,col = "red")
  legend(x = "topright",legend=c(author2,author1),col = c("red", "blue"),lty = c(1,2))
}