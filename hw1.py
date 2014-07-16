def resources_vs_time(upgrade_cost_increment, num_upgrades):
  current_time = 0.0
  total_resources = 0
  generation_rate = 1
  upgrade_cost = 1.0
  result = []

  while num_upgrades > 0:
    num_upgrades -= 1
    needed_time = upgrade_cost / generation_rate
    current_time += needed_time
    total_resources += generation_rate * needed_time
    result.append([current_time, total_resources])

    generation_rate += 1
    upgrade_cost += upgrade_cost_increment

  return result

resources_vs_time(1, 10)