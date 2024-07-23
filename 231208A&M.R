# First Netlogo model analysis
# install.packages("tidyverse")
library("tidyverse")

# loading the model results
results <- read_csv("Cottbus_ABM_DAY4 experiment-table.csv", skip = 6)

glimpse(results)

# satisficing_threshold

results |>
  group_by(satisficing_threshold) |>
  summarise(herdsize_mean_across_runs = mean(herdsize_mean)) ->
  results_mean

view(results_mean)

ggplot(results_mean, aes(x = satisficing_threshold, 
                         y = herdsize_mean_across_runs)) +
  geom_col()
