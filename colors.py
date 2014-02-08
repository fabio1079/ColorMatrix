COLOR_LIST = [
  "#2700E5", # Blue
  "#1800E4",
  "#0900E3",
  "#0005E3",
  "#0014E2",
  "#0023E1",
  "#0031E1",
  "#0040E0",
  "#004FE0",
  "#005DDF",
  "#006CDE",
  "#007ADE",
  "#0088DD",
  "#0096DD",
  "#00A5DC",
  "#00B3DB",
  "#00C1DB",
  "#00CEDA",
  "#00DAD7",
  "#00D9C8",
  "#00D8B9",
  "#00D8AA",
  "#00D79C",
  "#00D78D",
  "#00D67F",
  "#00D570",
  "#00D562",
  "#00D453",
  "#00D445",
  "#00D337",
  "#00D229", # Green
  "#00D21B",
  "#00D10D",
  "#00D100",
  "#0DD000",
  "#1BCF00",
  "#29CF00",
  "#36CE00",
  "#44CE00",
  "#51CD00",
  "#5ECC00",
  "#6BCC00",
  "#79CB00",
  "#86CB00",
  "#93CA00",
  "#9FC900",
  "#ACC900",
  "#B9C800",
  "#C6C800",
  "#C7BC00",
  "#C6AE00",
  "#C6A000",
  "#C59300",
  "#C58600",
  "#C47800",
  "#C36B00",
  "#C35E00",
  "#C25100",
  "#C24400",
  "#C13700",
  "#C02A00",
  "#C01D00",
  "#BF1000",
  "#BF0300"  # Red
]


def get_color(temp, grade_mult):
  ant = 0
  pos = 0
  i = 0
  color = "#000000"

  if temp == 0.0:
    color = COLOR_LIST[0]
  else:
    for k in range(1, 65):
      pos = k*grade_mult

      if ant < temp <= pos:
        color = COLOR_LIST[i]
        break

      ant = pos
      i += 1

  
  return color
  