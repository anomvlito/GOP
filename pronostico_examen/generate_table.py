import random

# Target sums
target_x_sum = 637.1
target_r_sum = 59.0

# Fixed out-of-control points
fixed_x = {16: 27.5, 22: 27.6}
fixed_r = {16: 2.6, 22: 2.6}

# We need 23 other values
x_vals = []
for _ in range(23):
    x_vals.append(round(random.uniform(25.1, 25.8), 1))
    
# adjust x_vals to exactly sum to target_x_sum - 55.1 = 582.0
diff = round(582.0 - sum(x_vals), 1)
while abs(diff) > 0.05:
    idx = random.randint(0, 22)
    step = 0.1 if diff > 0 else -0.1
    new_val = round(x_vals[idx] + step, 1)
    if 25.1 <= new_val <= 25.8:
        x_vals[idx] = new_val
        diff = round(582.0 - sum(x_vals), 1)

r_vals = []
for _ in range(23):
    r_vals.append(round(random.uniform(1.5, 3.5), 1))
    
# adjust r_vals to exactly sum to target_r_sum - 5.2 = 53.8
diff = round(53.8 - sum(r_vals), 1)
while abs(diff) > 0.05:
    idx = random.randint(0, 22)
    step = 0.1 if diff > 0 else -0.1
    new_val = round(r_vals[idx] + step, 1)
    if 1.5 <= new_val <= 3.5:
        r_vals[idx] = new_val
        diff = round(53.8 - sum(r_vals), 1)

# build final dictionaries
final_x = {}
final_r = {}
x_idx = 0
for i in range(1, 26):
    if i in fixed_x:
        final_x[i] = fixed_x[i]
        final_r[i] = fixed_r[i]
    else:
        final_x[i] = x_vals[x_idx]
        final_r[i] = r_vals[x_idx]
        x_idx += 1

# Generate the LaTeX table
print(r"\begin{tabular}{cccccc|cccccc}")
print(r"\toprule")
print(r"\textbf{Muestra} & \textbf{$\bar{X}_i$} & \textbf{Mín} & \textbf{Máx} & \textbf{$R_i$} & & \textbf{Muestra} & \textbf{$\bar{X}_i$} & \textbf{Mín} & \textbf{Máx} & \textbf{$R_i$} \\")
print(r"\midrule")
for i in range(1, 14):
    j = i + 13
    
    xi_1 = final_x[i]
    ri_1 = final_r[i]
    min_1 = round(xi_1 - ri_1/2, 1)
    max_1 = round(xi_1 + ri_1/2, 1)
    
    if j <= 25:
        xi_2 = final_x[j]
        ri_2 = final_r[j]
        min_2 = round(xi_2 - ri_2/2, 1)
        max_2 = round(xi_2 + ri_2/2, 1)
        print(f"{i} & {xi_1:.1f} & {min_1:.1f} & {max_1:.1f} & {ri_1:.1f} & & {j} & {xi_2:.1f} & {min_2:.1f} & {max_2:.1f} & {ri_2:.1f} \\\\")
    else:
        print(f"{i} & {xi_1:.1f} & {min_1:.1f} & {max_1:.1f} & {ri_1:.1f} & & & & & & \\\\")

print(r"\bottomrule")
print(r"\end{tabular}")
