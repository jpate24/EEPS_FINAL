data <- read.csv('~/Documents/EEPS 1720/code/N_seaice_extent_daily_v3.0.csv')

years = unique(data$Year)
print(years)

yearly_avgs <- list()

for (year in years) {
  curr_data = data[4][data[1] == year]
  average = sum(curr_data) / length(curr_data)
  yearly_avgs <- append(yearly_avgs, average)
}

print(yearly_avgs)

plot(years, yearly_avgs, type='l', main='Sea Ice Yearly (1979 - 2021)', xlab='Years', ylab='Average Ice Cover (10^6 sq km)')