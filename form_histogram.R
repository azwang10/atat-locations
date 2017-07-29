setwd("~/Desktop")

raw_data <- read.csv(file="tata_locations.csv", header=FALSE, sep=",")

raw_data = t(raw_data)

hist(raw_data, xlab = 'Relative Distance from Gene Start Site', main = 'Where ATAT boxes are located within gene sequences?', breaks = 200)