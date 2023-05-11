sst_data <- read.csv('~/Documents/EEPS 1720/code/sst_averages.csv')
swh_data <- read.csv('~/Documents/EEPS 1720/code/swh_averages.csv')

x1_coords <- list()
y1_coords <- list()


sst_rows = nrow(sst_data)
swh_rows = nrow(swh_data)



for (row in 1:swh_rows){
  x1_coords <- append(x1_coords, swh_data[row, 2])
  y1_coords <- append(y1_coords, swh_data[row, 1])
}
#set to plot swh
plot(x1_coords, y1_coords,type='h', main='Significant Wave Height Yearly (1979 - 2021)', xlab='Years', ylab='Significant Wave Height (m)')
abline(lm(unlist(y1_coords)~unlist(x1_coords)), col = "red")


