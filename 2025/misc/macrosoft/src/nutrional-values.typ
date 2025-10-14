#import "@preview/oxifmt:0.2.1": strfmt

#set text(font: "JetBrainsMono NF", size: 10pt)
#set page(margin: (top: 2.5cm, bottom: 2.5cm, left: 2cm, right: 2cm))

#let dark-blue = rgb("003366")
#let primary-blue = rgb("005B9A")
#let light-blue-stripe = rgb("E6F0FA")
#let white-color = rgb("FFFFFF")
#let text-color-on-dark = rgb("FFFFFF")
#let text-color-on-light = rgb("222222")

#let header-padding = (x: 0.7em, y: 0.4em)
#let pizza-name-padding = (x: 0.7em, y: 0.5em)
#let data-cell-padding = (x: 0.7em, y: 0.3em)

#let pizzas = (
  (
    "Aloha Special": (
      ("Classic", "Med", 800, 3347.2000000000003, 33.1, 91, 28.5),
      ("Classic", "Large", 1200.0, 5020.8, 49.65, 136.5, 42.75),
      ("Italian", "Med", 600, 2510.4, 23.1, 71, 23.5),
      ("Italian", "Large", 900.0, 3765.6000000000004, 34.65, 106.5, 35.25),
      ("Pan", "Med", 1400, 5857.6, 63.1, 161, 43.5),
    ),
    "Bacon Bonanza (double)": (
      ("Classic", "Med", 1060, 4435.04, 60, 82, 40),
      ("Classic", "Large", 1590.0, 6652.56, 90.0, 123.0, 60.0),
      ("Italian", "Med", 860, 3598.2400000000002, 50, 62, 35),
      ("Italian", "Large", 1290.0, 5397.360000000001, 75.0, 93.0, 52.5),
      ("Pan", "Med", 1660, 6945.4400000000005, 90, 152, 55),
    ),
    "Carnivore Carnival": (
      ("Classic", "Med", 1330, 5564.72, 77, 86, 64),
      ("Classic", "Large", 1995.0, 8347.08, 115.5, 129.0, 96.0),
      ("Italian", "Med", 1130, 4727.92, 67, 66, 59),
      ("Italian", "Large", 1695.0, 7091.88, 100.5, 99.0, 88.5),
      ("Pan", "Med", 1930, 8075.12, 107, 156, 79),
    ),
    "Cheesus Crust": (
      ("Classic", "Med", 820, 3430.88, 39, 81, 27),
      ("Classic", "Large", 1230.0, 5146.320000000001, 58.5, 121.5, 40.5),
      ("Italian", "Med", 620, 2594.08, 29, 61, 22),
      ("Italian", "Large", 930.0, 3891.1200000000003, 43.5, 91.5, 33.0),
      ("Pan", "Med", 1420, 5941.280000000001, 69, 151, 42),
    ),
    "Cluck & Oink": (
      ("Classic", "Med", 970, 4058.48, 50, 81, 40),
      ("Classic", "Large", 1455.0, 6087.72, 75.0, 121.5, 60.0),
      ("Italian", "Med", 770, 3221.6800000000003, 40, 61, 35),
      ("Italian", "Large", 1155.0, 4832.52, 60.0, 91.5, 52.5),
      ("Pan", "Med", 1570, 6568.88, 80, 151, 55),
    ),
    "Garden Delight": (
      ("Classic", "Med", 787, 3292.808, 33.1, 91.5, 22.6),
      ("Classic", "Large", 1180.5, 4939.212, 49.65, 137.25, 33.9),
      ("Italian", "Med", 587, 2456.0080000000003, 23.1, 71.5, 17.6),
      ("Italian", "Large", 880.5, 3684.012, 34.65, 107.25, 26.4),
      ("Pan", "Med", 1387, 5803.2080000000005, 63.1, 161.5, 37.6),
    ),
    "Greek Getaway": (
      ("Classic", "Med", 855, 3577.32, 41.7, 86.5, 26.1),
      ("Classic", "Large", 1282.5, 5365.9800000000005, 62.55, 129.75, 39.15),
      ("Italian", "Med", 655, 2740.52, 31.7, 66.5, 21.1),
      ("Italian", "Large", 982.5, 4110.78, 47.55, 99.75, 31.65),
      ("Pan", "Med", 1455, 6087.72, 71.7, 156.5, 41.1),
    ),
    "Lean & Green Bird": (
      ("Classic", "Med", 845, 3535.48, 38.2, 84.5, 31.8),
      ("Classic", "Large", 1267.5, 5303.22, 57.3, 126.75, 47.7),
      ("Italian", "Med", 645, 2698.6800000000003, 28.2, 64.5, 26.8),
      ("Italian", "Large", 967.5, 4048.02, 42.3, 96.75, 40.2),
      ("Pan", "Med", 1445, 6045.88, 68.2, 154.5, 46.8),
    ),
    "Mushroom Magic": (
      ("Classic", "Med", 720, 3012.48, 30.3, 83, 21),
      ("Classic", "Large", 1080.0, 4518.72, 45.45, 124.5, 31.5),
      ("Italian", "Med", 520, 2175.6800000000003, 20.3, 63, 16),
      ("Italian", "Large", 780.0, 3263.52, 30.45, 94.5, 24.0),
      ("Pan", "Med", 1320, 5522.88, 60.3, 153, 36),
    ),
    "Pepperoni Classic": (
      ("Classic", "Med", 850, 3556.4, 42, 81, 27),
      ("Classic", "Large", 1275.0, 5334.6, 63.0, 121.5, 40.5),
      ("Italian", "Med", 650, 2719.6, 32, 61, 22),
      ("Italian", "Large", 975.0, 4079.4, 48.0, 91.5, 33.0),
      ("Pan", "Med", 1450, 6066.8, 72, 151, 42),
    ),
    "Pepperoni Overload": (
      ("Classic", "Med", 1000, 4184.0, 54, 82, 34),
      ("Classic", "Large", 1500.0, 6276.0, 81.0, 123.0, 51.0),
      ("Italian", "Med", 800, 3347.2000000000003, 44, 62, 29),
      ("Italian", "Large", 1200.0, 5020.8, 66.0, 93.0, 43.5),
      ("Pan", "Med", 1600, 6694.400000000001, 84, 152, 49),
    ),
    "Quad Combo": (
      ("Classic", "Med", 915, 3828.36, 42.6, 89, 36.3),
      ("Classic", "Large", 1372.5, 5742.54, 63.9, 133.5, 54.45),
      ("Italian", "Med", 715, 2991.56, 32.6, 69, 31.3),
      ("Italian", "Large", 1072.5, 4487.34, 48.9, 103.5, 46.95),
      ("Pan", "Med", 1515, 6338.76, 72.6, 159, 51.3),
    ),
    "Rancher's Choice": (
      ("Classic", "Med", 845, 3535.48, 38.6, 88, 30.3),
      ("Classic", "Large", 1267.5, 5303.22, 57.9, 132.0, 45.45),
      ("Italian", "Med", 645, 2698.6800000000003, 28.6, 68, 25.3),
      ("Italian", "Large", 967.5, 4048.02, 42.9, 102.0, 37.95),
      ("Pan", "Med", 1445, 6045.88, 68.6, 158, 45.3),
    ),
    "Salty Sailor": (
      ("Classic", "Med", 785, 3284.44, 35.5, 81, 29.3),
      ("Classic", "Large", 1177.5, 4926.66, 53.25, 121.5, 43.95),
      ("Italian", "Med", 585, 2447.64, 25.5, 61, 24.3),
      ("Italian", "Large", 877.5, 3671.46, 38.25, 91.5, 36.45),
      ("Pan", "Med", 1385, 5794.84, 65.5, 151, 44.3),
    ),
    "Spinach Feta Fusion": (
      ("Classic", "Med", 793, 3317.9120000000003, 36.2, 85, 25.5),
      ("Classic", "Large", 1189.5, 4976.868, 54.3, 127.5, 38.25),
      ("Italian", "Med", 593, 2481.112, 26.2, 65, 20.5),
      ("Italian", "Large", 889.5, 3721.668, 39.3, 97.5, 30.75),
      ("Pan", "Med", 1393, 5828.312, 66.2, 155, 40.5),
    ),
    "Sweet Heat Wave": (
      ("Classic", "Med", 835, 3493.6400000000003, 35.2, 91, 30.7),
      ("Classic", "Large", 1252.5, 5240.46, 52.8, 136.5, 46.05),
      ("Italian", "Med", 635, 2656.84, 25.2, 71, 25.7),
      ("Italian", "Large", 952.5, 3985.26, 37.8, 106.5, 38.55),
      ("Pan", "Med", 1435, 6004.04, 65.2, 161, 45.7),
    ),
    "The Kitchen Sink": (
      ("Classic", "Med", 1340, 5606.56, 72.2, 105, 57.8),
      ("Classic", "Large", 2010.0, 8409.84, 108.3, 157.5, 86.7),
      ("Italian", "Med", 1140, 4769.76, 62.2, 85, 52.8),
      ("Italian", "Large", 1710.0, 7154.64, 93.3, 127.5, 79.2),
      ("Pan", "Med", 1940, 8116.96, 102.2, 175, 72.8),
    ),
    "The Plain Jane": (
      ("Classic", "Med", 700, 2928.8, 30, 80, 20),
      ("Classic", "Large", 1050.0, 4393.2, 45.0, 120.0, 30.0),
      ("Italian", "Med", 500, 2092.0, 20, 60, 15),
      ("Italian", "Large", 750.0, 3138.0, 30.0, 90.0, 22.5),
      ("Pan", "Med", 1300, 5439.2, 60, 150, 35),
    ),
    "Trio Treat": (
      ("Classic", "Med", 885, 3702.84, 42.4, 87, 28.5),
      ("Classic", "Large", 1327.5, 5554.26, 63.6, 130.5, 42.75),
      ("Italian", "Med", 685, 2866.04, 32.4, 67, 23.5),
      ("Italian", "Large", 1027.5, 4299.06, 48.6, 100.5, 35.25),
      ("Pan", "Med", 1485, 6213.240000000001, 72.4, 157, 43.5),
    ),
    "Volcano Blast": (
      ("Classic", "Med", 850, 3556.4, 39.2, 86, 30.7),
      ("Classic", "Large", 1275.0, 5334.6, 58.8, 129.0, 46.05),
      ("Italian", "Med", 650, 2719.6, 29.2, 66, 25.7),
      ("Italian", "Large", 975.0, 4079.4, 43.8, 99.0, 38.55),
      ("Pan", "Med", 1450, 6066.8, 69.2, 156, 45.7),
    ),
  )
)

#let fmt-float(x) = {
  if type(x) == float {
    let formatted = strfmt("{:.1}", x)
    if formatted.ends-with(".0") {
      strfmt("{:.0}", x)
    } else {
      formatted
    }
  } else {
    str(x)
  }
}

#let processed_rows = ()
#for (pizza_name, variants_data) in pizzas.pairs() {
  processed_rows.push( (table.cell(colspan: 7, align(center, pizza_name)),) )

  for (idx, variant_tuple) in variants_data.enumerate() {
    let current_row_items_list = ()
    let base_type = variant_tuple.at(0)
    let size = variant_tuple.at(1)
    let nutritional_values = variant_tuple.slice(2).map(fmt-float)

    if base_type == "Pan" {
      current_row_items_list.push(base_type)
      current_row_items_list.push(size)
      for v in nutritional_values {
        current_row_items_list.push(v)
      }
    } else {
      if calc.even(idx) {
        current_row_items_list.push(base_type)
        current_row_items_list.push(size)
        for v in nutritional_values {
          current_row_items_list.push(v)
        }
      } else {
        current_row_items_list.push([])
        current_row_items_list.push(size)
        for v in nutritional_values {
          current_row_items_list.push(v)
        }
      }
    }
    processed_rows.push(current_row_items_list)
  }
}

#align(center)[
  #text(size: 20pt, weight: "bold", fill: dark-blue)[Nutritional Information of Our Pizzas]
  #v(2em)
]

#set table(
  stroke: none,
  gutter: 0.6em,
  fill: (column, row_index) => {
    if row_index == 0 { primary-blue }
    else if calc.rem(row_index - 1, 6) == 0 { primary-blue }
    else if calc.even(row_index) { light-blue-stripe }
    else { white-color }
  }
)

#show table.cell: it => {
  let cell_content = it.body

  if it.y == 0 {
    set text(fill: text-color-on-dark, weight: "semibold", size: 1.05em)
    block(width: 100%, inset: header-padding, align(center, cell_content))
  } else if calc.rem(it.y - 1, 6) == 0 {
    set text(fill: text-color-on-dark, weight: "bold", size: 1.15em)
    block(width: 100%, inset: pizza-name-padding, cell_content)
  } else {
    set text(fill: text-color-on-light)
    let aligned_content = cell_content
    if it.x == 0 { aligned_content = align(left, cell_content) }
    else if it.x == 1 { aligned_content = align(center, cell_content) }
    else if it.x >= 2 and it.x <= 6 { aligned_content = align(right, cell_content) }

    block(width: 100%, inset: data-cell-padding, aligned_content)
  }
}

#table(
  columns: 7,
  [Base], [Size], [kcal], [kJ], [Fat (g)], [Carbs (g)], [Protein (g)],
  ..processed_rows.flatten(),
)
