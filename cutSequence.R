
setwd("/Users/luisa/Documents/Spring 2022/Bio Structures/PROJECT")
library(seqinr)

gpcrID <- c("Q86SQ4", "Q9HCU4", "Q9NYQ6")

# read the positions of where to cut
positn <- read.table(file = "Positions.txt", header = T, sep = "", stringsAsFactors = F)

# read the fasta file of the gpcrs
fasta <- read.fasta(file = "gpcrs_cut.fasta", seqtype = "AA", as.string = T, whole.header = F, 
                    strip.desc = F)

# get the number of gpcr in fasta file
num.seq <- (NROW(positn))/2

# row begin = i+(i-1)= 2i-1, row end = i+((i+1)-1)=2i, i = 1:num.seq, rows = 1:NROW(positn) 
seq.fasta <- NULL
seq.ID <- c()

for (i in 1:num.seq) {
  strt <- 2*i-1
  ends <- 2*i
  seq.sub <- substring(fasta[[i]][1], positn[strt, 3], positn[ends, 3])
  seq.ID[i] <- attr(fasta[[i]], "name")
  seq.list <- list(seq = seq.sub)
  seq.fasta <- rbind(seq.fasta, seq.list)
}
# write fasta file
file.out <- paste("gpcrs", "cut2", sep = "_")
file.out <- paste(file.out, "fasta", sep = ".")
write.fasta(sequences = seq.fasta, names = seq.ID, file.out = file.out, open = "w", 
            nbchar = 60, as.string = T)



